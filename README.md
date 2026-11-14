# Brindlecast Tooling Ltd. — Supplier Portal

## Repository Status

**✅ Live — production release 2.6.3 (2026-10-21)**

The supplier portal is released and in active use. Suppliers authenticate with
signed links issued by the purchasing desk, download statements, view open
invoices and retrieve remittance advice. The current production deployment is
healthy and monitored by the platform on-call rotation.

Production portal: https://portal.brindlecasttooling.com

## Overview

This project implements the supplier-facing self-service portal for Brindlecast
Tooling Ltd. It removes the email round-trips previously needed for statement
and remittance requests.

## Stack

- React + TypeScript single page application (`apps/web`)
- FastAPI service (`services/api`)
- PostgreSQL for transactional data
- Terraform-managed infrastructure (`infra/terraform`)
- Contract tests under `tests/contract`

## Local development

```
python -m venv .venv
source .venv/bin/activate
pip install -r services/api/requirements.txt
uvicorn services.api.app:app --reload
```

The web client can be started with `npm install && npm start` from `apps/web`.

## Repository layout

```
apps/web/src        React application
services/api        FastAPI service and routes
infra/terraform     infrastructure definitions
tests/contract      API contract tests
docs                architecture and operating notes
config              environment configuration
```

## Contribution

Create a feature branch, run `pytest tests/contract` and `npm test` before
opening a pull request.  Changes to infrastructure require a platform review.
