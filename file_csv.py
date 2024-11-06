import csv
import random


# Writing using CSV DictWriter
# fieldname=['Name','Age','Org','Salaries']
# row={'Name':random.choice(['Arshad','Yusuf','Hamida']),'Age':random.randint(30,39),'Org':random.choice(['AWS','Google','FB']),'Salaries':random.randint(10000,20000)}
# with open('Temp.csv', 'w', newline='') as file1:
#     filewriter=csv.DictWriter(file1,fieldnames=fieldname)
#     filewriter.writeheader()


# with open('Temp.csv', 'a', newline='') as file1:
#     filewriter=csv.DictWriter(file1,fieldnames=fieldname)
#     for i in range(10):
#         filewriter.writerow(row)


# Reading Using CSV DictReader

# with open('Temp.csv','r') as file1:
#     csv_reader=csv.DictReader(file1)

#     for line in csv_reader:
#         print(line,end='\n')

# Reading Using Normal File operator

f=open('Temp.csv','r')
# all at once
# print(f.read()) 


# all lines at once in list format
# print(f.readlines()) 

# all lines in parts
# print(f.readline(),end='')
# print(f.readline(),end='')
# for i in f.readlines() :  
#     print(i,end='')

# all lines in parts
# for i in f.read() : 
#     print(i,end='')

# size=10
# line=f.read(size)

# while(len(line) >0):
#     print(line,end='*')
#     line=f.read(size)
# f.close()

print(f.closed)
# numbers=[1,2,3,4,5,5]
# with open('List-NoHeader.csv', 'a') as nums:
#     writer=csv.writer(nums, lineterminator='\n')
#     for i in numbers:
#         writer.writerow([i])