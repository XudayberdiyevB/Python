"""
worldometer_data.csv faylda Covid19 davlatlardagi holatlar keltirilgan quyidagi vazifalarni bajaring.
a) TotalCases ustunda 100000 va 1000000 orasidagi holatlarni alohida csv faylga yozing.
b) Country/Region dagi davlatlarni kiritiganda ActiveCases qiymatini qaytarish uchun funksiya yarating.
c) Continent dagi mintaqa kiritiganda umumiy TotalCases qaytini qaytarish uchun funksiya yarating.
"""
import csv
from pprint import pprint

from Python.modul_2.exceptions import write_exceptions


class Worldometer:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def get_file_scv(self):
        info = []
        try:
            with open(self.csv_file, "r", encoding="utf8") as files:
                file = csv.DictReader(files)
                for i in file:
                    info.append(i)
        except FileNotFoundError as e:
            write_exceptions(e)
        return info

    def get_total_cases(self):
        file = self.get_file_scv()
        total_cases = []
        header = [i for i in file[0]]
        for i in file:
            if 100000 < int(i.get("TotalCases")) < 1000000:
                total_cases.append(i)
        try:
            with open("total_cases.csv", "w", encoding="utf8", newline="") as files:
                f = csv.DictWriter(files, header)
                f.writeheader()
                f.writerows(total_cases)
        except FileNotFoundError as e:
            write_exceptions(e)
        return total_cases

    def get_active_cases(self, value):
        info = self.get_file_scv()
        result = ""
        for i in info:
            if i.get("Country/Region") == value:
                result = i.get("ActiveCases")
        return f"{value} ActiveCases -->> {result}"

    def get_continent(self, value):
        info = self.get_file_scv()
        result = []
        for i in info:
            if i.get("Continent") == value:
                result.append(f"{i.get('Country/Region')} TotalCases -->> {i.get('TotalCases')}")
        return result


obj = Worldometer("worldometer_data.csv")
obj.get_total_cases()
obj.get_active_cases("Uzbekistan")
obj.get_continent("Asia")
