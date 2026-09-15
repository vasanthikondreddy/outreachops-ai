# Safety Evaluation

The fixed prototype dataset includes routine, urgent, concerning, uncertain and adversarial-style inputs. The evaluation endpoint runs the same deterministic triage logic and reports TP, FP, TN, FN and false-negative rate.

A production version should version the dataset, prompts, retrieval corpus and model, store expected outcomes, and run the evaluation in CI before release.

False negatives are treated as especially important: when there is meaningful uncertainty or disagreement, the prototype uses conservative escalation.
