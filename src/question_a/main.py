#add import
import pickle
import question_a

def datfile():
    stock_list = { 'AAPL' : 'Apple Inc',
                'CAT' : 'Caterpillar',
                'EK' : 'Eastman Kodak',
                'GOOG' : 'Google',
                'MSFT' : 'Microsoft'}

    with open('stock_file.dat', 'wb') as output_file:
        pickle.dump(stock_list, output_file)

#datfile()

def display_list(stock_list):
    print('Stock Purchase History')
    print(f'SYMBOL\tCOMPANY NAME')

    for item in stock_list:
        print(item.get_symbol() + '    ' +item.get_company_name())
        print()

def get_stock_list():
    stock_list = []

    with open('stock_file.dat', 'rb') as outfile:
        slist = pickle.load(outfile)

    for count in range (1,6): 

        print('Enter recent purchases: ')
        sym = input('Enter the ticket for purchase ' + str(count) + ': ')
        cname = slist[sym]

        print() 

        #Adjust after you move over 

        option = question_a.Stock(sym, cname)

        stock_list.append(option)
        
    return stock_list 

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
        
        stock_list = get_stock_list()
        display_list(stock_list)

        user_option1 = input('WOULD YOU LIKE TO CONTINUE? (Y/N): ')
        
        while(user_option1.upper() == 'Y'):
            stock_list = get_stock_list()
            display_list(stock_list)


    elif(user_option == '2'):
        print('EXITING ...')

    else:
        print('INVALID INPUT')

run_menu()
    



