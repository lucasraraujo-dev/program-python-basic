nome  = input ('Digite o primeiro nome:')
if nome == '' :
  print('Digite um  nome' )
  nome  = input ('Digite o primeiro nome:')
else:
    print('Seu nome é', nome)

if nome == nome: 
 print('Seja bem vindo', nome)



 sobre_nome = input ('digite seu sobrenome:')
 if sobre_nome == '' :
    print('Digite seu sobrenome')
    sobre_nome = input ('digite seu sobrenome:')
 if sobre_nome == sobre_nome:
  print('Este, é seu sobrenome ?', sobre_nome)



resposta = input('seu nome completo é '+ nome + sobre_nome +'correto ? 1: sim , 0: não >> ')
if resposta == '1': 
    print('Ok,Vamos continuar')
elif resposta == '0':
    print('Digite o nome novamente')    
else:
    print('Resposta incorreta')
   
    