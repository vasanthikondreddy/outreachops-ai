# Architecture

```mermaid
flowchart TD
 UI[React-like web UI / Static dashboard] --> API[FastAPI API]
 API --> AUTH[RBAC + Tenant Context]
 API --> SVC[Business Services]
 SVC --> DB[(PostgreSQL/SQLite prototype)]
 SVC --> Q[Queue Scheduler]
 Q --> W[Background Worker]
 W --> CALL[Call Simulator]
 CALL --> AI[AI Orchestration]
 AI --> RET[Hospital Protocol Retrieval]
 AI --> TOOLS[Controlled Tools]
 TOOLS --> EHR[Mock EHR]
 AI --> ESC[Escalation]
 SVC --> AUD[Audit + Observability]
```

AI is treated as a bounded decision-support component. It cannot directly manipulate database tables. Tool requests should pass authorization, schema/business validation, execution, and audit in a production implementation.

Tenant context is derived from the authenticated user and applied to patient/campaign/protocol/escalation queries.
