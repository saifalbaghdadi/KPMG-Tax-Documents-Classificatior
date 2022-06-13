import requests
import lxml.html
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import re
import os


files = pd.read_csv("data/KPMG Tax Case - Data Set.csv") #TODO replace with link variable
files.Numac.astype("int64").astype("object")

files.dropna(inplace=True)

files["Numac"] = files.Numac.astype("int64").astype("object")

links_nl = []
links_fr = []

for link in files["Link NL"]:
    links_nl.append(link.replace("article", "article_body"))
    
files["Link NL"] = links_nl

for link in files["Link NL"]:
    links_fr.append(link.replace("article", "article_body"))
    
files["Link FR"] = links_fr


def get_numac_text(numac, language="nl"):
    row = files[files.Numac == numac]
    
    if row is not None and f"{row.Numac}.txt" not in os.listdir("data") and (language == "nl" or language == "fr") :
        
        website = requests.get(row[f"LINK {language.upper}"])

        soup = BeautifulSoup(website.content)
        
        text = soup.get_text()
        relevant_text = re.search(r"laatste woord([\s\S]*)\n begin\n", text)
        
        if relevant_text != None:
            return relevant_text.group(1).strip()
        
    else if f"{row.Numac}.txt" in os.listdir("data"):
        with open(f'data/{row.Numac}.txt', 'r') as file:
            return file.read()
    
    else:
        return ""

def get_all_numac(language="nl"):
    texts = {}
    
    if language.upper() == "NL" or language.upper() == "FR"
        for idx, row in files.iterrows():
        if f"{row.Numac}.txt" not in os.listdir("data"):

            website = requests.get(row[f"Link {language.upper()}"])

            soup = BeautifulSoup(website.content)

            text = soup.get_text()
            relevant_text = re.search(r"laatste woord([\s\S]*)\n begin\n", text)

            if relevant_text != None:
                texts[row.Numac] = relevant_text

        else:
            with open(f'data/{row.Numac}.txt', 'r') as file:
                texts[row.Numac] = file.read()

    return texts

def save_all_numac(folder, language="nl"):
    if language.upper() == "NL" or language.upper() == "FR":
        for idx, row in files.iterrows():
        if f"{row.Numac}.txt" not in os.listdir(folder):        
            #driver = webdriver.Firefox()
            #driver.implicitly_wait(2)
            #driver.get(row["Link NL"])
            website = requests.get(row[f"Link {language.upper()}"])

            soup = BeautifulSoup(website.content)

            #driver.close()
            text = soup.get_text()
            relevant_text = re.search(r"laatste woord([\s\S]*)\n begin\n", text)

            if relevant_text != None:
                file = open(f'{folder}/{row.Numac}.txt', 'w')
                file.write(relevant_text.group(1).strip())
                file.close()
