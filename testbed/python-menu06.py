'''
Date: 10.1.2020
By: Ali Radwani.  www.ahradwani.com

Main_Menu Function 
'''
import os

def main_menu():

    """
    Template Function to help in creating a Menu for the application.

    You can change the names and functions must be defined.
    """
    while True:
        os.system("clear")
        print('\n ===========[ MENU NAME]=============')
        print('  --------------------------------------')
        print(' 1. Function-1 Name.')
        print(' 2. Function-2 Name. ')
        print(' 3. Function-3 Name')
        print(' 9. Exit')
        uinp= input('\n Enter your Selection: ')

        if uinp == '1':
            Function_1_Name()
        elif uinp == '2':
            Function_2_Name()
        elif uinp == '3':
            Function_3_Name()
        elif uinp =='9':
            return
        else:
            print('\n  Please select from the Menu.'