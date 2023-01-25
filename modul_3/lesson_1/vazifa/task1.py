import csv
from Python.python_exceptions import write_exceptions


class Department:
    def __init__(self, csv_file_1, csv_file_2):
        self.csv_file_1 = csv_file_1
        self.csv_file_2 = csv_file_2

    def get_full_info(self):
        department_information = []
        employee_information = []
        try:
            with open(self.csv_file_1) as files:
                file = csv.DictReader(files)
                for i in file:
                    department_information.append(i)
        except FileNotFoundError as e:
            write_exceptions(e)

        try:
            with open(self.csv_file_2) as files_2:
                file_2 = csv.DictReader(files_2)
                for j in file_2:
                    employee_information.append(j)
        except FileNotFoundError as e:
            write_exceptions(e)
        return department_information, employee_information

    def get_result(self):
        info_1 = self.get_full_info()[0]
        info_2 = self.get_full_info()[1]
        calendar = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December",
        }
        result = [["Employee ID", "DOB", "DOJ", "Department_Name"]]
        id = []
        department_id = []
        dob = []
        dob_res = []
        doj = []
        doj_res = []

        for i in info_2:
            department_id.append(i.get("Department_ID"))
            id.append(i.get("Employee ID"))
            dob.append(i.get("DOB").split("T")[0])
            doj.append(i.get("DOJ").split("T")[0])

        for i in dob:
            r = ""
            r += i.split("-")[0]
            r += " " + i.split("-")[1].replace(f"{i.split('-')[1]}", f"{calendar.get(i.split('-')[1])}")
            r += " " + i.split("-")[2]
            dob_res.append(r)

        for i in doj:
            r = ""
            r += i.split("-")[0]
            r += " " + i.split("-")[1].replace(f"{i.split('-')[1]}", f"{calendar.get(i.split('-')[1])}")
            r += " " + i.split("-")[2]
            doj_res.append(r)

        for i in range(len(id)):
            for j in info_1:
                if department_id[i] == j.get("Department_ID"):
                    result.append([f'{id[i]},{dob_res[i]},{doj_res[i]},{j.get("Department_Name")}'])
                    break

        return result

    def get_writer_new_csv(self):
        res = self.get_result()
        print(res)
        try:
            with open("employee_department_example.csv", "w") as files:
                file = csv.writer(files)
                file.writerows(res)
        except FileNotFoundError as e:
            write_exceptions(e)


obj = Department("Department_Information.csv", "Employee_Information.csv")
obj.get_writer_new_csv()
