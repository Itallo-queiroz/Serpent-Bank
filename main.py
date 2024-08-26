# importação
import os
from modulo import *

# programa principal
if __name__== '__main__':
    # Lista de dicionarios
    correntistas = {
            'Nome':'',
            'Saldo':0
        }
# Entrada no programa
    while True:
        exibir_menu()
        opcao = input('opção deejada: ')
        os.system('cls')

        #   cadastrar um novo correntista
        if opcao == '1':
            #criar um dicionario
            correntista = {
                'Nome':'',
                'Saldo':0
            }

            correntista['Nome'] = input('Informe o nome a ser cadastrado: ')
            correntistas.append(correntista)
            print(f'{correntista['Nome']} cadrasto com sucesso. ')
            continue
        # entrada nas operações
        elif opcao == '2':
            titular = input('Informe o nome do titular: ')
            try:
                # pesquisa pelo correntista
                for i in range(len(correntistas)):
                    if titular in correntistas[i]['Nome']:
                        nome = correntistas[i]['Nome']
                        saldo = correntistas[i]['Saldo']

                        # Exibe as operações
                        while True:
                            exibir_dados(nome, i, saldo)
                            exibir_operacoes()

                            operacao = input('Operaçao desejada: ')
                            os.system('cls')
                            # verificar a operaçao escolhida
                            match operacao:
                                # exibe o saldo
                                case '1':
                                    print(f'Saldo: R$ {saldo:,.2f}')
                                    continue
                                # deposito
                                case '2':
                                    valor = str(input('Valor do deposito: R$ '))
                                    valor = float(valor.replace('.', ''))
                                    saldo = depositar_valor(saldo, valor)
                                    correntista[i]['Saldo'] = saldo
                                    print('Deposito efetuado com sucesso.')
                                    print(f'Saldo atual:  R$ {saldo:,.2f}')
                                    continue
                                # Saque
                                case '3':
                                    valor = str(input('Valor do saque: R$ '))
                                    valor = float(valor.replace('.', ''))

                                    if valor < saldo:
                                        saldo = sacar_valor(saldo, valor)
                                        correntista[i]['Saldo'] = saldo
                                        
                                        print('Saque efetuado com sucesso.')
                                        print(f'Saldo atual:  R$ {saldo:,.2f}')
                                    else:
                                        print('Saldo insuficiente.')
                                    continue
                                # encerrar as operaçoes e volta para o menu anterior
                                case '4':
                                    break
                                # operação inexistente
                                case _:
                                    print('Operação invalida.')
                                    continue
                    # avança para o proximo loop caso o nome nao seja encontrado
                    else:
                        continue
            # mensagem de nome não encontrado
            except:
                print(f'{nome} não encontrado.')
            # voltar para o menu anterior
            continue
        # exibir a lista de correntista
        elif opcao =='3':
            for correntista in correntistas:
                print(correntista)
            continue
        # excluir correntista
        elif opcao == '4':
            indice = int(input('Informe o ID da conta a ser excluida: '))
            
            try:
                del [correntistas[indice]]
                print('Conta {indice} deletada com sucesso.')
            except:
                print('Não foi possivel deletar conta.')
            continue
        # encerrar programa
        elif opcao == '5':
            break
        # invalidar a opçao
        else:
            print('Opção invalida.')


    










































