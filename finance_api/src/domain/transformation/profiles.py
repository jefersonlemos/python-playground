# profiles.py

DEFAULT_PROFILE = {
    "memo": {
        "column": "Descrição",
        "default": ""
    },
    "amount": {
        "column": "Valor",
        "default": ""
    },
    "date": {
        "column": "Data de Lançamento", #When the debit happened
        "default": ""
    },    
    "due_date": {
        "column": "Data de Vencimento", #Card due date
        #TODO - Add due date manually via API
        #IMPROVEMENT - Add the credit card to the system and then select it when generating the csv
        "default": ""
    },
    "_categoria": {
        "column": "Categoria",
        "default": "Variáveis"
    },
    "_subcategoria": {
        "column": "Subcategoria",
        "default": "Outros"
    },
    "_cartao": {
        #TODO - Add card name via API
        "column": "Nome do Cartão",
        #IMPROVEMENT - This will be then set on the credit card definition        
        "default": "TBD"
    },    
    "_conta": {
        #TODO - Add account name via api        
        "column": "Conta",
        #IMPROVEMENT - This will be then set on the credit card definition        
        "default": "Account not defined"
    },

    "_observacoes": {
        "column": "Observações",
        #TODO - {date} is not working
        "default": "Compra feita em {date}"
    }
}

INTER_CURRENT = {
    # custom mapping
}

NUBANK_CREDIT_CARD = {
    # custom mapping
}


