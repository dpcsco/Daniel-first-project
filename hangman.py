echo "# Daniel-first-project" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/dpcsco/Daniel-first-project.git
git push -u origin main

class Hangman:
    def __init__(self, user_word) -> None:
        self.user_word = user_word
    
    global char_list
    global output_list
    
    char_list = []
    output_list = []

    global game_state
    global game_state_one
    global game_state_two
    global game_state_three
    global game_state_four
    global game_state_five
    global game_state_six

    game_state = (f"______\n"
            "|    |\n"
            "|\n"
            "|\n"  
            "|\n" 
            "|\n"
            "|\n"
            "|________|\n\n")

    game_state_one = (f"______\n"
            "|    |\n"
            "|    O\n"
            "|\n"  
            "|\n" 
            "|\n"
            "|\n"
            "|________|\n\n")

    game_state_two = (f"______\n"
            "|    |\n"
            "|    O\n"
            "|    |\n"  
            "|\n" 
            "|\n"
            "|\n"
            "|________|\n\n")

    game_state_three = (f"______\n"
            "|    |\n"
            "|    O\n"
            "|   /|\n"  
            "|\n" 
            "|\n"
            "|\n"
            "|________|\n\n")

    game_state_four = (f"______\n"
            "|    |\n"
            "|    O\n"
            "|   /|\ \n"  
            "|\n" 
            "|\n"
            "|\n"
            "|________|\n\n")

    game_state_five = (f"______\n"
            "|    |\n"
            "|    O\n"
            "|   /|\ \n"  
            "|   / \n" 
            "|\n"
            "|\n"
            "|________|\n\n")

    game_state_six = (f"______\n"
            "|    |\n"
            "|    O\n"
            "|   /|\ \n"  
            "|   / \ \n" 
            "|\n"
            "|\n"
            "|________|\n\n")


    def welcome_message(self):
        global game_state
        global output_list
        global char_list
        for x in range(25):
            print("")
        print("Here is your starting game board. Have Fun!")
        for character in self.user_word:
            if character == ' ':
                game_state += '  '
                output_list.append('  ')
            if character != ' ':
                game_state += '_ '
                char_list.append(character.lower())
                output_list.append('_ ')
        print(game_state)
        

    def check_guess(self):
        global output_list
        global char_list
        global game_state_one
        global game_state_two
        global game_state_three
        global game_state_four
        global game_state_five
        global game_state_six
        miss_count = 0
        while (miss_count <= 5):
            print("\nEnter your guess here:")
            user_guess = input()
            user_guess = user_guess.lower()
            if (user_guess == "exit"):
                exit()
            if user_guess not in char_list:
                miss_count += 1

            if user_guess in char_list:
                indices = [index for index, value in enumerate(char_list) if value == user_guess]
                for i in range(len(indices)):
                    output_list[indices[i]] = user_guess
                if '_ ' not in output_list:
                    print("That is correct! You Win!")
                    exit()

            if miss_count == 0:
                print('')
            if miss_count == 1:
                print(game_state_one)
            if miss_count == 2:
                print(game_state_two)
            if miss_count == 3:
                print(game_state_three)
            if miss_count == 4:
                print(game_state_four)
            if miss_count == 5:
                print(game_state_five)
            if miss_count == 6:
                print(game_state_six)
                print("Game Over. Better luck next time!")

            for char in output_list:
                    print(char, end="")


def main():
    user_word = input("Welcome to Hangman! Choose your word.\n")
    hang_game = Hangman(user_word)
    hang_game.welcome_message()
    hang_game.check_guess()

if __name__ == "__main__":
    main()
