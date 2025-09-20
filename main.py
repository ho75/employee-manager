import csv
import os

class EmployeeManager:
    def __init__(self, filename="employees.csv"):
        self.filename = filename
        self.employees = {}
        self.load_data()

   #load data at csv file
    def load_data(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, mode="r", newline="") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        self.employees[row["ID"]] = row
            else:
                with open(self.filename, mode="w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Position", "Salary", "Email"])
                    writer.writeheader()
        except Exception as e:
            print(f"Error while loading data: {e}")
#save data at csv file
    def save_data(self):

        try:
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Position", "Salary", "Email"])
                writer.writeheader()
                for emp in self.employees.values():
                    writer.writerow(emp)
        except Exception as e:
            print(f"⚠Error while saving data: {e}")
#add employee
    def add_employee(self):
        try:
            emp_id = input("Enter Employee ID: ").strip()
            if emp_id in self.employees:
                print("Employee with this ID already exists.")
                return

            name = input("Enter Name: ").strip()
            position = input("Enter Position: ").strip()
            salary = input("Enter Salary: ").strip()
            email = input("Enter Email: ").strip()

            if not salary.isdigit():
                raise ValueError("Salary must be numeric.")
            if "@" not in email:
                raise ValueError("Invalid email format.")

            self.employees[emp_id] = {
                "ID": emp_id,
                "Name": name,
                "Position": position,
                "Salary": salary,
                "Email": email
            }
            self.save_data()
            print("Employee added successfully.")
        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"Unexpected error while adding employee: {e}")
#view all employees
    def view_employees(self):
        try:
            if not self.employees:
                print("No employees found.")
                return
            print("\n--- Employee List ---")
            for emp in self.employees.values():
                print(f"ID: {emp['ID']}, Name: {emp['Name']}, Position: {emp['Position']}, Salary: {emp['Salary']}, Email: {emp['Email']}")
        except Exception as e:
            print(f"Error while viewing employees: {e}")
# update employee
    def update_employee(self):
        try:
            emp_id = input("Enter Employee ID to update: ").strip()
            if emp_id not in self.employees:
                print(" Employee not found.")
                return

            emp = self.employees[emp_id]
            print("Leave blank to keep old value.")

            name = input(f"Enter new Name ({emp['Name']}): ").strip()
            position = input(f"Enter new Position ({emp['Position']}): ").strip()
            salary = input(f"Enter new Salary ({emp['Salary']}): ").strip()
            email = input(f"Enter new Email ({emp['Email']}): ").strip()

            if name: emp["Name"] = name
            if position: emp["Position"] = position
            if salary:
                if salary.isdigit():
                    emp["Salary"] = salary
                else:
                    print("Salary must be numeric. Skipped.")
            if email:
                if "@" in email:
                    emp["Email"] = email
                else:
                    print("Invalid email. Skipped.")

            self.save_data()
            print("Employee updated successfully.")
        except Exception as e:
            print(f"Error while updating employee: {e}")
# delete employee
    def delete_employee(self):
        try:
            emp_id = input("Enter Employee ID to delete: ").strip()
            if emp_id in self.employees:
                del self.employees[emp_id]
                self.save_data()
                print("Employee deleted successfully.")
            else:
                print("Employee not found.")
        except Exception as e:
            print(f"Error while deleting employee: {e}")
# search for spesific employee
    def search_employee(self):
        try:
            emp_id = input("Enter Employee ID to search: ").strip()
            if emp_id in self.employees:
                emp = self.employees[emp_id]
                print(f"ID: {emp['ID']}, Name: {emp['Name']}, Position: {emp['Position']}, Salary: {emp['Salary']}, Email: {emp['Email']}")
            else:
                print("Employee not found.")
        except Exception as e:
            print(f"Error while searching for employee: {e}")

    def menu(self):
        while True:
            try:
                print("\n--- Employee Data Management ---")
                print("1. Add Employee")
                print("2. View All Employees")
                print("3. Update Employee")
                print("4. Delete Employee")
                print("5. Search Employee")
                print("6. Exit")

                choice = input("Enter choice (1-6): ").strip()
                if choice == "1":
                    self.add_employee()
                elif choice == "2":
                    self.view_employees()
                elif choice == "3":
                    self.update_employee()
                elif choice == "4":
                    self.delete_employee()
                elif choice == "5":
                    self.search_employee()
                elif choice == "6":
                    print("Exiting program...")
                    break
                else:
                    print("Invalid choice. Please enter 1-6.")
            except Exception as e:
                print(f"Unexpected error in menu: {e}")


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
