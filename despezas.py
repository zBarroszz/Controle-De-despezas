
from time import sleep

print('============= CONTROLADOR DE DIVIDAS =============')
print('==================================================')
sleep(0.5)

# 1. VARIÁVEIS GERAIS

dividas = []
saldo_usuario = 0.0
# PRÓXIMO PASSO:
# Futuramente, podemos criar outras listas ou estruturas
# para armazenar pagamentos realizados e histórico financeiro.


# 2. FUNÇÃO DO MENU

def mostrar_menu():
    while True:
        try:  
            print('[1] Cadastrar Dívida\n'
                '[2] Consultar Dívida\n'
                '[3] Editar Dívida\n'
                '[4] Remover Dívida\n'
                '[5] Registrar Pagamento\n'
                '[6] Consultar Saldo\n'
                '[7] Resumo Financeiro\n'
                '[8] Sugestões Financeiras\n\n'
                '[0] Sair\n')

            escolha = int(input('Escolha: '))
            
            if escolha not in (1, 2, 3, 4, 5, 6, 7, 8, 0):
                sleep(0.3)
                print('Escolhe um valor disponivel por favor!')
                sleep(0.3)
                continue
            break
        except ValueError:
            sleep(0.5)
            print('Valor invalido, digite novamente!!')
            sleep(0.3)
    return escolha
        
  #FUNÇÃO 100% REPARADA


# 3. FUNÇÃO DE CADASTRO

def cadastrar_divida():
    nome_divida = input('Informe o título da sua dívida: ')

    valor_divida = float(input('Qual o valor total da sua dívida: '))

    qnt_parcelas = int(input('Qual a quantidade de parcelas?: '))

    vlr_parcelas = float(input('Qual o valor da parcela?: '))

    vencimento = input('Qual a data de vencimento?: ')

    ctg_divida = input('Qual a categoria da sua dívida?: ')

    divida = {'ID': len(dividas) + 1,
              'Nome da Divida': nome_divida,
              'Valor total': valor_divida,
              'Parcelas': qnt_parcelas,
              'Valor das parcelas': vlr_parcelas,
              'Vencimento': vencimento,
              'Tipo': ctg_divida
              }

    dividas.append(divida)
    print('\nDívida cadastrada com sucesso!')

    # MELHORIAS FUTURAS:
    # 1. Validar valores negativos ou iguais a zero.
    # 2. Validar quantidade de parcelas.
    # 3. Melhorar a geração dos IDs para evitar repetições
    #    quando uma dívida for excluída.
    # 4. Validar o formato da data de vencimento.


# 4. FUNÇÃO DE CONSULTA

def consultar_divida():
    while True:
        if not dividas:
            print('Não há dívidas registradas!')
            sleep(0.5)
            break
        else:
            for divida in dividas:
                
                print(f"ID: {divida['ID']} -=-=-=-=-=- {divida['Nome da Divida']} -=-=-=-=-= R${divida['Valor total']:.2f}")
                   
                sleep(0.3)
            escolha_saida = int(input('Oque você deseja fazer?\n[0] Verificar divida ID\n[1] Voltar ao menu principal\nEscolha: '))
            if escolha_saida == 1:
                sleep(1)
                break
            elif escolha_saida == 0:
                programa = True
                while programa:
                    try:    
                        sleep(0.5)
                        id_escolha = int(input('Digite o ID escolhido: '))
                        for divida in dividas:
                            if id_escolha == divida['ID']:
                                print('ID encontrado...')
                                sleep(1)    
                                print(f'ID: {divida['ID']}\n\nNome da divida: {divida['Nome da Divida']}\nValor total: R${divida['Valor total']:.2f}\nQtd.Parcelas: {divida['Parcelas']}\nValor Parcelas: R${divida['Valor das parcelas']:.2f}\nVencimento:{divida['Vencimento']}\nTipo de Divida:{divida['Tipo']}\n')
                                escolha = int(input('Voltar [0]: '))
                                if escolha == 0:
                                    sleep(0.5)
                                    print('Voltando...\n')
                                    programa = False  
                                    break  
                                
                                
                        else:
                            print('Não encontrado...\n')
                            break
                    except ValueError:
                        print('Digite um valor valido!!\n')
                        sleep(0.5)
                        
                    
   
                
                
# FUNCÃO DE EDITAR DIVIDA
def editar_divida():
    print('-=-=-=-=-=-=-=-=-=- EDITOR DE DIVIDAS -=-=-=-=-=-=-=-=-=-=')
    if not dividas:
        print('Nenhuma divida encontrada\n\n')
        sleep(0.5)
        return
    else:
        id_escolha = int(input('Digite o ID escolhido: '))
        
        for divida in dividas:
            if divida['ID'] == id_escolha:
                print(f'Divida encontrada: {divida['Nome da Divida']}\n')
                sleep(0.5)
                escolha_menu = int(input('Oque deseja fazer??\n' 
                '[1] Alterar nome\n' 
                '[2] Alterar valor total\n' 
                '[3] Alterar quantidade de parcelas\n'
                '[4] Alterar valor das parcelas\n'
                '[5] Alterar vencimento\n'
                '[6] Alterar categoria\n\n\n'
                '[0] Voltar\n\n'
                'Escolha: '))
                if escolha_menu == 0:
                    print('Voltando...')
                    sleep(0.5)
                    break
                elif escolha_menu == 1:
                    print(f'Nome atual: {divida['Nome da Divida']}')
                    novo_nome = input('Digite o nome desejado: ')
                    sleep(1)
                    print('Nome alterado com sucesso !!\n')
                    divida['Nome da Divida'] = novo_nome
                elif escolha_menu == 2:
                    print(f'Valor total atual: R${divida['Valor total']:.2f}')
                    novo_valor = float(input('Digite o valor atual desejado: '))
                    sleep(1)
                    print('Valor atual alterado com sucesso !!\n')
                    divida['Valor total'] = novo_valor
                elif escolha_menu == 3:
                    print(f'Qtd de parcelas atuais: {divida['Parcelas']}')
                    nova_parcela = int(input('Digite a quantidade de parcelas desejada: '))
                    sleep(1)
                    print('Valor alterado com sucesso!!\n')
                    divida['Parcelas'] = nova_parcela
                elif escolha_menu == 4:
                    print(f'Valor da parcela atual: R${divida['Valor das parcelas']:.2f}')
                    novo_valor_parcela = float(input('Digite o valor das parcelas desejada: '))
                    sleep(1)
                    print('Valor alterado com sucesso!!\n')
                    divida['Valor das parcelas'] = novo_valor_parcela
                elif escolha_menu == 5:
                    print(f'Vencimento Atual: {divida['Vencimento']}')
                    novo_vencimento = input('Digite a nova data de vencimento: ')
                    sleep(1)
                    print('Data alterada com sucesso!!\n')
                    divida['Vencimento'] = novo_vencimento
                elif escolha_menu == 6:
                    print(f'Categoria atual: {divida['Tipo']}')
                    novo_tipo = input('Digite a categoria desejada: ')
                    sleep(1)
                    print('Categoria alterada com sucesso!!\n')
                    divida['Tipo'] = novo_tipo
                else:
                    print('Valor invalido, digite novamente!')
        
        else:
            print('ID não encontrado!!\n')  

#FUNÇÃO DE REMOVER DIVIDA        
def remover_divida():
    print('REMOVER DIVIDAS')
    sleep(0.5)
    
    if dividas:
        for divida in dividas:
            print(f'ID: {divida['ID']} -= -= -= -= -= Nome: {divida['Nome da Divida']}')
            sleep(0.5)

            

        id_escolha = int(input('Digite o ID escolhido: '))
        for divida in dividas:
            if divida['ID'] == id_escolha:    
                dividas.remove(divida)
                print(f'Divida {divida['Nome da Divida']} removida com sucesso!! ')
                sleep(1)
                break
        else:
            print('ID NAO ENCONTRADO!!\n\n')
            sleep(1)
    if not dividas:
        print('Nenhuma divida encontrada!')
        sleep(0.5)
        return             
    
#FUNÇÃO DE REGISTRAR PAGAMENTO
def registrar_pagamento():
    global saldo_usuario
    print('============ REGISTRAR PAGAMENTO ============')
    sleep(1)
    continuar = True
    while continuar:    
        
        try:    
            if dividas:            
                for divida in dividas:
                    print('=======================================')
                    sleep(0.3)
                    print(f'ID: {divida['ID']} || NOME: {divida['Nome da Divida']} || VALOR TOTAL: R${divida['Valor total']:.2f} ||')
                    sleep(0.5)
                    print(f'\nSeu Saldo: R${saldo_usuario:.2f} \n')
                    
                escolha_opcao = int(input('Oque deseja fazer?\n[0] Voltar ao menu\n[1] Registrar um pagamento\nEscolha:'))

                if escolha_opcao == 0:
                    print('Voltando...')
                    sleep(0.5)
                    continuar = False
                elif escolha_opcao == 1:

                    escolha = int(input('Escolha o id desejado: '))
                    for divida in dividas:
                        if divida['ID'] == escolha:
                            sleep(0.5)
                            print('ID encontrado...')
                            sleep(1)    
                            print(f'ID: {divida['ID']}\n\nNome da divida: {divida['Nome da Divida']}\nValor total: R${divida['Valor total']:.2f}\nQtd.Parcelas: {divida['Parcelas']}\nValor Parcelas: R${divida['Valor das parcelas']:.2f}\nVencimento:{divida['Vencimento']}\nTipo de Divida:{divida['Tipo']}\n') 
                            valor_pagar = float(input('\nDigite agora o valor que deseja pagar, 0 para voltar!: '))
                            if valor_pagar == 0:
                                continuar = False
                                sleep(0.5)
                                break
                            
                            elif valor_pagar <= divida['Valor total'] and saldo_usuario >= valor_pagar:
                                if valor_pagar < 0:
                                    print('Valores negativos não são validos!!')

                                else:
                                    saldo_usuario -= valor_pagar
                                    divida['Valor total'] -= valor_pagar
                                    sleep(0.5)
                                    print('Alterando divida...')
                                    sleep(0.5)
                                    print(f'Divida alterada com sucesso!, seu saldo agora é de R${saldo_usuario:.2f}')
                                    break
                            else:
                                print(f'Saldo insuficiente para realizar este pagamento, seu saldo é de R${saldo_usuario:.2f}')
                                sleep(0.5)
                    
                    else:
                        print('ID NAO ENCONTRADO')
                        sleep(0.5)
                    
            else:
                print('Nenhuma divida encontrada!')
                sleep(0.5)
                return
        except ValueError:
            print('Digite um valor valido!')

#. FLUXO PRINCIPAL

while True:

    opcao = mostrar_menu()

    if opcao == 1:
        cadastrar_divida()

    elif opcao == 2:
        consultar_divida()

    elif opcao == 3:
        editar_divida()
   
    elif opcao == 4:
        remover_divida()
   
    # PRÓXIMOS PASSOS:
    # [3] Criar função editar_divida(). CONCLUIDO
    # [4] Criar função remover_divida(). CONCLUIDO
    # [5] Criar função registrar_pagamento(). CONCLUIDO
    # [6] Criar função consultar_saldo().
    # [7] Criar função resumo_financeiro().
    # [8] Criar função sugestoes_financeiras().
    elif opcao == 5:
        registrar_pagamento()
    elif opcao == 0:
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida ou ainda não implementada!')
