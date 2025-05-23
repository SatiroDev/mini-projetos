
def adicionar_categorias(lista):
    esc = 's'
    while esc != 'n':
        verificacao = False
        nome_escolha_categoria = input('Nome da categoria: ').strip()
        if nome_escolha_categoria == '':
            print('Você precisa digitar algo!')
            continue
        if nome_escolha_categoria not in lista:
            veri = True
            for categoria in lista:
                if nome_escolha_categoria.lower() == categoria[0].lower():
                    veri = False
                    continue
                else:
                    veri = True
            if veri == True:
                verificacao = True
                lista.append([nome_escolha_categoria, []])
                print(f'Categoria "{nome_escolha_categoria}" adicionada com sucesso!')
        if verificacao == False:
            print('Categoria já esta adicionada!')
        esc = input('Deseja adicionar mais categorias? [s/n] ').lower()

def adicionar_tarefas(lista):
    verificacao = False
    if not lista:
        print('Nenhuma categoria adicionada! Você precisa adicionar pelo menos uma!')
    else:
        for categoria in lista:
            print(f'Nome da categoria: {categoria[0]}')
        nome_escolha_categoria = input('Nome da categoria que deseja adicionar : ').lower()
        for categoria in lista:
            if nome_escolha_categoria == categoria[0].lower():
                verificacao = True
                escolha = 's'
                while escolha != 'n':
                    tarefa = input('Digite uma tarefa: ').strip()
                    if tarefa in categoria[1]:
                        print(f'Tarefa "{tarefa}" já está adicionada!')
                    elif tarefa != '':
                        categoria[1].append(tarefa)
                    else:
                        print('Você precisa digitar algo!')
                    escolha = input('Deseja adicionar mais tarefas? [s/n] ').lower()
        if verificacao == False:
            print(f'Categoria "{nome_escolha_categoria}" não encontrada!')
            opcao = input('Deseja adicionar ela? [s/n] ').lower()
            if opcao == 's':
                nome_categoria = input('Digito o nome da categoria que quer adicionar: ')
                lista.append([nome_categoria, []])
                print(f'Categoria "{nome_categoria}" adicionada com sucesso!')
                adicionar_tarefas()
  
def exibir_tarefas(lista):
    verificacao = False
    if not lista:
        print('Nenhuma categoria adicionada! Você precisa adicionar pelo menos uma!')
    else: 
        contagem = 0
        for categoria in lista:
            verificacao = True
            if contagem == 0: 
                print('Categorias e tarefas adicionadas: ')
                contagem += 1
            print(f'Nome da categoria: {categoria[0]}')
            print('Tarefas: ')
            cont = 1
            if categoria[1] == []:
                print('Nenhuma tarefa adicionada')
            else:
                for tarefas in categoria[1]:
                    print(f'{cont}. {tarefas}')
                    cont += 1
            print()
    if verificacao == False:
        print('Nenhuma tarefa adicionada!')

