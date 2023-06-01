# Web scraping project using Python

The goal of this project is to use web scraping to extract data from different supermarkets' websites and analyze changes over time and the best deals for some common products. The library Beautiful Soup is being used. As the project evolves, one script will be released each month. Below are listed the ones so far:

1. January 2023: The code is available in [this file](https://github.com/clayamakita/webscraping_project_01/blob/main/webscraping_01.py). It defines functions to extract and transform the data. A list of products' urls is used to loop for the items in order to extract the product name and price and assign them to a dataframe.

2. February 2023: The code is available in [this file](https://github.com/clayamakita/webscraping_project_01/blob/main/webscraping_02.py). The script was developed using the base from the previous month and it included webscraping two different supermarket websites. A list of the same products in both supermarkets' websites was created in order to ultimately compare prices between them. The results were stored in a dataframe and saved in a csv file.

3. March 2023: The code is available in [this file](https://github.com/clayamakita/webscraping_project_01/blob/main/webscraping_03.py). New products were included, improvements to the script were made and the script was run about once a week. A [Jupyter Notebook](https://github.com/clayamakita/webscraping_project_01/blob/main/analysis_webscraping.ipynb) was created to read the files and clean the data. 

4. April 2023: The script was run once a week and results are being analyzed in a [Jupyter Notebook](https://github.com/clayamakita/webscraping_project_01/blob/main/analysis_webscraping.ipynb) and in a [Power BI report](https://app.powerbi.com/view?r=eyJrIjoiNDJkYjU3ZjctNGI4My00ZWE5LTlmYjAtMmM2ZTRhZGM5YTg4IiwidCI6ImZjNzk4OWZkLTI5NDUtNGViZS1hMWQxLTM2N2NkYWNhNjE2NSJ9).

5. May 2023: Created a [batch file](https://github.com/clayamakita/webscraping_project_01/blob/main/task_scheduler.bat) to automatically run the Python Script using the Windows task scheduler. Also improved the data slicer to always show the latest data upon refresh. Power BI report is available [here](https://app.powerbi.com/view?r=eyJrIjoiNDJkYjU3ZjctNGI4My00ZWE5LTlmYjAtMmM2ZTRhZGM5YTg4IiwidCI6ImZjNzk4OWZkLTI5NDUtNGViZS1hMWQxLTM2N2NkYWNhNjE2NSJ9)

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
