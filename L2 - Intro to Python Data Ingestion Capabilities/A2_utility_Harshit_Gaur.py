"""
<Module 2 Assignment>

Copyright (c) 2021 -- This is the 2021 Fall A version of the Template
Licensed
Written by <Harshit Gaur>

# you can also rely on the docstring documentation from pandas on how to format dosctrings:
# https://pandas.pydata.org/pandas-docs/stable/development/contributing_docstring.html
"""

import pandas as pd
from bs4 import BeautifulSoup
import sqlite3

def read_txt_file(txt_file):
    """
    Read Text File, Import data from it and assign in to an appropriate Data Structure. 
    :param txt_file : Text File
    :return: Data Structure (Data Frame)
    """
    
    return pd.read_table(filepath_or_buffer = txt_file, sep = '|', header = 0)

def read_csv_file(csv_file):
    """
    Read CSV File, Import data from it and assign in to an appropriate Data Structure. 
    :param csv_file : CSV File
    :return: Data Structure (Data Frame)
    """
    
    return pd.read_csv(filepath_or_buffer = csv_file, sep = ',', header = 0)

def read_json_file(json_file):
    """
    Read JSON File, Import data from it and assign in to an appropriate Data Structure. 
    :param json_file : JSON File
    :return: Data Structure (Data Frame)
    """
    
    return pd.read_json(path_or_buf=json_file)

def read_html_file(html_file):
    """
    Read HTML File, Import data from it in parsed format and assign in to an appropriate Data Structure. 
    :param html_file : HTML File
    :return: Data Structure (Data Frame)
    """
    
    page = open(html_file).read()
    return BeautifulSoup(page, 'html.parser')

def read_db_file(db_file):
    """
    Connect & Read Database File, Import data from it and assign in to an appropriate Data Structure. 
    :param db_file : Database File
    :return: Data Structure (Data Frame)
    """
    
    return sqlite3.connect(db_file)

def read_excel_file(excel_file):
    """
    Read Excel File, Import data from it and assign in to an appropriate Data Structure. 
    :param excel_file : Excel File
    :return: Data Structure (Data Frame)
    """
    
    return pd.ExcelFile(excel_file)

if __name__ == '__main__':
    print("Initializing")
    
    