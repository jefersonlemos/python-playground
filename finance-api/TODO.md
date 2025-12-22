# Finance API TODO
## v0.1.0
### Feature
- [ ] **Upload Capability**
  - [x] Create the endpoint, it should be shown on swagger UI
  - [x] Add the upload capability with basic extension validation (csv, ofx)
  - [ ] Add the validation capability
    - [ ] In FastAPI/ASGI, enforce max upload size
    - [x] Read only the first few KB, never the whole file.

        Reject if:  
        - [x] Binary content detected
        - [x] Null bytes present
        - [x] UTF-8 verification failed
        - [ ] Set depth / size limits
    
    ### Tests
    - [] Add unit tests for file upload
    ### Fix
    - [] OpenSwagger UI is showing file and import as two different endpoints

- [ ] **Create the file transformer class**
    - This class will receive the verified ofx file, read it and output the csv with the desired columns
    CSV output sanitization
    Before exporting CSV:
        Prefix dangerous cells with '
        Escape formulas starting with:
            =,+,-,@





