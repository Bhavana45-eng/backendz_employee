class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}"

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, position, salary):
        if emp_id in self.employees:
            print(f"Employee with ID {emp_id} already exists.")
        else:
            employee = Employee(emp_id, name, position, salary)
            self.employees[emp_id] = employee
            print(f"Employee {name} added successfully.")

    def display_employee(self, emp_id):
        if emp_id in self.employees:
            print(self.employees[emp_id])
        else:
            print(f"Employee with ID {emp_id} not found.")

    def update_employee(self, emp_id, name=None, position=None, salary=None):
        if emp_id in self.employees:
            employee = self.employees[emp_id]
            if name:
                employee.name = name
            if position:
                employee.position = position
            if salary:
                employee.salary = salary
            print(f"Employee {emp_id} updated successfully.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Employee {emp_id} deleted successfully.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def list_employees(self):
        if self.employees:
            for emp in self.employees.values():
                print(emp)
        else:
            print("No employees in the system.")

# Sample interaction with the system
if __name__ == "__main__":
    system = EmployeeManagementSystem()

    # Adding employees
    system.add_employee(1, "Alice", "Developer", 70000)
    system.add_employee(2, "Bob", "Manager", 90000)

    # Displaying a specific employee
    system.display_employee(1)

    # Listing all employees
    print("\nAll employees:")
    system.list_employees()

    # Updating an employee
    system.update_employee(1, salary=75000)

    # Deleting an employee
    system.delete_employee(2)

    # Listing all employees after deletion
    print("\nAll employees after deletion:")
    system.list_employees()
