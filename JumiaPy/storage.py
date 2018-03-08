import pandas as pd
import sqlite3
import os

class Excel(object):
    """
    This class receives the names, links, prices, ratings, rated_sales, sellers
    parameters as lists, where all the lists must be of same length.
    It then makes an excel file out of them using the Pandas DataFrame.

    It has the following methods:

        make_table()
        output()
    
    
    """
    def __init__(self, names, links, prices, ratings, rated_sales, sellers):
        
        self.names = names
        self.links = links
        self.prices = prices
        self.ratings = ratings
        self.rated_sales = rated_sales
        self.sellers = sellers
        self.pd_dataframe = []
        
    def make_table(self):
        
        self.pd_dataframe = pd.DataFrame({"Names": self.names, "Links": self.links, "Prices": self.prices,
                                    "Ratings": self.ratings, "Rated Sales": self.rated_sales,
                                    "Sellers": self.sellers})
    def output(self):
        writer = pd.ExcelWriter("output.xlsx")
        self.pd_dataframe.to_excel(writer, "Sheet1", index = False)
        writer.save()
        
        
class Database(object):

	"""
	This class receives the names, links, prices, ratings, rated_sales, sellers
    parameters as lists, where all the lists must be of same length.
    It then creates an SQLite database, creates a table and inserts the values.

    It has the following methods:

        create()
        connect()
        make_table()
        insert_row()

	"""

	def __init__(self, names, links, prices, ratings, rated_sales, sellers):

		self.names = names
		self.links = links
		self.prices = prices
		self.ratings = ratings
		self.rated_sales = rated_sales
		self.sellers = sellers
		self.connect_status = None
        
        #Database table and column names
		self.table_name = "PRODUCTS"
		self.index_column = "ID"
		self.column_1 = "NAMES"
		self.column_2 = "LINKS"
		self.column_3 = "PRICES"
		self.column_4 = "RATINGS"
		self.column_5 = "RATEDSALES"
		self.column_6 = "SELLERS"

	def create(self):

		if "output.sqlite3" in os.listdir("."):
			os.remove("output.sqlite3")
		else:
			new_database = sqlite3.connect("output.sqlite3")
			new_database.close()

	def connect(self):

		self.connect_status = sqlite3.connect("output.sqlite3")
		return self.connect_status.cursor()

	def make_table(self, access):

		access.execute("CREATE TABLE {} ({} INTEGER PRIMARY KEY, {} TEXT, {} TEXT, {} REAL,\
                        {} REAL,{} INTEGER, {} TEXT);".format(self.table_name, self.index_column,
                                                              self.column_1, self.column_2, 
                                                              self.column_3, self.column_4, 
                                                              self.column_5, self.column_6))

	def insert_row(self, access):

		for name, link, price, rating, rated_sale, seller in zip(self.names,self.links ,self.prices,
                                                                 self.ratings, self.rated_sales, self.sellers):

		    access.execute("INSERT INTO {} ({} , {} , {}, {}, {}, {})\
                            VALUES (?, ?, ?, ?, ?, ?);".format(self.table_name, self.column_1,
                            	                               self.column_2, self.column_3,
                            	                               self.column_4, self.column_5,
                            	                               self.column_6), (name, link, price,
                            	                               rating, rated_sale, seller))

	def commit_changes(self):

		self.connect_status.commit()

	def disconnect(self):

		self.connect_status.close()