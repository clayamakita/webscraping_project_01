# Web scraping project using Python

The goal of this project is to use web scraping to extract data from different supermarkets' websites and analyze changes over time and the best deals for some common products. The library Beautiful Soup is being used. As the project evolves, one script will be released each month. Below are listed the ones so far:

1. January 2023: The code is available in [this file](https://github.com/clayamakita/webscraping_project_01/blob/main/webscraping_01.py). It defines functions to extract and transform the data. A list of products' urls is used to loop for the items in order to extract the product name and price and assign them to a dataframe.

2. February 2023: The code is available in [this file](https://github.com/clayamakita/webscraping_project_01/blob/main/webscraping_02.py). The script was developed using the base from the previous month and it included webscraping two different supermarket websites. A list of the same products in both supermarkets' websites was created in order to ultimately compare prices between them. The results were stored in a dataframe and saved in a csv file.

3. March 2023: The code is available in [this file](https://github.com/clayamakita/webscraping_project_01/blob/main/webscraping_03.py). The idea for this month is to run the script, at least, once a week, include other products and analyze the results using Pandas and possibly a visualization tool.

## Starting the project

### Installing all modules
```
pip install -r requirements.txt
```
or
```
python -m pip install -r requirements.txt
```

### Running the project

```
python [filename]
```
