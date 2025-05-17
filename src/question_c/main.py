#add import
from question_c import get_most_likely_ancestor_consensus

def display_menu():
    print('1 - ANCESTOR CONSENSUS')
    print('2 - EXIT')

def run_menu():
    user_option = '0'

    while(user_option != '2'):
        display_menu()

        user_option = input("ENTER A MENU OPTION(1 or 2): ")
        handle_menu(user_option)

def handle_menu(user_option):
    if(user_option == '1'):
        
        dna1 = input('PLEASE ENTER A DNA STRING > 8 BUT <= 16: ')
        while len(dna1) < 8 or len(dna1) >= 16:
            print('INVALID STRING LENGTH, PLEASE TRY AGAIN')
            dna1 = input('PLEASE ENTER A DNA STRING > 8 BUT <= 16: ')
        
        dna2 = input('PLEASE ENTER A SUBSTRING OF 4 CHARACTERS: ')
        while len(dna2) != 4:
            print('INVALID STRING LENGTH, PLEASE TRY AGAIN')
            dna2 = input('PLEASE ENTER A SUBSTRING OF 4 CHARACTERS: ')
        
        result = get_most_likely_ancestor_consensus(dna1,dna2)
        print(result)

        user_option1 = input('WOULD YOU LIKE TO CONTINUE? (Y/N): ')
        
        while(user_option1.upper() == 'Y'):
            dna1 = input('PLEASE ENTER A DNA STRING > 8 BUT <= 16: ')
            while len(dna1) < 8 or len(dna1) >= 16:
                print('INVALID STRING LENGTH, PLEASE TRY AGAIN')
                dna1 = input('PLEASE ENTER A DNA STRING > 8 BUT <= 16: ')
        
            dna2 = input('PLEASE ENTER A SUBSTRING OF 4 CHARACTERS')
            while len(dna2) != 4:
                print('INVALID STRING LENGTH, PLEASE TRY AGAIN')
                dna2 = input('PLEASE ENTER A SUBSTRING OF 4 CHARACTERS')
            
            result = get_most_likely_ancestor_consensus(dna1,dna2)
            print(result)

            user_option1 = input('WOULD YOU LIKE TO CONTINUE? (Y/N): ')

    elif(user_option == '2'):
        print('EXITING ...')

    else:
        print('INVALID INPUT')

run_menu()