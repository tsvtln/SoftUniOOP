from typing import List

from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def __object_grep(self, provided_id, class_name):
        # Assuming class_name is the actual class, not a string
        object_grep = next((obj for obj in getattr(self, class_name) if obj.client_id == provided_id), None)
        return object_grep

    def add_loan(self, loan_type: str):
        if loan_type != 'StudentLoan' and loan_type != 'MortgageLoan':
            raise Exception("Invalid loan type!")
        # loan = eval(f"{loan_type}()")
        if loan_type == 'StudentLoan':
            loan = StudentLoan()
        else:
            loan = MortgageLoan()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in ['Student', 'Adult']:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        if client_type == 'Student':
            client = Student(client_name, client_id, income)
        else:
            client = Adult(client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        # find if client is student or adult and check if the loan type is correct
        client_object = self.__object_grep(client_id, "Student")
        if client_object is not None:
            if loan_type != 'StudentLoan':
                raise Exception("Inappropriate loan type!")
            loan = next((obj for obj in getattr(self, self.loans) if obj == StudentLoan), None)
            client_object.loans.append(loan)
            self.loans.remove(loan)
            return f"Successfully granted {loan_type} to {client_object.client_name} with ID {client_object.client_id}."

        if client_object is None:
            client_object_2 = self.__object_grep(client_id, "Adult")
            if loan_type != 'MortgageLoan':
                raise Exception("Inappropriate loan type!")
            loan = next((obj for obj in getattr(self, self.loans) if obj == MortgageLoan), None)
            client_object_2.loans.append(loan)
            self.loans.remove(loan)
            return (f"Successfully granted {loan_type} to {client_object_2.client_name} with ID "
                    f"{client_object_2.client_id}.")

    def remove_client(self, client_id: str):
        pass

    def increase_loan_interest(self, loan_type: str):
        pass

    def increase_clients_interest(self, min_rate: float):
        pass

    def get_statistics(self):
        pass
