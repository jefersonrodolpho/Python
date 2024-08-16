
 ####    #    #     #### #   # #     ###       ##### ##   ##  ####
#       # #   #    #     #   # #    #   # ____   #   # # # # #
#      #####  #    #     #   # #    #   #        #   #  #  # #
 #### #     # ####  ####  ###  ####  ###       ##### #     #  ####

## Para realizar o cálculo do IMC dividimos o peso em quilogramas (Kg) pela altura (em metros) ao quadrado.
## O resultado gerado deve ser comparado aos valores da tabela IMC abaixo, para definir se está abaixo, no peso ideal ou acima do peso, cada classificação apresentará o estado atual da pessoa.

### TABELA IMC ###
# IMC 	        Classificação
# < 16 	        Magreza grave
# 16 a < 17 	Magreza moderada
# 17 a < 18,5 	Magreza leve
# 18,5 a < 25 	Saudável
# 25 a < 30 	Sobrepeso
# 30 a < 35 	Obesidade Grau I
# 35 a < 40 	Obesidade Grau II (severa)
# ≥ 40 	        Obesidade Grau III (mórbida)


altura = float(input(f"\nDigite sua altura em metros: "))
peso = float(input(f"\nDigite seu peso em Kg: "))
 
imc = peso / altura**2
 
print(f"\nSeu IMC é: %.2f" % imc)
 
if imc < 16:
	print(f"\nMagreza grave")
	print(f"\nOH My God, corre pra Nutricionista URGENTE, você tem que começar a comer imediatamente!!!\n")
elif imc < 17:
	print(f"\nMagreza moderada")
	print(f"\nTá liberado Pizza todo fim de semana, pode comer à vontade, você precisa ganhar peso!!!\n")
elif imc < 18.5:
	print(f"\nMagreza leve")
	print(f"\nPara de comer só salada e começa a comer carne, lazanha, macarronada, pães e tudo o que você gosta, mas com moderação para não engordar muito\n")
elif imc < 25:
	print(f"\nSaudável")
	print(f"\nCongratulations!!! você está se alimentando de forma saudável e correta!\n")
elif imc < 30:
	print(f"\nSobrepeso")
	print(f"\nUma caminhada e andar de biscicleta faz bem, porque não começa a fazer exercícios\n")
elif imc < 35:
	print(f"\nObesidade Grau I")
	print(f"\nJá te chamaram de gordinho(a)? é desagradável né! então bora pra academina malhar esse corpo!\n")
elif imc < 40:
	print(f"\nObesidade Grau II (severa)")
	print(f"\nPara de comer chocolate e procura uma Nutricionista agora!!!\n")
else:
	print(f"\nObesidade Grau III (mórbida)")
	print(f"\nOH My God, tenta se inscrever no programa Kilos Mortais do Dr.Younan Nowzaradan, você precisa urgente!!!\n")
 