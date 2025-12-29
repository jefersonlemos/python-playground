# Padrao do App MyFinance
`Descrição,Valor,Data Venc,Categoria,Subcategoria,Conta,Nome Cartão,Observações`
```
Test1,10,12/01/2026,Variáveis,Remédios,Inter,Cartao Elo,
Test2,12,12/01/2026,Variáveis,Remédios,Inter,Cartao Elo,
```

- Precisa importar sem o cabeçalho
- Se eu colocar a data correta do vencimento, cai na fatura errada
- Ou seja, se em janeiro eu coloco a data do vencimento como 12/12/2025, cai na fatura de dezembro mas o vencimento dela é janeiro
- Para o lançamento aparecer na fatura de janeiro, é necessário que a data de vencimento seja igual à data de vencimento do cartao cadastrado no app


# Modelo Nubank
`Descrição,Valor,Data de Lançamento,Data de Vencimento,Categoria,Subcategoria,Cartão de Crédito,Conta`

- Pode importar com o cabeçalho
- A data do lançamento pode ser a data real, 
- A data de vencimento precisa ser igual à data de vencimento do cartao cadastrado no app

## Exemplo de um lançamento em OFX
```
<TRNTYPE>DEBIT</TRNTYPE>
<DTPOSTED>20251212000000[-3:BRT]</DTPOSTED>
<TRNAMT>-11.93</TRNAMT>
<FITID>90f487hh-3b5f-4983-b883-dfac1a81103k</FITID>
<MEMO>Uber Uber *Trip Help.U</MEMO>
</STMTTRN>
<STMTTRN>
```

TRNTYPE -> Debito -  Ignorar quando for <TRNTYPE>CREDIT</TRNTYPE>

Descrição,Valor,Data de Lançamento,Data de Vencimento,Categoria,Subcategoria,Cartão de Crédito,Conta
MEMO(Descrição),TRNAMT(Valor),DTPOSTED(Data de Lançamento),,,,

## Plano
- Fase 1 - gerar o output com categorias e o resto todo vazio e aí fazer isso manualmente depois no Excel
    Nessa fase, vou passar o ofx e ele vai pegar os lançamentos
    Caso nao tenha a data de vencimento no ofx, add via api
- Fase 2, - via api, add o cartao de credito e a conta
- Fase 3 - via api ou automaticamente, durante o transforming, add categoria e subcategoria



