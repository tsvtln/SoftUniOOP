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
        # client_object = self.__object_grep(client_id, "Student")
        client_object = [c for c in self.clients if c.client_id == client_id][0]
        if (loan_type == 'StudentLoan' and client_object.__class__.__name__ == 'Student') or \
                (loan_type == "MortgageLoan" and client_object.__class__.__name__ == 'Adult'):
            loan = [l for l in self.loans if l.__class__.__name__ == loan_type][0]
            self.loans.remove(loan)
            client_object.loans.append(loan)
            return f"Successfully granted {loan_type} to {client_object.name} with ID {client_id}."
        else:
            raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        try:
            client_object = [c for c in self.clients if c.client_id == client_id][0]
        except IndexError:
            raise Exception("No such client!")
        if client_object.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client_object)
        return f"Successfully removed {client_object.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        cnt = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                cnt += 1
        return f"Successfully changed {cnt} loans."

    def increase_clients_interest(self, min_rate: float):
        cnt = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                cnt += 1
        return f"Number of clients affected: {cnt}."

    def get_statistics(self):
        total_clients_income = sum([c.income for c in self.clients])
        loans_count_granted_to_clients = sum([len(c.loans) for c in self.clients])
        granted_sum = sum([l.amount for c in self.clients for l in c.loans])
        not_granted_sum = sum([l.amount for l in self.loans])

        try:
            avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients)
        except ZeroDivisionError:
            avg_client_interest_rate = 0

        result = f"Active Clients: {len(self.clients)}\n"
        result += f"Total Income: {total_clients_income:.2f}\n"
        result += f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
        result += f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n"
        result += f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"

        return result
