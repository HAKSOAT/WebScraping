import requests
import re
import pandas as pd
from bs4 import BeautifulSoup as bso

class JumiaProduct(object):
    """
    This class parses the products section pages of jumia.com.ng,
    then it extracts some data such as the product names, prices, ratings, number of rated sales,
    links, sellers.
    
    You instantiate this class, by passing in:
             a valid section link as a parameter (a string) 
             the start page number (an integer)
             the end page number (an integer)
    
    The link should be the first page of section without having page number in the string:
    
    Correct: https://www.jumia.com.ng/mobile-phones/
             https://www.jumia.com.ng/beauty-corner/
             
    Wrong:   https://www.jumia.com.ng/mobile-phones/?page=1
             https://www.jumia.com.ng/beauty-corner/?page=1
    
    
    Example: JumiaProduct("https://www.jumia.com.ng/mobile-phones/", 2, 4)
    
    If link is wrong, it returns an InvalidLink error.
    
    It has the following methods:
    
       get_pages()
       get_products()
       get_links()
       get_prices()
       get_names()
       get_ratings()
       get_sales() 
       get_sellers()
    
    """
    
    def __init__(self, category_link, start_page, end_page):
        
        if requests.get(category_link).status_code != 200:
            raise ConnectionError("This link is invalid")
        
        if (".html" or "?") in category_link:
            raise Exception("This link doesn't lead to a Jumia category")
        
        if (type(start_page) or type(end_page)) != int:
            raise TypeError("start_page and end_page should be integers")
            
        
        self.category_link = category_link
        self.start_page = start_page
        self.end_page = end_page
        self.pages = []
        self.products = []
        self.names = []
        self.links = []
        self.prices = []
        self.ratings = []
        self.rated_sales = []
        self.sellers = []
        
        
    def get_pages(self):
        """
        
        This method is used to get the html pages of products from
        the section link provided.
        
        It returns a list of the html pages.
        
        """
        
        for page_number in range(self.start_page, self.end_page + 1):
                address_extension = "?page={}".format(page_number)
                full_address = self.category_link + address_extension
                html_request = requests.get(full_address)
                html_content = html_request.content
                page = bso(html_content, "html.parser").find("section", {"class":"products -mabaya"})
                self.pages.append(page)   
                
    def get_products(self): 
        """
        
        This method is used to get the products from
        the section link provided.
        
        It returns a list of the products.
        
        """
        
        for page in self.pages:
            class_value = re.compile(r"(?:^mabaya sku -gallery$)|(?:^sku -gallery$)|(?:^sku -gallery.+$)")
            self.products += page.find_all("div", {"class": class_value})  
          
    def get_links(self):
        """
        
        It takes in a list of html pages already parsed by the get_pages method
        and further parses them to get the link
        to every product.
        
        It returns a list of the product links
        
        """
        
        for product in self.products:
            self.links.append(product.find("a")["href"])
    
    def get_names(self):
        """
        
        It takes in a list of html pages already parsed by the get_pages method
        and further and parses them to get the name
        of every product.
        
        It returns a list of the product names
        
        """
        
        for product in self.products:
            self.names.append(product.find("span", {"class": "name"}).text)
        
    def get_prices(self):
        """
        
        It takes in a list of html pages already parsed by the get_pages method
        and further and parses them to get the price
        of every product.
        
        It returns a list of the product prices
        
        """
        
        for product in self.products:
            self.prices.append(product.find("span", {"data-price": re.compile(r"\d+")}).text)
        
    def get_ratings(self):
        """
        
        It takes in a list of html pages already parsed by the get_pages method
        and further and parses them to get the rating
        of every product.
        
        It returns a list of the product ratings
        
        """
        
        for product in self.products:
            if product.find("div", {"class": "stars"}) == None:
                self.ratings.append("No Rating")
            else:
                rating_tag = product.find("div", {"class": "stars"})["style"]
                rating_re = re.compile(r"[0-9]+")
                stars = format(int(rating_re.findall(rating_tag)[0])/100 * 5, '.2f')
                self.ratings.append(stars)
    
    def get_rated_sales(self):
        """
        
        It takes in a list of html pages already parsed by the get_pages method
        and further and parses them to get the number of sales
        of every product.
        
        It returns a list of the product sales number
        
        """

        for product in self.products:
            if product.find("div", {"class": "total-ratings"}) == None:
                self.rated_sales.append("No Rated Sales")
            else:
                dirty_sales = product.find("div", {"class": "total-ratings"}).text
                rated_sales_re = re.compile(r"[0-9]+")
                self.rated_sales.append(rated_sales_re.findall(dirty_sales)[0])
                
    def get_sellers(self):
        """
        
        It takes in a list of html pages already parsed by the get_pages method
        and further and parses them to get the seller
        of every product.
        
        It returns a list of the product sellers
        
        """
        
        for product in self.products:
            self.sellers.append(product.find("span", {"class": "brand "}).text)