# Guideline-Based Labeling Consistency Report

## Summary

| Item | Value |
| --- | --- |
| Number of invoices reviewed | 41 |
| Number changed to HIGH | 3 |
| Number changed to MEDIUM | 33 |
| Number remaining NORMAL | 0 |
| Number remaining HIGH | 5 |
| Low-confidence invoices | 0 |
| Potential rule conflicts | 11 |
| Final dataset rows | 105 |
| Final HIGH labels | 27 |
| Final MEDIUM labels | 33 |
| Final NORMAL labels | 45 |

## Rule Frequency

| Rule ID | Frequency |
| --- | --- |
| R6 | 2 |
| R7 | 6 |
| R8 | 30 |
| R9 | 7 |

## Invoices with Low Confidence

No rows.

## Potential Conflicts Between Rules

A conflict is recorded when rule conditions from different priority levels are detected and the published priority order resolves the final label.

| Invoice Number | Current Label | Suggested Label | Applied Rule(s) | All Matching Rule Conditions | Conflict Detail |
| --- | --- | --- | --- | --- | --- |
| S202605-0419 | NORMAL | HIGH | R7 | R7; R8 | R7; R8 |
| S202605-0557 | NORMAL | HIGH | R7 | R7; R8 | R7; R8 |
| S202605-0587 | HIGH | HIGH | R7 | R7; R8 | R7; R8 |
| S202605-0719 | NORMAL | HIGH | R7 | R7; R8 | R7; R8 |
| S202605-0745 | HIGH | HIGH | R7 | R7; R8 | R7; R8 |
| S202605-0764 | HIGH | HIGH | R6 | R6; R8 | R6; R8 |
| S202605-0772 | HIGH | HIGH | R6 | R6; R8 | R6; R8 |
| S202605-1766 | HIGH | HIGH | R7 | R7; R8 | R7; R8 |
| S202605-0632 | NORMAL | MEDIUM | R9 | R9; R10 | R9; R10 |
| S202605-0708 | NORMAL | MEDIUM | R9 | R9; R10 | R9; R10 |
| S202605-0737 | HIGH | MEDIUM | R9 | R9; R10 | R9; R10 |
