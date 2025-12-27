# Project description
This is an API capable of reading bank data from a file (input), parse and output to a desired csv format (output), it's an ETL. 

# Purpose
Each bank
This output can be used afterwards to import bank data to other systems, like personal finance apps.

## Capabilities

### v0.1.0

* :construction_worker: Input formats: csv or ofx or both, yet to decide
* :construction_worker: Generic input - the api will have common known fields in order to parse them, for example:
    1. Date
    2. Value
    3. Comment
    4. Payment_form
    It's not possible to add new input fields via API.
* :construction_worker: Conversion based on profiles - The output will be based on profiles, so the user will be able to create a profile for an app that requires a specific CSV format. The output fields will always have to be linked to an input field. 
Let's say that the user wants to convert the csv from a bank to import to the MyFinance app. The bank csv contains the Date, Value, Payment_form and Location columns and the user needs Payment_Date, Value, Payment_form, Where. That's how the profile will look like:
```
    my_finance_app_profile: {
        Date: Payment_date
        Value: value
        Payment_form: payment_form
        Location: Where
    }
```
It will output a csv file with the following data:
`Payment_date, value,payment_form, where`

Up to this moment, it will come with a default profile.

# How to run

## Development
### Installing the dependencies
```
python -m venv .venv && \
source .venv/bin/activate && \
python -m pip install -r requirements.txt && \
python -m pip install -e .
```

### Starting the environment locally
```
source .venv/bin/activate && \
uvicorn main:app --reload --app-dir src
```

## Production

# Endpoints

## 1. API Docs

### Swagger UI
http://127.0.0.1:8000/docs
### API doc via Redoc
http://127.0.0.1:8000/redoc
### Get the OpenAPI spec
http://127.0.0.1:8000/openapi.json

## 2. File Operations

### Import files
http://127.0.0.1:8000/v1/file/import

```
curl -X POST -F "file=@testing.csv;type=multipart/form-data" http://localhost:8000/v1/file/import
```