# AI Usage

The prototype exposes the architecture expected by the PRD: Voice Intake, Clinical Triage, Escalation Assessment/Consensus and Documentation. For reproducibility, the included implementation uses deterministic simulated AI/rules. A provider adapter can replace `triage()` with structured LLM calls while preserving Pydantic validation and controlled tools.

Protocol retrieval is tenant-scoped by `hospital_id`. Triage evidence includes the conversation and protocol reference. Model output must be validated before business actions.
