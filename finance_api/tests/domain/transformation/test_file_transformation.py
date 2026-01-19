from pathlib import Path
from fastapi import UploadFile

from domain.transformation.file_transformation import FileTransformer


FIXTURES = Path(__file__).parent.parent / "fixtures"


def test_ofx_transformation_with_manual_fields():
    ofx_path = FIXTURES / "sample.ofx"

    with open(ofx_path, "rb") as f:
        upload = UploadFile(filename="sample.ofx", file=f)

        transformer = FileTransformer()
        csv_output = transformer.transform(
            upload,
            manual_fields={
                "due_date": "2026-02-10",
                "_cartao": "Nubank",
                "_conta": "Main Account",
            },
        )

    assert "Coffee Shop" in csv_output
    assert "2026-02-10" in csv_output
    assert "Nubank" in csv_output
    assert "Main Account" in csv_output
