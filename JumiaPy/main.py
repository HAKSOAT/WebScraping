from jumia_product import JumiaProduct
from storage import Excel, Database
import sys


output_type = sys.argv[1]
category_link = sys.argv[2]
start_page = int(sys.argv[3])
end_page = int(sys.argv[4])



def parse_product(category_link, start_page, end_page):

	product = JumiaProduct(category_link, start_page, end_page)
	product.get_pages()
	product.get_products()
	product.get_links()
	product.get_names()
	product.get_prices()
	product.get_ratings()
	product.get_rated_sales()
	product.get_sellers()

	return product

def save_to_excel(names, links, prices, ratings, rated_sales,
                  sellers):

	excel = Excel(names, links, prices, ratings, rated_sales,
                  sellers)
	excel.make_table()
	excel.output()

def save_to_database(names, links, prices, ratings, rated_sales,
                  sellers):

    database = Database(names, links, prices, ratings, rated_sales,
                  sellers)

    database.create()
    connection = database.connect()
    database.make_table(connection)
    database.insert_row(connection)
    database.commit_changes()
    database.disconnect()


if "__main__" == __name__:
	product = parse_product(category_link, start_page, end_page)
	if output_type == "-e":
		save_to_excel(product.names, product.links, product.prices,
    	              product.ratings, product.rated_sales, 
    	              product.sellers)
	elif output_type == "-d":
		save_to_database(product.names, product.links, product.prices,
    	              product.ratings, product.rated_sales, 
    	              product.sellers)
	else:
		raise Exception("Wrong output file parameter.")
