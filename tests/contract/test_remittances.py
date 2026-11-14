def test_list_remittances(client):
    response = client.get("/api/supplier/remittances")
    assert response.status_code == 200


def test_missing_remittance_returns_404(client):
    response = client.get("/api/supplier/remittances/does-not-exist")
    assert response.status_code == 404
