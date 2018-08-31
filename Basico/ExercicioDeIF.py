#Pergunte a velocidade de um carro, supondo um valor inteiro. caso ultrapasse 110 km/h
#exiba uma mensagem dizendo que o usuario foi multado. neste caso, exiba o valor da multa
#, cobrando R$ 5,00 por km acima de 110.

velocity = int(input("How fast was it? "))

if velocity>110:
	print "you qere fined\nfind:R$:%d "%((velocity-110)*5)
else:
	print"You not Find!! :)"