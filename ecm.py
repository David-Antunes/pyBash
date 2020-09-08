import os
import sys
import pathlib as pl
import subprocess

# Displays the prompt in the pyBash
prompt = ''

# Directories to verify if there is a corresponding script to be executed
path = []

# Structure of colors inside the pyBash
colors = []

# Extensions the program recognizes and will try to execute
execute_file = {}


# initial values
# delete after config files are done

prompt = os.getcwd() + ':$ '
path = [os.getcwd + '/ecms',]
execute_file = {
    '.py' : 'python3',
}

def execute_script():
    pass

def check_if_script_exists():
    pass

def get_file_extension():
    pass

def change_dir():
    pass

def main():

    
    while(1):

        cmd = input(prompt) # Holds the user input
        
        if(cmd == 'exit' or cmd == 'q'):
            print('Bye!')
            break  
        elif(cmd == 'cd'):
            change_dir()
        else:
                subprocess.run(['python3', 'h'])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt: # This is to not generate an error when you ctrl+c the program
        print()


