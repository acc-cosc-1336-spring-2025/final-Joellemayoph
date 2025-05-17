#add import
from question_b import display_multiplication_table

def display_menu():
    print('1 - MULTIPLICATION TABLE')
    print('2 - EXIT')

def run_menu():
    user_option = '0'

    while(user_option != '2'):
        display_menu()

        user_option = input("ENTER A MENU OPTION(1 or 2): ")
        handle_menu(user_option)

def handle_menu(user_option):
    if(user_option == '1'):
        
        length = int(input('HOW MANY ROWS FOR YOUR TABLE? '))
        height = int(input('HOW MANY COLUMNS FOR YOUR TABLE? '))
        display_multiplication_table(length,height)
        
        user_option1 = input('WOULD YOU LIKE TO CONTNIUE? (Y/N): ')
        
        while(user_option1 == 'Y'):
            length = int(input('HOW MANY ROWS FOR YOUR TABLE? '))
            height = int(input('HOW MANY COLUMNS FOR YOUR TABLE? '))
            display_multiplication_table(length,height)

            user_option1 = input('WOULD YOU LIKE TO CONTINUE? (Y/N): ')

    elif(user_option == '2'):
        print('EXITING ...')

    else:
        print('INVALID INPUT')

run_menu()
