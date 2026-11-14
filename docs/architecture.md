# Portal architecture

The supplier portal is a small three-tier application:

- `apps/web` - React single-page application served behind the reverse proxy.
- `services/api` - FastAPI service exposing invoice upload, statement and
  remittance endpoints.
- PostgreSQL - stores supplier accounts, invoices and remittance records.
- S3-compatible object storage - stores the uploaded PDF originals.

Authentication uses short-lived signed links issued by the buying organisation;
no supplier passwords are stored by the portal.  Every request is tagged with a
correlation id that is recorded in the audit log.
