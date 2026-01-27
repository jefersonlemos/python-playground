# Finance API TODO
## v0.1.0
### Feature
- [ ] **Upload Capability**
  - [x] Create the endpoint, it should be shown on swagger UI
  - [x] Add the upload capability with basic extension validation (csv, ofx)
  - [x] Add the File validation capability - minimum security and consistency
  - [x] Tests - File validation capability
    - [x] In FastAPI/ASGI, enforce max upload size
    - [x] Tests - Enforce max upload size
    - [ ] In NGINX, enforce max upload size
    - [x] Read only the first few KB, never the whole file.

        Reject if:  
        - [x] Binary content detected
        - [x] Null bytes present
        - [x] UTF-8 verification failed
        - [ ] Set depth / size limits
    
    ### Tests
    - [x] Add unit tests for file upload
    ### Fix
    - [ ] OpenSwagger UI is showing file and import as two different endpoints

- [x] **Transforming capability** -> [Details](transforming.md)
    - [X] Create the file transformer class to output a csv with the default [columns](transforming.md) of the MyFinance app
        - This class will receive the verified ofx file, read it and output the csv with the desired columns
        CSV output sanitization
        Before exporting CSV:
            Prefix dangerous cells with '
            Escape formulas starting with:
                =,+,-,@
    - [x] Add the class tests and ensure that they're passing






