import random
import os

def forca():
    lets=[]
    er=0
    palavra = sort_palavra()
    pal=['_']*(len(palavra)-1)
    exibe(lets,pal)
# Realiza a busca da letra na palavra
    while True:
        letra = ent_dados()
        lets.append(letra)
        for i in range(0,len(palavra)-1):
            if palavra[i]==letra:
                pal[i]=letra
# Verifica se a letra está errada
        if letra not in palavra:
            er+=1

        exibe(lets,pal,er)
# Verifica se errou todas as letras
        if er>7:
            print('Fim de jogo você perdeu!!!!!')
            print('A palavra era '+palavra)
            break
# Verifica se acertou a palavra
        fim=0
        for k in pal:
            if k=='_':
                fim+=1
        if fim==0:
            print('Parabens você descobriu a palavra!!!!!')
            break
# Sorteia a palavra do arquivo
def sort_palavra():
    arqui = open('list_forca.txt')
    list_pal = arqui.readlines()
    random.shuffle(list_pal)
    return list_pal[0]

# Realiza a verificação e entrada de dados
def ent_dados():
    l = input('Informe uma letra')
    while l.isnumeric() or len(l)>1 :
        l = input('Dado inválido, informe uma letra')
    return l

# Realiza a exibição e logica do boneco da forca
def exibe(letras=[],palavra=[],erros=0):
    a=''
    b=''
    c=''
    d=''
    e=''
    f=''
    g=''
    h=''
    if erros>0:a='O'
    if erros>1:b='/'
    if erros>2:c='|'
    if erros>3:d='\\'
    if erros>4:e='|'
    if erros>5:f='/'
    if erros>6:g='|'
    if erros>7:h='\\'

    os.system('cls')
    print('letras usadas')
    print(letras)
    print('   ____')
    print('  |    |')
    print('  |    '+a)
    print('  |  '+b,c,d)
    print('       '+e)
    print('     '+f,g,h)
    print('           ')
    #print(palavra.center(10,' '))
    for n in range(0,len(palavra)):
        print(palavra[n],end=' ')
    print('          ')
    print('          ')

forca()
