import gspread
from oauth2client.service_account import ServiceAccountCredentials
import validators

class Reader:
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    def __init__(self, name):
        self.name = name
        # use creds to create a client to interact with the Google Drive API
    


reader = Reader('Reader')

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.

stores_sheet = reader.client.open_by_url('https://docs.google.com/spreadsheets/d/1LY4oHCzi3wh0kWB-5vGKju94ALeYP8hHxEUiin6J60Q/edit?resourcekey#gid=1170650640').sheet1

customers_sheet = reader.client.open_by_url('https://docs.google.com/spreadsheets/d/1nQcpdXqcNJhQZoR3w9McREpNzlM3u5gSmOstQHlQzwg/edit?resourcekey#gid=1474534520').sheet1

row = len(customers_sheet.col_values(1))
print(row)
entry = customers_sheet.row_values(row)
print(entry)

matching_stores = []


for i in range(len(stores_sheet.col_values(6))):
    thing = stores_sheet.col_values(6)[i]
    #print(type(thing))
    #print(thing)
    if validators.url(thing):
        thing_sheet = reader.client.open_by_url(thing).sheet1
   
        print(thing_sheet.get_all_records())
        print(len(thing_sheet.col_values(1)))
        for row in range(2, len(thing_sheet.col_values(1))+1):
            item = thing_sheet.row_values(row)
            print("row", row, "item", item)
            wants = str.split(entry[1], " ")
            print("want:", wants)
            if item[0] in wants:
                print("item matches")
                matching_stores.append(stores_sheet.row_values(i+1))
                
                break

f = open("stores.json", "w")
for store in matching_stores:
    store.pop(0)
    print(store)
    for thing in store:
        print(thing)
        f.write(thing + "\n")
    f.write("\n")
f.close()

    


'''
# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
'''