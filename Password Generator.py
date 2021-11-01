#-----------------------------------------------------------------------------------------------------------------------
# Imports

import colorama
from colorama import Fore, Style, Back
from random import choice
from string import ascii_letters, punctuation, digits


#-----------------------------------------------------------------------------------------------------------------------
# Coding

def password_generator(Length=8):
  chars = tuple(ascii_letters) + tuple(punctuation) + tuple(digits)
  pwd = ''.join(choice(chars) for i in range(Length))
  return pwd
  
print("""



                    ___  __    __   __  _   _  __  ___ __     __ ___ __  _ ___ ___  __ _____ __  ___  
                    | _,\/  \ /' _//' _/| | | |/__\| _ \ _\   / _] __|  \| | __| _ \/  \_   _/__\| _ \ 
                    | v_/ /\ |`._`.`._`.| 'V' | \/ | v / v | | [/\ _|| | ' | _|| v / /\ || || \/ | v / 
                    |_| |_||_||___/|___/!_/ \_!\__/|_|_\__/   \__/___|_|\__|___|_|_\_||_||_| \__/|_|_\  
                    
                                 Password Generator v1.0 coded by @Pronunciare
                                              t.me/TrustyProjects 


""")

def main():
  try:
    length = int(input("Indica la lunghezza della password: "))
    print("Password generata:", password_generator(length))
  except ValueError:
    print("Non hai inserito nessun numero.")
    
if __name__ == "__main__":
   main()
   
input()

    
