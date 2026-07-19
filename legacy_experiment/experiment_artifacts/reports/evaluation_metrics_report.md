# Evaluation Metrics

Metrics are generated for the full dataset and for the 20% stratified test split.

| scope | model | n | accuracy | weighted_precision | weighted_recall | weighted_f1 | macro_precision | macro_recall | macro_f1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| full_dataset | RuleBased | 107 | 0.6729 | 0.9363 | 0.6729 | 0.7593 | 0.5758 | 0.5151 | 0.522 |
| full_dataset | DT | 107 | 0.9907 | 0.991 | 0.9907 | 0.9907 | 0.6538 | 0.6626 | 0.6581 |
| test_split | RuleBased | 22 | 0.6818 | 0.9351 | 0.6818 | 0.7618 | 0.5714 | 0.5294 | 0.5247 |
| test_split | DT | 22 | 0.9545 | 0.9621 | 0.9545 | 0.9559 | 0.6111 | 0.6471 | 0.6263 |
