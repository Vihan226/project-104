# list of elements to calculate mean
import csv;
from collections import Counter;

with open('data.csv', newline="") as f:
    reader=csv.reader(f)

    file_data=list(reader)


file_data.pop(0)
#print(file_data)
#sorting data to get the height of people
new_data= []
for i in range(len(file_data)):
    n_number=file_data[i][1]
    new_data.append(float(n_number))

#getting the mean
n=len(new_data)
total=0
for x  in new_data:
    total += x

mean=total/n

print("Mean/Average is :- "+str(mean)) 