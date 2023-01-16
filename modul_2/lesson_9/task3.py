"""
Sales_April_2019.csv faylda berilgan ma'lumotlar orqali quyidagilarni bajaring.
a) Macbook Pro Laptop mahsulotdan nechta buyurtma bo'lganini aniqlang.
b) Price Each ustun orqali 300 dan katta bo'lgan buyurtmalarni txt faylga yozing.
c) 04/10/19 sanadan keyingi buyurmalarni boshqa csv faylga yozing
"""
import csv
full_info = []
with open("Sales_April_2019.csv") as files:
    read_file = csv.DictReader(files)
    # read_file.__next__()
    for i in read_file:
        print(i)
        full_info.append(i)

# for i in full_info:
#     if i.get("Product") == "Macbook Pro Laptop":
#         print(i)
#         # print(i.get("Purchase Address"))