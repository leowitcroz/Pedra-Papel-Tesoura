import random
user_wins = 0
computer_wins = 0
opcoes = ["pedra","papel","tesoura"]
print("Bem-vindo!!")
print("-" *12)
while True:
    user_input = input("Digite pedra/papel/tesoura ou Q para sair: ").lower()
    if user_input == "q":
        break
    
    if user_input not in opcoes:
        continue
    print("-" *12)

    random_option= random.choice(opcoes)
    # pedra: 0, papel: 1, scissors: 2

    computer_pick = random_option
    print("Computador escolheu", computer_pick + ".")
    
    if user_input == "pedra" and computer_pick == "tesoura":
        print("Voce ganhou")
        user_wins += 1
        print("-" *12)

    elif user_input == "papel" and computer_pick == "pedra":
        print("Voce ganhou")
        user_wins += 1
        print("-" *12)
      

    elif user_input == "tesoura" and computer_pick == "papel":
        print("Voce ganhou")
        user_wins += 1
        print("-" *12)

    else:
        print("Voce perdeu! ")
        computer_wins += 1;
        print("-" *12)

print("voce ganhou",user_wins)
print("-" *12)
print("adversario ganhou",computer_wins)
print("-" *12)
   

print("Adeus!!")









        




