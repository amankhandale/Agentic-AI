# Agentic-AI [Testing & Evaluation]
Status: STAGING / EVALUATION

This branch is the gatekeeper. Code here is being benchmarked against "Golden Datasets" before being promoted to Developed (Main).

# Promotion Requirements
To move code from Testing ➔ Developed, the following must be true:
* 100% pass rate on core logic unit tests.
* 90% success rate on the "Reasoning Benchmark."
* No regression in performance compared to the previous version.
* Documentation in docs/ is updated to match new capabilities.

# [!IMPORTANT]
Do not write new features in this branch. Only bug fixes and evaluation scripts should be committed here.
