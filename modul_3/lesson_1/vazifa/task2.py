import csv
from Python.python_exceptions import write_exceptions


class Account:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def get_info(self):
        result = []
        try:
            with open(self.csv_file) as files:
                file = csv.DictReader(files)
                for i in file:
                    result.append(i)
        except FileNotFoundError as e:
            write_exceptions(e)
        return result

    def get_write_new_csv(self):
        info = self.get_info()
        header = self.get_info()[0]
        for i in info:
            if i.get("Country/Continent") == "United States":
                try:
                    with open("United States account.csv", "a") as files:
                        file = csv.DictWriter(files, header)
                        file.writeheader()
                        file.writerow(i)
                except FileNotFoundError as e:
                    write_exceptions(e)
            if i.get("Country/Continent") == "India":
                try:
                    with open("India account.csv", "a") as files:
                        file = csv.DictWriter(files, header)
                        file.writeheader()
                        file.writerow(i)
                except FileNotFoundError as e:
                    write_exceptions(e)

            if i.get("Country/Continent") == "Portugal":
                try:
                    with open("Portugal account.csv", "a") as files:
                        file = csv.DictWriter(files, header)
                        file.writeheader()
                        file.writerow(i)
                except FileNotFoundError as e:
                    write_exceptions(e)
            if i.get("Country/Continent") == "Argentina":
                try:
                    with open("Argentina account.csv", "a") as files:
                        file = csv.DictWriter(files, header)
                        file.writeheader()
                        file.writerow(i)
                except FileNotFoundError as e:
                    write_exceptions(e)
            if i.get("Country/Continent") == "Canada":
                try:
                    with open("Canada account.csv", "a") as files:
                        file = csv.DictWriter(files, header)
                        file.writeheader()
                        file.writerow(i)
                except FileNotFoundError as e:
                    write_exceptions(e)
            if i.get("Country/Continent") == "Trinidad and Tobago United States":
                try:
                    with open("Trinidad and Tobago United States account.csv", "a") as files:
                        file = csv.DictWriter(files, header)
                        file.writeheader()
                        file.writerow(i)
                except FileNotFoundError as e:
                    write_exceptions(e)
            if i.get("Country/Continent") == "Canada":
                try:
                    with open("Canada account.csv", "a") as files:
                        file = csv.DictWriter(files, header)
                        file.writeheader()
                        file.writerow(i)
                except FileNotFoundError as e:
                    write_exceptions(e)
            if i.get("Country/Continent") == "Brazil":
                try:
                    with open("Brazil account.csv", "a") as files:
                        file = csv.DictWriter(files, header)
                        file.writeheader()
                        file.writerow(i)
                except FileNotFoundError as e:
                    write_exceptions(e)


obj = Account("List of most-followed Instagram accounts.csv")
obj.get_write_new_csv()
