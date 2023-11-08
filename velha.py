tabela = [
    [0,0,0], 
    [0,0,0],
    [0,0,0]
]


while True:

   
    print("Jogador 1")
    linha_usuario1 =input("qual é sua linha: ")
    print(linha_usuario1)
    coluna_usuario1 =input("qual é sua coluna: ")
    print(coluna_usuario1)
    linha_usuario1 = int(linha_usuario1)
    coluna_usuario1 = int(coluna_usuario1)
    tabela[linha_usuario1][coluna_usuario1]=11   
    print(tabela)

    
    print("Jogador 2")
    linha_usuario2 =input("qual é sua linha: ")
    print(linha_usuario2)
    coluna_usuario2 =input("qual é sua coluna: ")
    print(coluna_usuario2)
    linha_usuario2 = int(linha_usuario2)
    coluna_usuario2 = int(coluna_usuario2)

    tabela[linha_usuario2][coluna_usuario2]=7
    print(tabela)

def ganhador(tabela):
    #horizontal
    if tabela[1][1][1] == '1' and tabela[0][0][0] == '1' and tabela[0][0][0] == '1' or tabela[0][0][0] == '1' and tabela[1][1][1] == '1' and tabela[0][0][0] == '1' or tabela[0][0][0] == '1' and tabela[0][0][0] == '1' and tabela[1][1][1] == '1':
        print('O jogador 1 venceu')
#vertical
    elif tabela[1][0][0] == '1' and tabela[1][0][0] == '1' and tabela[1][0][0] == '1' or tabela[0][1][0] == '1' and tabela[0][1][0] == '1' and tabela[0][1][0] == '1' or tabela[0][0][1] == '1' and tabela[0][0][1] == '1' and tabela[0][0][1] == '1':
        print('O jogador 1 venceu')
#diagonal
    elif tabela[1][0][0] == '1' and tabela[0][1][0] == '1' and tabela[0][0][1] == '1' or tabela[0][0][1] == '1' and tabela[0][1][0] == '1' and tabela[1][0][0] == '1':
        print('O jogador 1 venceu')
#horizontal
    if tabela[2][2][2] == '2' and tabela[0][0][0] == '2' and tabela[0][0][0] == '2' or tabela[0][0][0] == '2' and tabela[2][2][2] == '2' and tabela[0][0][0] == '2' or tabela[0][0][0] == '2' and tabela[0][0][0] == '2' and tabela[2][2][2] == '2':
        print('O jogador 2 venceu')
#vertical
    elif tabela[2][0][0] == '2' and tabela[2][0][0] == '2' and tabela[2][0][0] == '2' or tabela[0][2][0] == '2' and tabela[0][2][0] == '2' and tabela[0][2][0] == '2' or tabela[0][0][2] == '2' and tabela[0][0][2] == '2' and tabela[0][0][2] == '2':
        print('O jogador 2 venceu')
#diagonal
    elif tabela[2][0][0] == '2' and tabela[0][2][0] == '2' and tabela[0][0][2] == '2' or tabela[0][0][2] == '2' and tabela[0][2][0] == '2' and tabela[2][0][0] == '2':
        print('O jogador 2 venceu')
    else:
        return False
        
           
           
           
   
            

        

