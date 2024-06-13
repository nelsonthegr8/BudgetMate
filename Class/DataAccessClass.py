import csv
import json

class DataAccessClass():
    
    def getAccountData(filter):
        data = {}
        csvFilePath = r"C:\Users\nelso\Downloads\Family Financials.xlsx - Accounts.csv"
        # Open a csv reader called DictReader
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            
            # Convert each row into a dictionary 
            # and add it to data
            for rows in csvReader:
                
                # Assuming a column named 'No' to
                # be the primary key
                key = rows['No']
                data[key] = rows
    
        # Open a json writer, and use the json.dumps() 
        # function to dump data
        # with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        #     jsonf.write(json.dumps(data, indent=4))
        return data
       
