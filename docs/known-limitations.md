# Known Limitations and Tradeoffs

- Telephony is simulated rather than connected to a voice provider.
- EHR is a mock abstraction.
- Authentication is demo-grade.
- SQLite is the default for zero-setup local execution; PostgreSQL is the intended relational production direction.
- The scheduler lock is process-local and should become a durable distributed reservation mechanism for multi-worker production deployment.
- Clinical protocols are simplified demo content and must not be used for patient care.
- AI behavior is deterministic for reproducibility and does not constitute clinical judgment.
- Notifications are represented operationally but not integrated with real SMS/email providers.
- The frontend is a lightweight prototype dashboard rather than a production design system.
- No HIPAA/SOC 2 claim is made.
