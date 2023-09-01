from Operações.consulta import consultarSaldo
from Operações.saque import sacar
from Operações.deposito import depositar
from Operações.transferencia import trasferir
from banco import *

def menu():
    while True:
        print("---- BEM VINDO AO MENU ----")
        print("1 - Adicionar conta")
        print("2 - Editar nome")
        print("3 - Consultar nome")
        print("4 - Excluir conta")
        print("5 - Listar todos")
        print("6 - Realizar saque")
        print("7 - Realizar deposito")
        print("8 - Realizar transferência")
        print("9 - Consultar saldo")
        print("10 - Sair")
        opcao = int(input('Selecione uma opção: '))
        if opcao == 1:
            nome = input('Digite o nome do cliente: ')
            saldo = float(input('Digite saldo: '))
            adicionarConta(nome, saldo)
        elif opcao == 2:
            conta = int(input('Digite o número do cliente: '))
            nome = input('Digite o novo nome do cliente: ')
            editarNome(conta, nome)
        elif opcao == 3:
            conta = int(input('Digite o número da conta: '))
            buscarCliente(conta)
        elif opcao == 4:
            conta = int(input('Digite o número da conta: '))
            removerConta(conta)
        elif opcao == 5:
            listarTodos()
        elif opcao == 6:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor de saque: '))
            sacar(conta, valor)
        elif opcao == 7:
            conta = int(input('Digite o número da conta: '))
            valor = float(input('Digite o valor do deposito: '))
            depositar(conta, valor)
        elif opcao == 8:
            contaOrigem =  int(input('Informe a conta de origem: '))
            contaDestino = int(input('Informe a conta de destino: '))
            valor = float(input('Digite o valor que deseja transferir: '))
            trasferir(contaOrigem, contaDestino, valor)
        elif opcao == 9:
            conta = int(input('Digite o número da conta: '))
            consultarSaldo(conta)
        elif opcao == 10:
            print('---- VOCÊ SAIU DO PROGRAMA ----')
            break
        else:
            print('Opção inválida!')

menu()
