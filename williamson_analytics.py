### Demonstrate skills in fetching data from the web, processing it using Python collections, and writing the processed data to different file formats.

# Imports
import csv
import json
import os
import pandas as pd
import pathlib 
import requests  
import xlrd

# Local module imports
#import williamson_attr      
#import williamson_projsetup

## Aquire data from URLs

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_txt_file(folder_name, filename, response.text)
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        write_excel_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

def fetch_and_write_csv_data(folder_name, filename,url):
    response = requests.get(url)
    if response.status_code == 200:
        write_csv_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch CSV data: {response.status_code}")

def fetch_and_write_json_data(folder_name, filename,url):
    response = requests.get(url)
    if response.status_code == 200:
        write_json_file(folder_name, filename, response.content)
    else:
        print(f"Failed to fetch JSON data: {response.status_code}")

## Write data to new folders and files

def write_txt_file(folder_name, filename, data):
    pathlib.Path(folder_name).mkdir(exist_ok=True)
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

def write_excel_file(folder_name, filename, data):
    pathlib.Path(folder_name).mkdir(exist_ok=True)
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

def write_csv_file(folder_name, filename, data):
    pathlib.Path(folder_name).mkdir(exist_ok=True)
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

def write_json_file(folder_name, filename, data):
    pathlib.Path(folder_name).mkdir(exist_ok=True)
    file_path = pathlib.Path(folder_name).joinpath(filename) # use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(data)
        print(f"JSON data saved to {file_path}")

## Data processing
## Function 1. Process Text Data: Process text with lists and sets 
def process_txt_file(folder_name,input_txt,output_txt):
    path = pathlib.Path(folder_name).joinpath(input_txt)
    words = []
    unique_words = set()
    
    with open(path, 'r') as file:
        data = file.read()
        words = data.split()
        unique_words = set(words)
    
    word_count = len(words)
    unique_word_count = len(unique_words)
    
    with open(output_txt, 'w') as file:
        file.write(f"Word Count: {word_count}\n")
        file.write(f"Unique Word Count: {unique_word_count}\n")

## Function 2. Process CSV Data: Process CSV files with tuples
def process_csv_file(folder_name,input_txt,output_txt):
    path = pathlib.Path(folder_name).joinpath(input_txt)
    data = []
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(tuple(row))
        tuple(data)
    with open(output_txt, 'w') as file:
        file.write(str(data))
    
## Function 3. Process Excel Data: Extract and analyze data from Excel files
def process_excel_file(folder_name,input_txt,output_txt):
    path = pathlib.Path(folder_name).joinpath(input_txt)
    df = pd.read_excel(path)
    # Analyze the Excel data
    insights = df.describe()
    with open(output_txt, 'w') as file:
        file.write(str(insights))

## Function 4. Process JSON Data: Process JSON data with dictionaries
def process_json_file(folder_name,input_txt,output_txt):
    path = pathlib.Path(folder_name).joinpath(input_txt) 
    input_json = open(path, 'r', encoding='utf-8').read()
    data = json.loads(input_json)
    people = data['people']
    
    with open(output_txt,'w') as file:
        for person in people:
            file.write(f"Name: {person['name']}\n")
            
## Main
def main():
    ''' Main function to demonstrate module capabilities. '''

    print(f"Name: Scott Williamson")

    txt_url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
    csv_url = 'https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv' 
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls' 
    json_url = 'http://api.open-notify.org/astros.json'

    txt_folder_name = 'data-txt'
    csv_folder_name = 'data-csv'
    excel_folder_name = 'data-excel' 
    json_folder_name = 'data-json' 

    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls' 
    json_filename = 'data.json' 

    fetch_and_write_txt_data(txt_folder_name, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder_name, csv_filename,csv_url)
    fetch_and_write_excel_data(excel_folder_name, excel_filename,excel_url)
    fetch_and_write_json_data(json_folder_name, json_filename,json_url)

    process_txt_file(txt_folder_name,'data.txt', 'results_txt.txt')
    process_csv_file(csv_folder_name,'data.csv', 'results_csv.txt')
    process_excel_file(excel_folder_name,'data.xls', 'results_xls.txt')
    process_json_file(json_folder_name,'data.json', 'results_json.txt')

if __name__ == '__main__':
    main()