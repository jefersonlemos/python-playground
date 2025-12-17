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
```
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install -r requirements.txt && \
uvicorn finance_api.main:app --reload --app-dir src
```