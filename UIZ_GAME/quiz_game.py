print("Bem-vindo ao quiz!")

playing = input("Você quer jogar? (sim/não) ")

if playing != "sim":
    quit()

print("Maravilha! Vamos Jogar :)")

answer = input("Qual e o nome do filho de Deus nosso pai? ")
if answer == "Jesus":
    print("correto!")
else:
    print("errou!")