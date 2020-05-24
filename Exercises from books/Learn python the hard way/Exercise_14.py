#* Prompting and passing

from sys import argv
import re

script, username = argv
clean_script = re.sub('[.py]', '',script)
prompt="-->"

def prompts_passing_game():    
    while True:
        print(f"Hi {username} how you doing?.\nI'm the {clean_script} script")
        print("I'm going to ask you some questions, is it okay? answer in 'y' or 'n" )
        permission =input(prompt)

        if (permission == 'y' or 'yes'):
            pass
        else:
            print("Okay that's fine comeback once you are ready.")
            print(f"{clean_script} signing off bye 👋")

            return False
            
        print(f"Do you like me {username}")
        likes = input(prompt)

        print("What do you do for living ?")
        occupation = input(prompt)

        print(f"What's your age? {username} ")
        age = input(prompt)

        print(f"""So you said you {likes} about liking me.\nProfessionally you do {occupation}.\nAnd your age is {age}.\nThanks for the survey {username}.""")
        return False
        
prompts_passing_game()