"""
countries of the world.csv file da berilgan ma'lumotlar orqali quyidagi ma'lumotlarni chiqaring.
a) Population 20 000 000 dan ko'p bo'lgan mamlakatlar ro'yxatini chiqaring.
b) C bilan boshlanadigan davlatlar ro'yxatini txt file ga yozing.
c) GDP 1000 dan baland bo'lganlar ro'yxatini qaytaring.
"""
import csv


class Country:
    def __init__(self, file_):
        self.file = file_

    def get_file(self):
        return self.file

    def get_full_info(self):
        full_info = []
        try:
            with open(self.file) as file:
                reader_file = csv.DictReader(file)
                # reader_file.__next__()
                for row in reader_file:
                    full_info.append(row)
        except FileNotFoundError as e:
            return e
        return full_info

    def get_population(self):
        full_info = self.get_full_info()
        population = []
        for i in full_info:
            if int(i.get("Population")) >= 20000000:
                population.append(i)
        return population

    def get_c_country(self):
        full_info = self.get_full_info()
        c_country = []
        for i in full_info:
            if i.get("Country") == "C":
                c_country.append(i)
        return c_country

    def get_gdp_country(self):
        full_info = self.get_full_info()
        gdp_country = []
        for i in full_info:
            try:
                int(i.get("GDP ($ per capita)"))
            except TypeError as e:
                return e
            else:
                if int(i.get("GDP ($ per capita)").strip()) > 1000:
                    gdp_country.append(i)
        return gdp_country


obj = Country("countries of the world.csv")


def get_file_txt():
    try:
        with open("counrty.txt", "a") as file:
            for i in obj.get_population():
                file.write(str(i))
    except FileNotFoundError as e:
        return e
    return file

obj.get_gdp_country()

