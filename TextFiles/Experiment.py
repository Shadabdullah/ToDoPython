# import time
#
# now: str = time.strftime("%d-%m-%y")
# print(now)
#
# # Glob module : it return list of file with matching pattern
#
# import glob
#
# myfiles = glob.glob("*.txt")
#
# for filepath in myfiles:
#     with  open(filepath,'r') as file:
#         print(file.read())


# csv: module

# import  csv
#
# with open('station.csv','r') as file:
#     data = list (csv.reader(file))
#
#     print(data)



import webbrowser

search = input("Enter what you want to search : ").replace(" ","+")

webbrowser.open(f"https://www.google.com/search?q={search}")











# shutil module :

import shutil

data = shutil.make_archive("output","zip","../TextFiles")

