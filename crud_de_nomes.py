escolha = 1

while escolha > 0:
    print ("Lista de Opções\n")
    print('1 - Inserir pessoa na Lista')
    print('2 - Listar pessoas cadastradas')
    print('3 - Pesquisar pelo nome de uma pessoa')
    print('4 - Ordenar a lista por ordem alfabética')
    print('5 - Atualizar nome')
    print('6 - Deletar nome da lista')
    print('7 - Sair do programa')

    opcoes = int(input('\nEscolha a sala desejada (1 a 7):\n'))
    
    match opcoes:
        case 1:
                nomes_lista = []
                while True:
                    try:    
                        novo_nome = input('Informe o novo nome a ser inserido na lista: ')
                        if novo_nome !='':
                           nomes_lista.append(novo_nome)
                           print(f'{novo_nome} inserido com sucesso.')
                           continue
                        else: 
                            break
                    except:
                        print('Não foi possível inserir o nome.')
        case 2:
            for nome in nomes_lista:
                print(nome)
        case 3:
            nome = input('Informe o nome que deseja encontrar: ')
            # busca o nome desejado
            if nome in nomes_lista:
                print(nome)
            else:
                print(f'{nome} não encontrado.')
        case 4:
            nomes_lista.sort()        
            # lista ordenada...
            print ('Lista ordenada:')
            for nome in nomes_lista:
                print(nome)
        case 7:
            escolha = 0
            break








