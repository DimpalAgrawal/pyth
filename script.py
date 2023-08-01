
# program to copy the data from one csv file to another cv file in python in  file handling
# import csv
# with open("command.csv", "r") as fp1:
#     with open("sample.csv", "w", newline='') as fp2:
#         Rs = csv.reader(fp1)
#         wp = csv.writer(fp2, delimiter=',')
#         for i in Rs:
#             wp.writerow(i)
# print("File Created") 


#  progarm to swap the columns in the table
# import csv
# with open("command.csv", "r") as fp1:
#     with open("sample.csv" , "w", newline='') as fp2:
#         Rs = csv.reader(fp1)
#         wp =  csv.writer(fp2, delimiter=',')
#         for i  in Rs:
#             wp.writerow([i[1], i[2], i[3],i[0]])
# print("file Swap")


# program to change the series in the key_value pair

# import csv

# import sys
# sys.stdout = open("dict.csv" ,"w")


# fp = open("command.csv", "r") 
# csvDictReader = csv.DictReader(fp)
# for i in csvDictReader:
#   print(i)


import csv

csv_filename = 'my_file.csv'

with open('command.csv') as f_input:
    # read the current csv file
    reader = csv.reader(f_input)
    fields = next(reader)
    my_dictionary = dict.fromkeys(fields)

    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []
    for row in reader:
        col_1.append(row[0])
        col_2.append(row[1])
        col_3.append(row[2])
        col_4.append(row[3])

    my_dictionary[fields[0]] = col_1
    my_dictionary[fields[1]] = col_2
    my_dictionary[fields[2]] = col_3
    my_dictionary[fields[3]] = col_4
    print(my_dictionary)
    
    
    
# Split the string into list of strings

# Input : Geeks for Geeks
# Output : ['Geeks', 'for', 'Geeks']


# string = "Geeks for Geeks"
# str =  string.split(' ')
# print(str)



# Join the list of strings into a string based on delimiter ('-')


# Input :  ['Geeks', 'for', 'Geeks']
# Output : Geeks-for-Geeks


string =  ['Geeks', 'for', 'Geeks']
print("-".join(string))
