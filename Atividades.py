#-----------------------------------------------------------Questão 1-------------------------------------------------------

#Nome do mercado
print('+',49* '-', '+')
print('|','MERCADO ATACADÃO | NEDER PEREIRA DOS SANTOS FILHO','|')
print('+',49* '-', '+')

#Tabela dos produtos
print('*', 46*'-','*')
print('|','Código do produto','|', 'Preço   ','|' ,'Nome do produto','|')
print('|','      001        ', '|' ,'R$ 20,00','|','Arroz          ', '|')
print('*', 46*'-','*')

#Solicitando dados ao usuário
produto = (input('Escolha o código do produto que deseja efetuar a compra.\nR:'))
quantidade = int(input('Qual a quantidade que deseja levar desse produto?\nR:'))

while(produto == '001'): #Verificando qual produto foi escolhido
    valor = 20.00  
    if(quantidade <= 9): 
        print('Valor total | sem desconto: R${:.2f}'.format(valor * quantidade))
        print('Valor Total | com desconto: R${:.2f}'.format(valor * quantidade))
        print('O desconto efetuado foi de: 0%')
        break
    elif(quantidade >= 10 and quantidade <= 99): 
        valor_qt = valor * quantidade 
        desconto = valor_qt * 5 / 100 
        valor_final = valor_qt - desconto 
        print('Valor total | sem desconto: R${:.2f}'.format(valor_qt))
        print('Valor total | com desconto: R${:.2f}'.format(valor_final))
        print('O desconto efetuado foi de: 5%')
        break
    elif(quantidade >= 100 and quantidade <= 999): 
        valor_qt = valor * quantidade
        desconto = valor_qt * 10 / 100 
        valor_final = valor_qt - desconto
        print('Valor total | sem desconto: R${:.2f}'.format(valor_qt))
        print('Valor total | com desconto: R${:.2f}'.format(valor_final))
        print('O desconto efetuado foi de: 10%')
        break
    elif(quantidade >= 1000):
        valor_qt = valor * quantidade
        desconto = valor_qt * 15 / 100
        valor_final = valor_qt - desconto
        print('Valor total | sem desconto: R${:.2f}'.format(valor_qt))
        print('Valor total | com desconto: R${:.2f}'.format(valor_final))
        print('O desconto efetuado foi de: 15%')
        break


    #------------------------------------------------------Fim Questão 1------------------------------------------------------

    #------------------------------------------------------Questão 2----------------------------------------------------------


    #Tabela de produtos
print('+', 42 * '-',13* '-', '+')
print('|','Bem Vindo a Lanchonete do Neder Pereira dos Santos filho', '|')
print('+', 42 * '-', '+',11* '-', '+')
print('|','Código', '|', 'Descrição            ', '|', 'Valor(R$)', '|')
print('|', '100   ', '|', 'Cachorro-Quente      ', '|', '9,00     ', '|')
print('|', '101   ', '|', 'Cachorro-Quente Duplo', '|', '11,00    ', '|')
print('|', '102   ', '|', 'X-Egg                ', '|', '12,00    ','|')
print('|', '103   ', '|', 'X-Salada             ', '|', '13,00    ', '|')
print('|', '104   ', '|', 'X-Bacon              ', '|', '14,00    ', '|')
print('|', '105   ', '|', 'X-Tudo               ', '|', '17,00    ', '|')
print('|', '200   ', '|', 'Refrigerante Lata    ', '|', '5,00     ', '|')
print('|', '201   ', '|', 'Chá Gelado           ', '|', '13,00    ', '|')
print('+', 42 * '-', '+')

#Variavel para armazenar o valor da compra
final = 0

while True:
     produto = input('Escolha seu pedido.\nR:') 

     if(produto == '100'): 
         valor = 9.00 
         final += valor 
     elif(produto == '200'): 
         valor = 5.00
         final += valor
     else:
        print('Opção Invalida!') 
        continue
     print('Deseja escolhe mais algum item?') 
     print('Sim - 1')
     print('Não - 0')
     escolha = int(input('R:')) 

     if(escolha == 1):
         continue
     elif(escolha == 0):
         print('Total a ser pago: R${:.2f}'.format(final)) 
         break
     else:
         print('Opção invalida!')
         break

#-----------------------------------------------------------fim questão 2---------------------------------------------------------

#------------------------------------------------------------Questão 3------------------------------------------------------------


#Total = dimensoes * peso * rota
print('+', 53*'-','+')
print('|','Empresa de logística - Neder pereira dos santos filho','|')
print('+', 53*'-','+')

final_dimensoes = 0 
final_rota = 0 
final_peso = 0 

#função com saida do valor da dimensão
def dimensoesObjeto():
 global final_dimensoes 
 while True:
   try:
    altura = int(input('Digite a altura em cm.\nR:'))
    comprimento = int(input('Digite o comprimento em cm.\nR:'))
    largura = int(input('Digite a largura em cm.\nR:'))

    #calculo
    valor = altura * comprimento * largura

    #logica
    if(valor < 1000):
     final_dimensoes = 10
     return final_dimensoes
    elif(valor <= 1000 or valor < 10000):
     final_dimensoes = 20
     return final_dimensoes
    elif(valor <= 10000 or valor < 30000):
     final_dimensoes = 30
     return final_dimensoes
    elif(valor <= 30000 or valor < 100000):
     final_dimensoes = 50
     return final_dimensoes
    elif(valor >= 100000):
     print('O valor do objeto:', valor)
     print('Não é aceito')
   except ValueError:
       print('Você digitou alguma dimensão do objeto com valor não númerico')
       print('Por favor digite as dimensoes desejadas novamente..')

#Função para verificar o peso
def pesoObjeto():
 global final_peso
 while True:

  try:
   peso = int(input('Qual o peso do objeto em kg?\nR:'))

 #logica
   if(peso <= 0.1):
    final_peso = 1
    return final_peso
   elif(peso < 0.1 or peso <= 1):
    final_peso = 1.5
    return final_peso
   elif(peso < 1 or peso <= 10):
    final_peso = 2
    return final_peso
   elif(peso < 10 or peso <= 30):
    final_peso = 3
    return final_peso
   elif(peso > 30):
    print('Não é aceitamos esse peso!')
  except ValueError:
   print('Você digitou um peso com valor não númerico')

#Função para verificar rota
def rotaObjeto():

  print('Rota:')
  print('RS - De Rio de Janeiro até São paulo')
  print('SR - De São Paulo até Rio de Janeiro')
  print('BS - De Brasília até São paulo')
  print('SB - De São paulo até Brasília')
  print('BR - De Brasília até Rio de Janeiro')
  print('RB - Rio de Janeiro até Brasília')
  print( 34 *'-')

  while True:
   global final_rota
   rota = input('Qual rota deseja? Escolha a sigla.\n R:')

   if(rota == 'RS' or rota == 'SR'):
    final_rota = 1
    return final_rota
   elif(rota == 'BS' or rota == 'SB'):
    final_rota = 1.2
    return final_rota
   elif(rota == 'BR' or rota == 'RB'):
    final_rota = 1.5
    return final_rota
   else:
    print('Você digitou uma rota que não existe!')
    print('Por favor entre com a rota desejada novamente..')


#Executando o programa
dimensoesObjeto()
pesoObjeto()
rotaObjeto()

# Valor final
valor_final = final_dimensoes * final_peso * final_rota
print('Total a pagar(R$): {:.2f}'.format(valor_final))

#----------------------------------------------------------- fim questão 3 -------------------------------------------------------


#------------------------------------------------------------Questão 4------------------------------------------------------------


# Apresentação
print(82 *'-')
print('Bem vindo ao Controle de estoque da Bicicletaria do Neder Pereira dos Santos Filho')
print(82 *'-')

# variavel para armanezar os dados
listaEstoque = []

# função cadastrar
def cadastrarPeca(id):
  print('Cadastrar Item:')
  print('O código da peça cadastrada vai ser: {}'.format(id))
  nome = input('Digite o nome da peça: \n')
  fabricante = input('Digite o nome do fabricante: \n')
  valor_peca = int(input('Digite o valor da peça: \n'))

  estoque = {'id' : id, 'nome' : nome , 'fabricante' : fabricante , 'Valor' : valor_peca}
  listaEstoque.append(estoque.copy()) #salvando os dados no estoque

# função consultar
def consultarPeca():
    while True:
     try:
       print('Consultar Item:')
       print('1 - Consultar todas as peças.')
       print('2 - Consultar Peças por código.')
       print('3 - Consultar Peças por fabricante.')
       print('4 - voltar')
       opConsultar = int(input('Escolha a opção desejada:\nR:'))

       if(opConsultar == 1):
           print('Opção escolhida: Consultar todos')
           for peca in listaEstoque:
               for key, value in peca.items(): #Realizar a consulta
                   print('{} : {}' .format(key, value))
       elif(opConsultar == 2):
           print('Opção escolhida: Consultar Peças por código')
           dados = int(input('Digite o código desejado:\nR:'))
           for peca in listaEstoque:
            if(peca['id'] == dados): # Realizando a consulta do ID
                for key, value in peca.items():
                    print('{} : {}'.format(key, value))
       elif(opConsultar == 3):
           print('Opção escolhida: Consultar peças por fabricante')
           dados = input('Digite o fabricante desejado:\nR:')
           for peca in listaEstoque:
               if (peca['fabricante'] == dados):  #Realizando a consulta do fabricante
                   for key, value in peca.items():
                       print('{} : {}'.format(key, value))

       elif(opConsultar == 4):
           print('Opção escolhida: Voltar')
           return
       else:
           print('Essa opção não existe!')
           continue
     except ValueError:
       print('Você digitou um valor inteiro..Erro!')

# função remover
def removerPeca():
    print('Remover peça:')
    opremover = int(input('Digite o código da peça que deseja remover:\nR:'))
    for peca in listaEstoque:
        if (peca['id'] == opremover):
          listaEstoque.remove(peca) #removendo a peça

# Iniciando o programa
identificar = 0 # contador
while True:
     try:
         print('1 | Cadastrar Peça')
         print('2 | Consultar Peça')
         print('3 | Remover Peça')
         print('4 | Sair')

         opcao = int(input('Digite a opção desejada:\nR:'))

         if(opcao == 1):
           identificar = identificar + 1
           cadastrarPeca(identificar)
         elif(opcao == 2):
           consultarPeca()
         elif(opcao == 3):
           removerPeca()
         elif(opcao == 4):
           break
     except ValueError:
          print('Você digitou uma opção errada!')


#-------------------------------------------------------fim questão 4------------------------------------------------------------
