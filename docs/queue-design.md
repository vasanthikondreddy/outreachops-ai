# Queue Design

## States
PENDING → CALLING → CONNECTED → COMPLETED/ESCALATED; failure states include NO_ANSWER, BUSY, VOICEMAIL, DROPPED, RETRY_SCHEDULED, CALLBACK_SCHEDULED, MANUAL_FOLLOW_UP and FAILED.

## Priority
`score = risk + deadline_urgency + time_since_discharge + 0.2*campaign_priority + 2*attempts`.
Risk = HIGH 50, MEDIUM 30, LOW 10. Deadline urgency rises as remaining hours shrink and is capped. Time since discharge is capped at 20. This intentionally makes a near-cutoff patient capable of overtaking a patient with more campaign priority.

## Capacity
Each hospital has a configured capacity. The prototype reserves available slots under a lock before changing tasks to CALLING. A production multi-worker deployment should replace the process lock with transactional row locking/atomic reservation or a distributed lease.

## Retries
NO_ANSWER/BUSY/DROPPED become RETRY_SCHEDULED with increasing delay. After the maximum attempt count, the task becomes MANUAL_FOLLOW_UP.

## Callbacks
A callback request becomes CALLBACK_SCHEDULED with an explicit timestamp; it is not immediately reinserted into generic work.

## Fairness
Deadline urgency and a bounded age component reduce starvation. Production should add campaign fairness quotas/weighted round-robin if many campaigns compete.

## Failure recovery
Tasks should use leases/heartbeats. The prototype records `worker_id` and `lease_until`; production workers should periodically reclaim stale leases and return them to retry/manual states.
