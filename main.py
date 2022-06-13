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

moves = {
    'R': 'Rock',
    'P': 'Paper',
    'S': 'Scissors'
}

playing = True

while playing:
    user = input(
        "What do you choose? Type R for Rock, P for Paper, S for Scissors: ").upper()
    if user not in moves.keys():
        print("invalid choice!")
    else:
        computer = random.choice(list(moves.keys()))

        print(f"{viz[user]} vs {viz[computer]}")
        print(
            f"Player ({moves[user]}) : Computer ({moves[computer]})")

        if user == computer:
            print("Draw")
        else:
            if (user == 'R' and computer == 'S') or (user == 'P' and computer == 'R') or (user == 'S' and computer == 'P'):
                print("You win!")
            else:
                print("You lose!!!")

            playing = False
