
import pandas as pd
import sqlite3

class Excel(object):
    """
    
    
    
    """
    def __init__(self, names, links, prices, ratings, rated_sales, sellers):
        
        self.names = names
        self.links = links
        self.prices = prices
        self.ratings = ratings
        self.rated_sales = rated_sales
        self.sellers = sellers
        self.pd_dataframe = []
        
    def make_tables(self):
        
        pd_dataframe = pd.DataFrame({"Names": self.names, "Links": self.links, "Prices": self.prices,
                                    "Ratings": self.ratings, "Rated Sales": self.rated_sales,
                                    "Sellers": self.sellers})
    def output(self):
        writer = pd.ExcelWriter("output.xlsx")
        pd_dataframe.to_excel(writer, "Sheet1", index = False)
        writer.save()
        
        
class Database(object):
    
    def __init__(self, names, links, prices, ratings, rated_sales, sellers):
        
        self.names = names
        self.links = links
        self.prices = prices
        self.ratings = ratings
        self.rated_sales = rated_sales
        self.sellers = sellers
        self.connect_status = None 

    def create(self):
        new_database = sqlite3.connect("output.sqlite3")
        new_database.close()
        
    def connect(self):
        self.connect_status = sqlite3.connect("output.sqlite3")
        return self.connect_status.cursor()
    
    def make_table(self, access):
        table_name = "JUMIA PRODUCTS"
        index_column = "ID"
        access.execute("CREATE TABLE {} ({} INTEGER AUTOINCREMENT, {} TEXT, {} TEXT, {} REAL,\
                        {} REAL,{} INTEGER, {} TEXT);".format(index_column, self.names, self.links, self.prices,
                                                             self.ratings, self.rated_sales, self.sellers))