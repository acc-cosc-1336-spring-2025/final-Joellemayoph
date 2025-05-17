#add import
import question_d

def get_stock_purchase_history():

    mystocks = {}

    stock_list = { 'AAPL' : 'Apple Inc',
                'CAT' : 'Caterpillar',
                'EK' : 'Eastman Kodak',
                'GOOG' : 'Google',
                'MSFT' : 'Microsoft'}
    

    symbols = []
    
    for index in range(1,6):
        sym = input(f'Enter symbol for purchase {index}: ').upper()
        symbols.append(sym)

    for sym in symbols: 
        stock = question_d.Stock(sym, stock_list[sym])
        mystocks[sym] = stock

    print()
    print('Stock Purchase History')
    print(f'SYMBOL\tCOMPANY NAME')
    print('------------------')
    for value in mystocks:
        stock = mystocks[value]
        print(f'{stock.get_symbol()}\t{stock.get_company_name()}')


def display_menu():
    print('1 - GET STOCK PURCHASE HISTORY')
    print('2 - EXIT')

def run_menu():
    user_option = '0'

    while(user_option != '2'):
        display_menu()

        user_option = input("ENTER A MENU OPTION(1 or 2): ")
        handle_menu(user_option)

def handle_menu(user_option):
    if(user_option == '1'):
        
        get_stock_purchase_history()
        
        user_option1 = input('WOULD YOU LIKE TO CONTNIUE? (Y/N): ')
        
        while(user_option1 == 'Y'):
            get_stock_purchase_history()

            user_option1 = input('WOULD YOU LIKE TO CONTINUE? (Y/N): ')

    elif(user_option == '2'):
        print('EXITING ...')

    else:
        print('INVALID INPUT')

run_menu()

