import json
import os

INVENTORY_FILE = "inventory.json"

class Product:

    def __init__ (self, product_id, name, price, stock):

        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock  = stock

    def update_stock(self, quantity):

        if quantity < 0 :
            return False

        else:
            self.__stock = quantity
            return True

    def display_information (self):
        print (f"Product ID:  {self.__product_id} | Product Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def get_product_id (self):
         get_product_ID = self.__product_id
         return get_product_ID

    def to_dict(self):
        return {"Product ID": self.__product_id, "Product Name": self.__name, "Price": self.__price, "Stock": self.__stock}




