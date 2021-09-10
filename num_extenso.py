# Escreve por extenso
def extenso():
    num = ent_dados()
# Verifica se o numero inicia com zero
    if len(num)==3 and num[0]=='0':
        num=num[1:3]
    if len(num)==2 and num[0]=='0':
        num=num[1:2]
# Realiza a separação das unidades dezenas e centenas
    if len(num)==1:
        exibe(unidade(num[0]))  #chama a função de unidades retornando a string com nome

    elif len(num)==2:
        exibe(numdezena(num))   #chama a função dezena  retornando o valor por extenso

    elif len(num)==3:
        if num=='100':
            exibe('Cem')
        else:
            strg1 = numdezena(num[1:3])
            strg2 = cent(num[0])
            exibe(strg2+' e '+strg1)
    else:
        print('informe um numero entre 0 e 999')
        extenso()

def numdezena(num):
    n=int(num)
    if n<20:
        return(casadez(n))
    else:
        if num[1]=='0':
            return(dezena(num[0]))

        else:
            n1 = unidade(num[1])
            n2 = dezena(num[0])
            return(n2+' e '+n1)

# Realiza a entrada e validação dos dados
def ent_dados():
    num = input('digite um numero')
    while num.isalpha():
        print('digite um numero valido entre 0 e 999')
        num = input('digite um numero')
    return num

def exibe(nome):
    print('-'*len(nome))
    print(nome)
    print('-'*len(nome))

# Dicionario de numeros por extenso
def unidade(nu):
    nu = int(nu)
    if nu==0:return 'Zero'
    elif nu==1: return 'Um'
    elif nu==2: return 'Dois'
    elif nu==3: return 'Tres'
    elif nu==4: return 'Quatro'
    elif nu==5: return 'Cinco'
    elif nu==6: return 'Seis'
    elif nu==7: return 'Sete'
    elif nu==8: return 'Oito'
    else: return 'Nove'

def dezena(nu):
    nu = int(nu)
    if nu==2: return 'Vinte'
    elif nu==3: return 'Trinta'
    elif nu==4: return 'Quarenta'
    elif nu==5: return 'Cinquenta'
    elif nu==6: return 'Sessenta'
    elif nu==7: return 'Setenta'
    elif nu==8: return 'Oitenta'
    else: return 'Noventa'

def cent(nu):
    nu = int(nu)
    if nu==1: return 'Cento'
    elif nu==2: return 'Duzentos'
    elif nu==3: return 'Trezentos'
    elif nu==4: return 'Quatrocentos'
    elif nu==5: return 'Quinhentos'
    elif nu==6: return 'Seiscentos'
    elif nu==7: return 'Setecentos'
    elif nu==8: return 'Oitocentos'
    elif nu==9: return 'Novecentos'
    else: return ''

def casadez(nu):
    nu = int(nu)
    if nu==10: return 'Dez'
    elif nu==11: return 'Onze'
    elif nu==12: return 'Doze'
    elif nu==13: return 'Treze'
    elif nu==14: return 'Quatorze'
    elif nu==15: return 'Quinze'
    elif nu==16: return 'Dezesseis'
    elif nu==17: return 'Dezessete'
    elif nu==18: return 'Dezoito'
    else: return 'Dezenove'

extenso()
