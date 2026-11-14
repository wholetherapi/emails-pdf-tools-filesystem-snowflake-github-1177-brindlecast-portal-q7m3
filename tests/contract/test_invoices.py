import uuid

def test_list_invoices_returns_paginated_payload(client):
    response = client.get("/api/supplier/invoices")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_upload_invoice_requires_file(client):
    response = client.post("/api/supplier/invoices")
    assert response.status_code == 422


def test_upload_invoice_roundtrip(client, sample_pdf):
    response = client.post(
        "/api/supplier/invoices",
        files={"file": ("invoice.pdf", sample_pdf, "application/pdf")},
    )
    assert response.status_code == 201
    body = response.json()
    uuid.UUID(body["id"])
