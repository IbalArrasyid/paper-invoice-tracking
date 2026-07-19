"""
Eksperimen komparatif Rule-Based System dan Decision Tree C4.5
untuk klasifikasi prioritas pengiriman invoice.

Cara menjalankan:
    python compare_priority_models.py
    python compare_priority_models.py --data expert_labeling_sheet.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


FEATURE_COLUMNS = [
    "days_to_cutoff",
    "missed_receive_schedule",
    "month_end_flag",
]
TARGET_COLUMN = "expert_label"
CLASS_LABELS = ["HIGH", "MEDIUM", "NORMAL"]


def predict_rule_based(row: pd.Series) -> str:
    """
    Model knowledge-driven berdasarkan guideline pakar.

    Aturan dibuat eksplisit agar setiap keputusan prioritas dapat ditelusuri
    kembali ke logika bisnis pelanggan, terutama aturan cut-off dan jadwal
    penerimaan dokumen.
    """
    days_to_cutoff = pd.to_numeric(row["days_to_cutoff"], errors="coerce")
    if pd.isna(days_to_cutoff):
        days_to_cutoff = 999

    missed_receive_schedule = str(row["missed_receive_schedule"]).strip()
    month_end_flag = str(row["month_end_flag"]).strip()

    if (
        days_to_cutoff <= 2
        or "Yes" in missed_receive_schedule
        or (month_end_flag == "Yes" and days_to_cutoff <= 4)
    ):
        return "HIGH"

    if 2 < days_to_cutoff <= 10:
        return "MEDIUM"

    if days_to_cutoff > 10 or days_to_cutoff == 999:
        return "NORMAL"

    return "NORMAL"


def load_dataset(csv_path: Path) -> pd.DataFrame:
    """Memuat dataset dan memastikan kolom eksperimen tersedia."""
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset tidak ditemukan: {csv_path}")

    df = pd.read_csv(csv_path)
    missing_columns = [col for col in FEATURE_COLUMNS + [TARGET_COLUMN] if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Kolom berikut tidak ditemukan dalam dataset: {missing_columns}")

    return df


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Membersihkan data minimal agar eksperimen reprodusibel.

    month_end_flag yang kosong dianggap 'No' karena nilai kosong pada atribut ini
    merepresentasikan tidak adanya kondisi akhir bulan pada proses operasional.
    """
    cleaned_df = df.copy()

    cleaned_df["days_to_cutoff"] = pd.to_numeric(
        cleaned_df["days_to_cutoff"], errors="coerce"
    ).fillna(999).astype(int)
    cleaned_df["missed_receive_schedule"] = (
        cleaned_df["missed_receive_schedule"].fillna("No (On Schedule)").astype(str).str.strip()
    )
    cleaned_df["month_end_flag"] = (
        cleaned_df["month_end_flag"].fillna("No").astype(str).str.strip()
    )
    cleaned_df[TARGET_COLUMN] = cleaned_df[TARGET_COLUMN].astype(str).str.strip().str.upper()

    cleaned_df = cleaned_df[cleaned_df[TARGET_COLUMN].isin(CLASS_LABELS)].reset_index(drop=True)
    if cleaned_df.empty:
        raise ValueError("Dataset tidak memiliki baris valid untuk label HIGH, MEDIUM, atau NORMAL.")

    return cleaned_df


def build_c45_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Mengubah fitur kategorikal menjadi numerik dengan One-Hot Encoding.

    scikit-learn membutuhkan input numerik, sedangkan One-Hot Encoding menjaga
    kategori nominal agar tidak diperlakukan sebagai urutan angka.
    """
    feature_df = df[FEATURE_COLUMNS].copy()
    encoded_df = pd.get_dummies(
        feature_df,
        columns=["missed_receive_schedule", "month_end_flag"],
        drop_first=False,
        dtype=int,
    )
    return encoded_df


def print_evaluation(title: str, y_true: pd.Series, y_pred: list[str] | pd.Series) -> None:
    """
    Menampilkan metrik evaluasi klasifikasi.

    classification_report memuat precision, recall, F1-score, dan accuracy,
    sedangkan confusion matrix memperlihatkan pola kesalahan antar kelas.
    """
    print(f"\n{'=' * 80}")
    print(title)
    print("=" * 80)
    print("\nClassification Report:")
    print(
        classification_report(
            y_true,
            y_pred,
            labels=CLASS_LABELS,
            target_names=CLASS_LABELS,
            zero_division=0,
        )
    )

    print("Confusion Matrix:")
    matrix = confusion_matrix(y_true, y_pred, labels=CLASS_LABELS)
    matrix_df = pd.DataFrame(
        matrix,
        index=[f"Actual_{label}" for label in CLASS_LABELS],
        columns=[f"Predicted_{label}" for label in CLASS_LABELS],
    )
    print(matrix_df)


def run_experiment(csv_path: Path, random_state: int) -> None:
    df = clean_dataset(load_dataset(csv_path))

    x_raw = df[FEATURE_COLUMNS]
    x_encoded = build_c45_features(df)
    y = df[TARGET_COLUMN]

    # Stratified split menjaga proporsi HIGH, MEDIUM, dan NORMAL pada data uji.
    x_raw_train, x_raw_test, x_train, x_test, y_train, y_test = train_test_split(
        x_raw,
        x_encoded,
        y,
        test_size=0.20,
        random_state=random_state,
        stratify=y,
    )

    # criterion='entropy' mensimulasikan pemilihan atribut berbasis Information Gain.
    c45_model = DecisionTreeClassifier(
        criterion="entropy",
        random_state=random_state,
    )
    c45_model.fit(x_train, y_train)

    rule_based_predictions = x_raw_test.apply(predict_rule_based, axis=1)
    c45_predictions = c45_model.predict(x_test)

    print(f"Dataset              : {csv_path}")
    print(f"Jumlah data valid    : {len(df)}")
    print(f"Jumlah data latih    : {len(x_train)}")
    print(f"Jumlah data uji      : {len(x_test)}")
    print("\nDistribusi kelas data uji:")
    print(y_test.value_counts().reindex(CLASS_LABELS, fill_value=0))

    print_evaluation("Evaluasi Rule-Based System", y_test, rule_based_predictions)
    print_evaluation("Evaluasi Decision Tree C4.5", y_test, c45_predictions)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Komparasi Rule-Based System dan Decision Tree C4.5 untuk prioritas invoice."
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=Path("expert_labeling_sheet.csv"),
        help="Path dataset CSV. Default: expert_labeling_sheet.csv",
    )
    parser.add_argument(
        "--random-state",
        type=int,
        default=42,
        help="Seed agar pembagian data eksperimen reprodusibel.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_experiment(args.data, args.random_state)
