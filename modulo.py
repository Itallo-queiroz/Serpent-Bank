# importa função de data
from datetime import date

# Função exiir o menu
def exibir_menu():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f'\n{'=' * 20} Serpent Bank | {dia}/{mes}/{ano} {'=' * 20}\n')
    print('1 - Criar conta')
    print('2 - Entrar na conta')
    print('3 - Exibir correntistas')
    print('4 - Excluir Conta')
    print('5 - encerrar programa')

# função exibir operações
def exibir_operacoes():
    print('\nOPERAÇÕES\n')
    print('1 - Consultar saldo ')
    print('2 - Depositar valor')
    print('3 - Sacar valor')
    print('4 - Voltar ')

# função exibir dados do correntista
def exibir_dados(nome, i, saldo):
    print(f'ID: {i}' )
    print(f'Nome: {nome} ')
    print(f'Agência: 1001 ')
    print(f'Conta: 1001{i} ')
    print(f'Saldo: R$ {saldo} ')

# função depósito
def depositar_valor(saldo, valor):
    saldo += valor
    return saldo

# Função de saque
def sacar_valor(saldo, valor):
    saldo -= valor
    return saldo




































