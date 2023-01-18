"""
worldcities.csv faylda berilgan ma'lumotlar orqali quyidagilarni bajaring.
a) Country Uzbekistan bo'lgan shaharlarni txt faylga yozing
b) Uzbekistan shaharlari lat va lng orqali quyidagi ko'rinishdagi
 location=https://my-location.org/?lat=41.284067&lng=69.147750 ma'lumotni txt faylga yozing.
"""

import csv
from Python.modul_2.exceptions import write_exceptions

class Country:
    def __init__(self, file_):
        self.file = file_

    def city_in_txt(self):
        uzbekistan = []
        try:
            with open(self.file, encoding="utf8") as files:
                read_file = csv.DictReader(files)
                for i in read_file:
                    if i.get("country") == "Uzbekistan":
                        uzbekistan.append(i)

        except FileNotFoundError as e:
            write_exceptions(e)
        else:
            with open("uzbekistan.txt", "w+", encoding="utf8") as file:
                for i in uzbekistan:
                    file.writelines(str(f"{i}\n"))
        return uzbekistan

    def city_lat_long(self):
        lst = []
        try:
            with open("task2.txt", "w", encoding="utf8") as f:
                for i in self.city_in_txt():
                    lst.append(f"location=https://my-location.org/?lat={i.get('lat')}&lng={i.get('lng')}")
                for i in lst:
                    f.writelines(f"{i}\n")
        except FileNotFoundError as e:
            write_exceptions(e)
        return lst


obj = Country("worldcities.csv")