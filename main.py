import random

viz = {
    0: '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

    1: '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

    2: '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''', }

moves = ['R', 'P', 'S']
m_text = {
    'R': 'Rock',
    'P': 'Paper',
    'S': 'Scissors'
}
game = True

while game:
    try:
        user = moves.index(
            input("What do you choose? Type R for Rock, P for Paper, S for Scissors\n").upper())
    except ValueError:
        print("invalid choice!")
    else:
        computer = random.randint(0, len(moves)-1)
        user_choice = moves[user]
        com_choice = moves[computer]

        print(f"{viz[user]} vs {viz[computer]}")
        print(
            f"Player ({m_text[user_choice]}) : Computer ({m_text[com_choice]})")

        if user_choice == com_choice:
            print("Draw")
        else:
            if (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
                print("You win!")
            else:
                print("You lose!!!")

            game = False
