"""
netflix_titles.csv ushbu faylda Netflix kinolari malumotlari mavjud, quyidagi vazifalarni bajaring:
a) release_year da 2020 va 2021 yildagi kinolar ma'lumotlari bilan birga alohida csv faylga yozing
b) listed_in ustunidan Comedies bo'lgan filmlarni alohida csv faylga yozing.
c) type Movie va country United States bo'lgan filmalarni alohida csv faylga yozing.
"""
import csv
from Python.modul_2.exceptions import write_exceptions


class Netflix:
    def __init__(self, file_csv):
        self.file_csv = file_csv

    def get_file_scv(self):
        result = []
        try:
            with open(self.file_csv, encoding="utf8") as files:
                file = csv.DictReader(files)
                for i in file:
                    result.append(i)
        except FileNotFoundError as e:
            write_exceptions(e)
        return result

    def info_file_csv(self):
        info = self.get_file_scv()
        lst = ["2020", "2021"]
        listed_in = []
        release_year = []
        movie_united = []
        for i in info:
            if i.get("release_year") in lst:
                release_year.append(i)
            if "Comedies" in i.get("listed_in"):
                listed_in.append(i)
            if i.get("type") == "Movie" and "United States" in i.get("country"):
                movie_united.append(i)

        return release_year, listed_in, movie_united

    def write_release_year(self):
        column = [i for i in self.get_file_scv()[0]]
        info = self.info_file_csv()[0]
        try:
            with open("release_year.csv", "w", newline="", encoding="utf8") as files:
                file = csv.DictWriter(files, column)
                file.writeheader()
                file.writerows(info)
        except FileNotFoundError as e:
            write_exceptions(e)
        return file

    def write_listed_in(self):
        column = [i for i in self.get_file_scv()[0]]
        comedies = self.info_file_csv()[1]
        try:
            with open("listed_in.csv", "w", encoding="utf8", newline="") as files:
                file = csv.DictWriter(files, column)
                file.writeheader()
                file.writerows(comedies)
        except FileNotFoundError as e:
            write_exceptions(e)

    def write_movie_united(self):
        column = [i for i in self.get_file_scv()[0]]
        movie_united = self.info_file_csv()[2]
        try:
            with open("movie_united.csv", "w", encoding="utf8", newline="") as files:
                file = csv.DictWriter(files, column)
                file.writeheader()
                file.writerows(movie_united)
        except FileNotFoundError as e:
            write_exceptions(e)
        return file


obj = Netflix("netflix_titles.csv")
obj.write_listed_in()
obj.write_release_year()
obj.write_movie_united()
