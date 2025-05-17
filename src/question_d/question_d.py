#write functions here, don't add input('') statements here!

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name 

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name
    
    def set_symbol(self, symbol):
        self.__symbol = symbol

    def __str__(self):
        return f'The stock purchased is {self.__company_name}'

    



