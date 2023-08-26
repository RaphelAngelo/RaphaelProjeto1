from banco import obterConta, banco

def trasferir(contaOri: int, contaDes: int, valor: float) -> None:
    contaOrigem = obterConta(contaOri)
    contaDestino = obterConta(contaDes)
    if contaOrigem and contaDestino:
        if contaOrigem['saldo'] >= valor:
            contaOrigem['saldo'] -= valor
            contaDestino['saldo'] += valor
            print('Transferência realizada com sucesso!')
        else:
            print('Saldo insulficiente para transferência!')
    else:
        print('Uma ou mais contas não econtradas!')
