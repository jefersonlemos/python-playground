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
        #TODO - Add it manually via API
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
        "column": "Nome do Cartão",
        "default": "CardName not defined"
    },    
    "_conta": {
        "column": "Conta",
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


