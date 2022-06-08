import random

viz = {
    'R': '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

    'P': '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

    'S': '''
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
    user = input(
        "What do you choose? Type R for Rock, P for Paper, S for Scissors\n").upper()
    if user not in moves:
        print("invalid choice!")
    else:
        computer = random.choice(moves)

        print(f"{viz[user]} vs {viz[computer]}")
        print(
            f"Player ({m_text[user]}) : Computer ({m_text[computer]})")

        if user == computer:
            print("Draw")
        else:
            if (user == 'R' and computer == 'S') or (user == 'P' and computer == 'R') or (user == 'S' and computer == 'P'):
                print("You win!")
            else:
                print("You lose!!!")

            game = False
