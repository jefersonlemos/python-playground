def test_import_endpoint_returns_csv(client):
    with open("finance_api/tests/fixtures/sample.ofx", "rb") as f:
        response = client.post(
            "/v1/file/import",
            files={"file": ("sample.ofx", f, "application/xml")},
            data={
                "due_date": "2026-02-10",
                "card_name": "Nubank",
                "account": "Main",
            },
        )

    assert response.status_code == 200
    body = response.json()

    assert body["filename"] == "sample.ofx"
    assert "csv_content" in body
    assert "Coffee Shop" in body["csv_content"]
