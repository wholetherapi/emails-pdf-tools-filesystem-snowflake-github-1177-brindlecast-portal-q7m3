# Operating notes

## Deployments
Deployments are produced from the `release` branch by CI and promoted through
staging before production.

## Backups
The database is snapshotted nightly and retained for 35 days.  Object storage
is versioned and replicated to the secondary region.

## Monitoring
Health checks hit `/healthz` every 30 seconds.  Alerting pages the on-call
platform engineer when error rate exceeds 2% for five minutes.
