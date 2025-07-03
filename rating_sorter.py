import csv
from pprint import pprint

with open("students.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    
    students = []
    for i in reader:
        students.append(i)
        
    sorted_students = sorted(students,key=lambda x:int(x["score"]),reverse=True)
    
with open("rating.csv","w") as csv_file:
    fieldnames = ["rank","name","score"]
    dict_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    
    dict_writer.writeheader()
    
    for i,student in enumerate(sorted_students,1):
        dict_writer.writerow({
            "rank":i,
            "name":student["name"],
            "score":student["score"]
        })