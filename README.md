# Multi-Hospital Post-Discharge Outreach Platform

Prototype implementation of the attached PRD. It demonstrates multi-tenancy, RBAC-ready authentication, hospital configuration, patient/discharge data, campaigns, explainable eligibility/priority queueing, centralized capacity control, call outcomes, retries, callbacks, AI-style structured triage, tenant-aware protocols, conservative escalation consensus, human review, mock EHR-oriented documentation, audit logging, dashboards, and safety evaluation.

## Quick start (Windows / macOS / Linux)

### 1. Python
Use Python 3.11 or 3.12.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run

```bash
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000

Demo users: `admin`, `manager`, `reviewer`, `platform`, `hospital2`. The login field acts as the demo bearer identity; this is intentionally prototype authentication, not production auth.

### 3. Demo flow
1. Login as `admin`.
2. Click **Create & Start**.
3. Click **Schedule** repeatedly to observe capacity-limited selection.
4. Select a task and simulate `NO_ANSWER`, `BUSY`, `DROPPED`, `CALLBACK`, `URGENT`, or `ROUTINE`.
5. Observe retries/manual follow-up or escalation.
6. Resolve an escalation as a human reviewer.
7. Run Safety Evaluation.

## Docker

```bash
docker compose up --build
```

Open http://localhost:8000.

## API
FastAPI Swagger UI: http://127.0.0.1:8000/docs

Key endpoints:
- `/api/hospitals`
- `/api/patients`
- `/api/campaigns`
- `/api/campaigns/{id}/start`
- `/api/queue`
- `/api/queue/schedule`
- `/api/tasks/{id}/simulate`
- `/api/escalations`
- `/api/escalations/{id}/resolve`
- `/api/dashboard`
- `/api/evaluation/run`
- `/api/audit`

## Queue design
Priority is recalculated from clinical risk, deadline urgency, time since discharge, campaign priority, and attempt adjustment. Capacity is reserved under a process lock for the prototype; production should use transactional DB/Redis coordination across multiple processes/hosts. Callback tasks remain outside the generic immediate queue until their callback time.

## Safety
The prototype uses deterministic rules in place of a paid model so it is reproducible. It produces structured triage, performs a second independent-style assessment, escalates red flags/uncertainty/disagreement, and reports TP/FP/TN/FN and false-negative rate.

## Important prototype limitation
This is NOT a clinical product and does not claim HIPAA/SOC 2 compliance. Telephony is simulated, EHR is mocked, authentication is demo-grade, and the concurrency lock is process-local. Before real patient use, replace these with production identity, authorization, encrypted infrastructure, durable distributed locking, audited EHR integration, validated clinical protocols, security/privacy controls, and formal clinical safety validation.
on.
