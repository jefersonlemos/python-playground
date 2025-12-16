# Purpose
This API will read Bank data from a file, will parse and output to a desired format. This output can be then used to import to other systems.


Capabilities




## v0.1

* :construction_worker: Input formats: csv or ofx or both, yet to decide
* :construction_worker: Generic input - the api will common known fields in order to parse them, for example:
    1. Date
    2. Value
    3. Comment
    4. Payment_form
    It's not possible to add new input fields via API.
3. The output will be based on profiles, so the user will be able to create a profile for an app that requires a specific CSV format. The output fields will always have to be linked to an input field.
2. Parse the input file and output it according to the desired profile, for example:
Let's say you want to output to the my_finance_app format, you can map the fields from the Inter bank, like below:
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