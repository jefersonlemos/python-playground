# profiles.py

DEFAULT_PROFILE = {
    "memo": {
        "column": "Description",
        "default": ""
    },
    "amount": {
        "column": "Amount",
        "default": ""
    },
    "date": {
        "column": "Data de Vencimento",
        "default": "13/{current_month}/{current_year}"
    },
    "_categoria": {
        "column": "Categoria",
        "default": "Variáveis/Outros"
    },
    "_subcategoria": {
        "column": "Subcategoria",
        "default": ""
    },
    "_conta": {
        "column": "Conta",
        "default": "TBD"
    },
    "_cartao": {
        "column": "Nome do Cartão",
        "default": "TBD"
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


