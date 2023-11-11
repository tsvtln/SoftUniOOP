from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def obj_extractor(self, customer_id: int, dvd_id: int):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        dvd = next((d for d in self.dvds if d.id == dvd_id), None)
        return customer, dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        # customer_obj = []
        # dvd_obj = []
        # for grep_customer in self.customers:
        #     if grep_customer.id == customer_id:
        #         customer_obj = grep_customer
        #         break
        # for grep_dvd in self.dvds:
        #     if grep_dvd.id == dvd_id:
        #         dvd_obj = grep_dvd
        #         break
        # bace to mojelo s generatori ama dobre 4e e 6efa da kaje
        customer, dvd = self.obj_extractor(customer_id, dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer, dvd = self.obj_extractor(customer_id, dvd_id)
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        to_print = []
        for customer in self.customers:
            to_print.append(repr(customer))
        for dvd in self.dvds:
            to_print.append(repr(dvd))
        return '\n'.join(to_print)




