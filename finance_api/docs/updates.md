### 2026-01-19

I finished the file importing and transformation, tested on MyFinances app and it seems to be working.
Next steps:
- I tested with only one transaction, test now with the whole bill
- Ensure that the tests are passing, they're not yet
```
====================================================================================================== FAILURES ======================================================================================================
__________________________________________________________________________________________ test_import_endpoint_returns_csv __________________________________________________________________________________________

client = <starlette.testclient.TestClient object at 0x7f30b5aeebf0>

    def test_import_endpoint_returns_csv(client):
>       with open("finance_api/tests/fixtures/sample.ofx", "rb") as f:
E       FileNotFoundError: [Errno 2] No such file or directory: 'finance_api/tests/fixtures/sample.ofx'

tests/domain/importing/test_file_import.py:2: FileNotFoundError
_____________________________________________________________________________________ test_ofx_transformation_with_manual_fields _____________________________________________________________________________________

    def test_ofx_transformation_with_manual_fields():
        ofx_path = FIXTURES / "sample.ofx"
    
>       with open(ofx_path, "rb") as f:
E       FileNotFoundError: [Errno 2] No such file or directory: '/home/jeferson/1.personal/POC/python-playground/finance_api/tests/domain/fixtures/sample.ofx'

tests/domain/transformation/test_file_transformation.py:13: FileNotFoundError
============================================================================================== short test summary info ===============================================================================================
FAILED tests/domain/importing/test_file_import.py::test_import_endpoint_returns_csv - FileNotFoundError: [Errno 2] No such file or directory: 'finance_api/tests/fixtures/sample.ofx'
FAILED tests/domain/transformation/test_file_transformation.py::test_ofx_transformation_with_manual_fields - FileNotFoundError: [Errno 2] No such file or directory: '/home/jeferson/1.personal/POC/python-playground/finance_api/tests/domain/fixtures/sample.ofx'
============================================================================================ 2 failed, 3 passed in 0.09s =============================================================================================
```
- Ensure that all defined tasks are finished
- Proceed to deployment to local cluster.
    - Build
    - Pipeline to deploy
- When it's deployed and running, block main branch and start working with feature-branch