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
    "DTPOSTED": {
        "column": "Data de Lançamento", #When the debit happened
        #TODO - Current day, the day the csv is bein generated
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
        "default": "Compra feita em {date}"
    }
}

INTER_CURRENT = {
    # custom mapping
}

NUBANK_CREDIT_CARD = {
    # custom mapping
}


