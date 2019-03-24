import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('mlh hackAbull AttendanceSheet-e713af6542e0.json', scope)
client = gspread.authorize(credentials)

# Find a workbook by name and open the first sheet
sheet = client.open('Attendance Sheet').sheet1
# Find a workbook by key and open the first sheet
##sht = client.open_by_key('0BmgG6nO_6dprdS1MN3d3MkdPa142WFRrdnRRUWl1UFE')

# Extract and print all of the values
"""
list_of_hashes = sheet.get_all_records() #Dictionary
print(list_of_hashes)
"""
allfile_data = sheet.get_all_values()

nameOfStudent = "Leonardo Dicaprio" ##this a variable will change to hold the actual student

print ("Number of records: " + str(len(allfile_data)))

for x in range(1, len(allfile_data)):
    #print(allfile_data[x][0])
    if allfile_data[x][0] == nameOfStudent:
        sheet.update_cell(x+1, 4, "HERE")
        print ("   Marked " + allfile_data[x][0] + "as present.")
