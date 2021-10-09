import requests
import json
import csv

APY_KEY = "127e2ff2f6115e176eb53814ac2a313a"
PASSWORD = "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"
HOSTNAME = "dangvandat15021997"
VERSION = "2021-10"
RESOURCE = "customers"

url = f'https://{APY_KEY}:{PASSWORD}@{HOSTNAME}.myshopify.com/admin/api/{VERSION}/{RESOURCE}.json'
customer_data = requests.get(url)
customers = customer_data.json()

if customers["customers"]:
    cols = []
    for index in range (len(customers["customers"])):
        if (index == 0):
            cols = customers["customers"][index].keys()
        with open('customers.csv', 'w', newline ='')  as output_file:
            dict_writer = csv.DictWriter(output_file, cols)
            dict_writer.writeheader()
            dict_writer.writerows(customers["customers"])