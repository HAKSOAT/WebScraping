
import pandas as pd

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
        