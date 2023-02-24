"""
A simple, feature rich, command line interface (cli). Took some insperation from windows and linux systems.
"""

#libraries
import os
import random as rand
import json 
from rich.console import Console

#So I can style the text
console = Console()

#Login to the CLI
def login():
    with open("logins.json", 'r') as f:
        logins = json.load(f)
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")
    if entered_username in logins and entered_password in logins[entered_username]:
        print(f'Login in as {entered_username}.')
        main_menu()
    else:
        print("Login information false you hacker.")

#Text editor
def text_editor():
    print('')
#Utillity menu
def utillity():
    console.print('1. Text editor', sytle='green')
def main_menu():
    main_menu_logo = '''                                                                                                                                                          
        CCCCCCCCCCCCC                                                                                        CCCCCCCCCCCCCLLLLLLLLLLL             IIIIIIIIII
     CCC::::::::::::C                                                                                     CCC::::::::::::CL:::::::::L             I::::::::I
   CC:::::::::::::::C                                                                                   CC:::::::::::::::CLL::::::::L             I::::::::I
  C:::::CCCCCCCC::::C                                                                                  C:::::CCCCCCCC::::CLL:::::::LL             II::::::II
 C:::::C       CCCCCC   ooooooooooo       ssssssssss      mmmmmmm    mmmmmmm      ooooooooooo         C:::::C       CCCCCC  L:::::L                 I::::I  
C:::::C               oo:::::::::::oo   ss::::::::::s   mm:::::::m  m:::::::mm  oo:::::::::::oo      C:::::C                L:::::L                 I::::I  
C:::::C              o:::::::::::::::oss:::::::::::::s m::::::::::mm::::::::::mo:::::::::::::::o     C:::::C                L:::::L                 I::::I  
C:::::C              o:::::ooooo:::::os::::::ssss:::::sm::::::::::::::::::::::mo:::::ooooo:::::o     C:::::C                L:::::L                 I::::I  
C:::::C              o::::o     o::::o s:::::s  ssssss m:::::mmm::::::mmm:::::mo::::o     o::::o     C:::::C                L:::::L                 I::::I  
C:::::C              o::::o     o::::o   s::::::s      m::::m   m::::m   m::::mo::::o     o::::o     C:::::C                L:::::L                 I::::I  
C:::::C              o::::o     o::::o      s::::::s   m::::m   m::::m   m::::mo::::o     o::::o     C:::::C                L:::::L                 I::::I  
 C:::::C       CCCCCCo::::o     o::::ossssss   s:::::s m::::m   m::::m   m::::mo::::o     o::::o      C:::::C       CCCCCC  L:::::L         LLLLLL  I::::I  
  C:::::CCCCCCCC::::Co:::::ooooo:::::os:::::ssss::::::sm::::m   m::::m   m::::mo:::::ooooo:::::o       C:::::CCCCCCCC::::CLL:::::::LLLLLLLLL:::::LII::::::II
   CC:::::::::::::::Co:::::::::::::::os::::::::::::::s m::::m   m::::m   m::::mo:::::::::::::::o        CC:::::::::::::::CLL:::::::::::::::::::::LI::::::::I
     CCC::::::::::::C oo:::::::::::oo  s:::::::::::ss  m::::m   m::::m   m::::m oo:::::::::::oo           CCC::::::::::::CL:::::::::::::::::::::LI::::::::I
        CCCCCCCCCCCCC   ooooooooooo     sssssssssss    mmmmmm   mmmmmm   mmmmmm   ooooooooooo                CCCCCCCCCCCCCLLLLLLLLLLLLLLLLLLLLLLLLIIIIIIIIII
                 '''
    console.print(main_menu_logo, style='light_green')
    console.print('1. Utility Menu', sytle='green')
    console.print('2. Game Menu', sytle='light_green')
    console.print('3. Exit', sytle='green')
    user_choice = input()
    if user_choice == '1':
        pass
    elif user_choice == '2':
        pass
    elif user_choice == '3' or 'exit':
        pass
