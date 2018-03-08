JumiaPy is written to scrape [Nigeria's number one ecommerce store](www.jumia.com.ng).

**THIS IS STRICTLY FOR EDUCATIONAL PURPOSES.**

This program scrapes the following information from the website:

	* Product Names

	* Product Links

	* Product Prices

	* Product Ratings

	* Product Seller


Installation:

	Simply fork this repository to your local machine, navigate to the JumiaPy directory, there you would find all the files for this project.

Requirements:

	To install the requirements run the command below:

	```
		pip install -r requirements.txt

	```

	It installs the requirements on your machine.


	> Python3 is required.


Usage:

	To use this code, you run the main.py file.

	This file takes four arguments:

		The output file type
		The section link
		The section start page number of choice
		The section end page number of choice


    The output file type:

	The output file choices are an excel file and an SQLite database file.

	You can select any of them using:

	-e for Excel
	-d for SQLite



	The section link:
    
    The link should be the first page of section without having page number in the string:
    
    Correct: "https://www.jumia.com.ng/mobile-phones/"
             "https://www.jumia.com.ng/beauty-corner/"
             
    Wrong:   "https://www.jumia.com.ng/mobile-phones/?page=1"
             "https://www.jumia.com.ng/beauty-corner/?page=1"
    
    
    > Remember: The link should be in double quotes, and don't forget the trailing forward slash.
    
    If link is wrong, it returns an error.


    The start and end page of choice:

    This should be a single integer value, indicating the start and end page of choice.

    


    Examples:

    ```
    python main.py -e "https://www.jumia.com.ng/mobile-phones/" 2 5

    ```

    This scrapes the mobile phones section from page 2 to page 5 and saves in an excel file.


    ```
    python main.py -d "https://www.jumia.com.ng/mobile-phones/" 1 10

    ```

    This scrapes the mobile phones section from page 1 to page 10 and saves in an SQLite database.




    Kindly raise issues if you have problems with the program running.


