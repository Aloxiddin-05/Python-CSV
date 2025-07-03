import csv

with open("users.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    
    users = []
    for i in reader:
        users.append(i)
        
    top_users_sorted = sorted(users,key=lambda x:x["username"])

    
with open("top_users.csv","w") as csv_file:
    fieldnames = ["rank","username","posts"]
    writer_dict = csv.DictWriter(csv_file,fieldnames=fieldnames)
    
    writer_dict.writeheader()
    
    for i,user in enumerate(top_users_sorted,1):
        writer_dict.writerow({
            "rank":i,
            "username":user["username"],
            "posts":user["posts"]
        })
    
