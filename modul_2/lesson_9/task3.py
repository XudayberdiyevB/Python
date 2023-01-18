"""
Sales_April_2019.csv faylda berilgan ma'lumotlar orqali quyidagilarni bajaring.
a) Macbook Pro Laptop mahsulotdan nechta buyurtma bo'lganini aniqlang.
b) Price Each ustun orqali 300 dan katta bo'lgan buyurtmalarni txt faylga yozing.
c) 04/10/19 sanadan keyingi buyurmalarni boshqa csv faylga yozing
"""
import csv

from Python.modul_2.exceptions import write_exceptions


def get_full_info():
    full_info = []
    try:
        with open("Sales_April_2019.csv") as files:
            f = csv.DictReader(files)
            for i in f:
                full_info.append(i)
    except FileNotFoundError as e:
        write_exceptions(e)
    return full_info


def get_Macbook_order():
    info = get_full_info()
    order_number = 0
    for i in info:
        if i.get("Product") == "Macbook Pro Laptop":
            try:
                int(i.get("Quantity Ordered"))
            except ValueError as e:
                write_exceptions(e)
            else:
                order_number += int(i.get("Quantity Ordered"))
    return f"Macbook order number > {order_number}"


def get_price():
    info = get_full_info()
    try:
        with open("price_each.txt", "w") as file:
            for i in info:
                try:
                    float(i.get("Price Each"))
                except ValueError as e:
                    write_exceptions(e)
                else:
                    if float(i.get("Price Each")) > 300.0:
                        file.write(f"{i.get('Product')} >> Price >> {i.get('Price Each')}\n")

    except FileNotFoundError as e:
        write_exceptions(e)


def get_order_date():
    info = get_full_info()
    result = []
    data = "04/10/19"
    for i in info:
        if i.get("Order Date") > data:
            result.append(i)
    return result


def write_order_date():
    order_date = [i for i in get_order_date()]
    columns = [i for i in order_date[0]]
    try:
        with open("order_date.csv", "w", newline="") as files:
            writer = csv.DictWriter(files, fieldnames=columns)
            writer.writeheader()
            writer.writerows(order_date)
    except FileNotFoundError as e:
        write_exceptions(e)
    return files
