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


def test_import_endpoint_requires_file(client):
    response = client.post("/v1/file/import")
    assert response.status_code == 422


def test_import_endpoint_rejects_missing_filename(client):
    import io
    response = client.post(
        "/v1/file/import",
        files={"file": ("", io.BytesIO(b"test"), "text/plain")},
    )
    assert response.status_code == 400


def test_import_endpoint_returns_all_required_fields(client):
    with open("finance_api/tests/fixtures/sample.ofx", "rb") as f:
        response = client.post(
            "/v1/file/import",
            files={"file": ("sample.ofx", f, "application/xml")},
        )

    assert response.status_code == 200
    body = response.json()

    assert "filename" in body
    assert "content_type" in body
    assert "csv_content" in body


def test_import_endpoint_with_optional_fields(client):
    with open("finance_api/tests/fixtures/sample.ofx", "rb") as f:
        response = client.post(
            "/v1/file/import",
            files={"file": ("sample.ofx", f, "application/xml")},
            data={
                "due_date": "2026-03-15",
                "card_name": "Credit Card",
                "account": "Checking",
            },
        )

    assert response.status_code == 200
    body = response.json()
    assert "2026-03-15" in body["csv_content"]
    assert "Credit Card" in body["csv_content"]
    assert "Checking" in body["csv_content"]


def test_import_endpoint_rejects_invalid_file(client):
    import io
    response = client.post(
        "/v1/file/import",
        files={"file": ("bad.ofx", io.BytesIO(b"\x00\x01\x02"), "application/xml")},
    )
    assert response.status_code == 422
