# IDENTIFICAÇÃO:
# Nome: FELIPE KITAMOTO AMARAL
# Matrícula: 2022200987
# Programação I / Programação Funcional
# EP 1 - Coffee Machine
# UFES - Ciência da Computação 2022/2
# =================================================================================================

from os import system , name

def limpaTela():
    """Essa função limpa a tela do terminal."""
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def leValor(tipo, msg = ""):
    """Essa função lê, verifica e aprova (ou reprova) uma entrada baseada em seu tipo,
e retorna a sí própria caso seja reprovada."""
    RED = '\033[31m'
    RST     = '\033[00m'
    try:
        return tipo(input(msg))
    except:
        print(f"{RED}ERRO: Tipo inválido! Tente Novamente.{RST}")
        return leValor(tipo, msg)

def boasvindas():
    """Essa função exibe uma mensagem de boas vindas."""
    BLUE    = '\033[34m'
    GREEN   = "\033[1;32m"
    RST     = '\033[00m'
    print(f'{BLUE} ____    _____   __  __          __     __  ___   _   _   ____     ___  ')
    print(f'| __ )  | ____| |  \/  |         \ \   / / |_ _| | \ | | |  _ \   / _ \ ')
    print(f'|  _ \  |  _|   | |\/| |  _____   \ \ / /   | |  |  \| | | | | | | | | |')
    print(f'| |_) | | |___  | |  | | |_____|   \ V /    | |  | |\  | | |_| | | |_| |')
    print(f'|____/  |_____| |_|  |_|            \_/    |___| |_| \_| |____/   \___/ ')
    print(72*'=')
    print(f' {RST}')
    x = input(f'{GREEN}                  [Pressione ENTER para continuar]{RST}')
    limpaTela()

def maquina(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5):
    """Essa função exibe a tela principal da máquina de vendas e chama a função escolhas()."""
    RED     = '\033[31m'
    RST     = '\033[00m'
    if c<1 or p1<200 or p3<80 or p4<50 or p5<50 or p6<50:
        v1=f'{RED}INDISPONÍVEL{RST}'
    if c<1 or p1<250 or p2<50 or p3<30 or p7<10:
        v2=f'{RED}INDISPONÍVEL{RST}'
    if c<1 or p1<250 or p2<30 or p3<60 or p4<35 or p7<10:
        v3=f'{RED}INDISPONÍVEL{RST}'
    if c<1 or p1<200 or p8<70 or p9<30 or p7<20:
        v4=f'{RED}INDISPONÍVEL{RST}'
    if c<1 or p1<150 or p9<100 or p7<25:
        v5=f'{RED}INDISPONÍVEL{RST}'
    
    print(f"""+-------------------- BEBIDAS --------------------+
| 1 - Achocolatado.................. {v1} 
| 2 - Café com Leite................ {v2} 
| 3 - Cappuccino.................... {v3} 
| 4 - Chá Gelado.................... {v4} 
| 5 - Limonada...................... {v5} 
+-------------------- OUTROS ---------------------+
| 6 - Informações dos Produtos              
| 7 - Informações Internas                  
| 8 - Finalizar                             
+-------------------------------------------------+ """)
    escolhas(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)

def infProd(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5):
    """Essa função exibe o preço e a quantidade de ingredientes necessários para cada produto."""
    GREEN   = "\033[1;32m"
    RST     = '\033[00m'
    print("""+ ---------------------------- +
| ---> Achocolatado: R$2,00    |
| 200ml de Água                |
| 80ml de Leite em Pó          |
| 50g de Chocolate em Pó       |
| 50ml de Leite Condensado     |
| 50ml de Creme de Leite       |
+ ---------------------------- +
| ---> Café com Leite: R$2,50  |
| 250ml de Água                |
| 50g de Leite em Pó           |
| 30g de Café Solúvel          |
| 10g de Açúcar                |
+ ---------------------------- +
| ---> Cappuccino: R$6,00      |
| 250ml de Água                |
| 60g de Leite em Pó           |
| 30g de Café Solúvel          |
| 35g de Chocolate em Pó       |
| 10g de Açúcar                |
+ ---------------------------- +
| ---> Chá Gelado: R$5,00      |
| 200ml de Água                |
| 70ml de Chá Preto            |
| 30ml de Limão                |
| 20g de Açúcar                |
+ ---------------------------- +
| ---> Limonada: R$3,50        |
| 150ml de Água                |
| 100ml de Limão               |
| 25g de Açúcar                |
+ ---------------------------- +
""")
    retornar(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)

def retornar(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5):
    """Essa função pergunta se o usuário gostaria de voltar para a tela principal,
caso contrário o programa é finalizado."""
    RED     = '\033[31m'
    GREEN   = "\033[1;32m"
    RST     = '\033[00m'
    x = leValor(str,f'{GREEN}Deseja retornar à máquina? (S/N): {RST}')
    if x == 's' or x == 'S':
        limpaTela()
        return maquina(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    elif x == 'n' or x == 'N':
        limpaTela()
        infInt(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
        print(f'{GREEN}Processo Finalizado.{RST}\n')
        exit()
    else:
        print(f'{RED}ERRO! Você deve digitar uma das opções especificadas (S ou N). Tente Novamente.{RST}')
        retornar(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)

def infInt(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5):
    """Essa função exibe as informações internas da máquina, bem como seus ingredientes e seu faturamento."""
    print(f"""+ --------------------------- +
| Copos: {c}                   
| Água: {p1}ml                
| Café Solúvel: {p2}g          
| Leite em Pó: {p3}g           
| Chocolate em Pó: {p4}g       
| Leite Condensado: {p5}ml     
| Creme de Leite: {p6}ml       
| Açúcar: {p7}g                
| Chá Preto: {p8}g             
| Poupa de Limão: {p9}ml       
+ --------------------------- +
| Faturamento: R${fat:.2f}         
+ --------------------------- +
""")

def escolhas(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5):
    """Essa função determina o caminho do código com base na escolha do usuário,
as escolhas são baseadas nos valores da tela principal da máquina (a função maquina())."""
    RED     = '\033[31m'
    RST     = '\033[00m'
    BLUE    = '\033[34m'
    GREEN   = "\033[1;32m"
    valor = leValor(int,f'{GREEN}[Selecione o número do produto desejado] ===> {RST}')
    if valor<1 or valor>8:
        print(f'{RED}ERRO: Você deve digitar um valor correspondente à tabela!{RST}')
        return escolhas(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    elif valor==8:
        limpaTela()
        infInt(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
        print(f'{GREEN}Processo Finalizado.{RST}\n')
        exit()
    elif valor==1:
        if c<1 or p1<200 or p3<80 or p4<50 or p5<50 or p6<50:
            print(f'{RED}Desculpe, ingredientes insuficientes no momento, tente escolher outro produto.{RST}')
            return escolhas(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
        else:
            print(f'\nVocê escolheu: {BLUE}Achocolatado{RST} \nPreço: {BLUE}R$2,00{RST}\n')
            c-=1
            p1-=200
            p3-=80
            p4-=50
            p5-=50
            p6-=50
            fat+=2.00
            insDin(valor,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5,d1=0)
    elif valor==2:
        if c<1 or p1<250 or p2<50 or p3<30 or p7<10:
            print(f'{RED}Desculpe, ingredientes insuficientes no momento, tente escolher outro produto.{RST}')
            return escolhas(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
        else:
            print(f'\nVocê escolheu: {BLUE}Café com Leite{RST} \nPreço: {BLUE}R$2,50{RST}\n')
            c-=1
            p1-=250
            p2-=50
            p3-=30
            p7-=10
            fat+=2.50
            insDin(valor,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5,d1=0)
    elif valor==3:
        if c<1 or p1<250 or p2<30 or p3<60 or p4<35 or p7<10:
            print(f'{RED}Desculpe, ingredientes insuficientes no momento, tente escolher outro produto.{RST}')
            return escolhas(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
        else:
            print(f'\nVocê escolheu: {BLUE}Cappuccino{RST} \nPreço: {BLUE}R$6,00{RST}\n')
            c-=1
            p1-=250
            p2-=30
            p3-=60
            p4-=35
            p7-=10
            fat+=6.00
            insDin(valor,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5,d1=0)
    elif valor==4:
        if c<1 or p1<200 or p8<70 or p9<30 or p7<20:
            print(f'{RED}Desculpe, ingredientes insuficientes no momento, tente escolher outro produto.{RST}')
            return escolhas(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
        else:
            print(f'\nVocê escolheu: {BLUE}Chá Gelado{RST} \nPreço: {BLUE}R$5,00{RST}\n')
            c-=1
            p1-=200
            p8-=70
            p9-=30
            p7-=20
            fat+=5.00
            insDin(valor,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5,d1=0)
    elif valor==5:
        if c<1 or p1<150 or p9<100 or p7<25:
            print(f'{RED}Desculpe, ingredientes insuficientes no momento, tente escolher outro produto.{RST}')
            return escolhas(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
        else:
            print(f'\nVocê escolheu: {BLUE}Suco de Laranja{RST} \nPreço: {BLUE}R$3,50{RST}\n')
            c-=1
            p1-=150
            p9-=100
            p7-=25
            fat+=3.50
            insDin(valor,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5,d1=0)
    elif valor==6:
        infProd(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    elif valor==7:
        infInt(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
        retornar(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)

def insDin(valor,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5,d1=0):
    """Pede para que o usuário insira uma quantidade de dinheiro e exibe o troco para tal quantia."""
    BLUE    = '\033[34m'
    RED     = '\033[31m'
    GREEN   = "\033[1;32m"
    RST     = '\033[00m'
    if valor == 1:
        preco = 2.00
    if valor == 2:
        preco = 2.50
    if valor == 3:
        preco = 6.00
    if valor == 4:
        preco = 5.00
    if valor == 5:
        preco = 3.50
    d = leValor(float,f'{GREEN}Insira o dinheiro: R${RST}')
    """Variável em que será armazenada o valor das notas/moedas inseridas pelo usuário."""
    if d<0:
        print(f'{RED}ERRO! Valores negativos ou não numéricos não podem ser validados. Tente Novamente.{RST}')
        insDin(valor,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5,d1=0)
    else:
        d1+=d
        troco=d1-preco
        if d1>=preco:
            print(' ')
            print(f'Valor pago: {BLUE}R${d1:.02f}{RST}\nTroco: {BLUE}R${troco:.02f}{RST}')
            print(' ')
            PegTroc(preco,troco,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
            return d-preco
        else:
            return insDin(valor,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5,d1)

def PegTroc(preco,troco,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5):
    """Função que exibe cada nota/moeda devolvida ao usuário tendo em base
o valor pago e o troco necessário."""
    BLUE    = '\033[34m'
    GREEN   = "\033[1;32m"
    RST     = '\033[00m'
    if troco==0:
        print(f' \n{GREEN}Obrigado pela sua compra! Volte sempre!{RST}\n ')
        retornar(c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    if troco>=100:
        troco-=100
        print(f'Pegue o seu troco: {BLUE}R$100,00.{RST}')
        PegTroc(preco,troco,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)   
    if troco>=50 and troco<100:
        troco-=50
        print(f'Pegue o seu troco: {BLUE}R$50,00.{RST}')
        PegTroc(preco,troco,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    if troco>=20 and troco<50:
        troco-=20
        print(f'Pegue o seu troco: {BLUE}R$20,00.{RST}')
        PegTroc(preco,troco,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    if troco>=10 and troco<20:
        troco-=10
        print(f'Pegue o seu troco: {BLUE}R$10,00.{RST}')
        PegTroc(preco,troco,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    if troco>=5 and troco<10:
        troco-=5
        print(f'Pegue o seu troco: {BLUE}R$5,00.{RST}')
        PegTroc(preco,troco,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    if troco>=2 and troco<5:
        troco-=2
        print(f'Pegue o seu troco: {BLUE}R$2,00.{RST}')
        PegTroc(preco,troco,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    if troco>=1 and troco<2:
        troco-=1
        print(f'Pegue o seu troco: {BLUE}R$1,00.{RST}')
        PegTroc(preco,troco,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    if troco>=0.50 and troco<1:
        troco-=0.50
        print(f'Pegue o seu troco: {BLUE}R$0,50.{RST}')
        PegTroc(preco,troco,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    if troco>=0.25 and troco<0.50:
        troco-=0.25
        print(f'Pegue o seu troco: {BLUE}R$0,25.{RST}')
        PegTroc(preco,troco,c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    if round(troco, 2)>=round(0.10, 2) and round(troco, 2)<round(0.25, 2):
        troco-=round(0.10, 2)
        print(f'Pegue o seu troco: {BLUE}R$0,10.{RST}')
        PegTroc(preco, round(troco, 2),c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    if round(troco, 2)>=round(0.05, 2) and round(troco, 2)<round(0.10, 2):
        troco-=0.05
        print(f'Pegue o seu troco: {BLUE}R$0,05.{RST}')
        PegTroc(preco, round(troco, 2),c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)
    if round(troco, 2)>=round(0.01, 2) and round(troco, 2)<round(0.05, 2):
        troco-=0.01
        print(f'Pegue o seu troco: {BLUE}R$0,01.{RST}')
        PegTroc(preco, round(troco, 2),c,p1,p2,p3,p4,p5,p6,p7,p8,p9,fat,v1,v2,v3,v4,v5)

def main():
    """Função principal do código, que chama todas as demais e as executa."""
    limpaTela()
    boasvindas()
    maquina(10,2000,500,500,500,1000,1000,1000,500,1000,0.0,'R$2.00','R$2.50','R$6.00','R$5.00','R$3.50')

main()