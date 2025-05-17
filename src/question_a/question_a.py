#write functions here, don't add input('') statements here!
def test_config():
    return True

import pickle


class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name 

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name
     
    

