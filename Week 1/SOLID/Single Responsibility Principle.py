class Employee:
    def __init__(self, name):
        self.name = name


class SalaryService:
    def calculate_salary(self, emp):
        print(f"Salary calculated for {emp.name}")


class EmployeeRepository:
    def save(self, emp):
        print(f"{emp.name} saved to database")


if __name__ == "__main__":
    employee = Employee("Kanisha")

    salary_service = SalaryService()
    employee_repository = EmployeeRepository()

    salary_service.calculate_salary(employee)
    employee_repository.save(employee)