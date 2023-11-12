from typing import List

from project.trainer import Trainer
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer) if customer not in self.customers else None

    def add_trainer(self, trainer: Trainer):
        self.trainers.append(trainer) if trainer not in self.trainers else None

    def add_equipment(self, equipment: Equipment):
        self.equipment.append(equipment) if equipment not in self.equipment else None

    def add_plan(self, plan: ExercisePlan):
        self.plans.append(plan) if plan not in self.plans else None

    def add_subscription(self, subscription: Subscription):
        self.subscriptions.append(subscription) if subscription not in self.subscriptions else None

    def subscription_info(self, subscription_id: int):
        subscription_grep_id = next((obj for obj in self.subscriptions if obj.id == subscription_id), None)
        customer_id = subscription_grep_id.customer_id
        customer_grep_id = next((obj for obj in self.customers if obj.id == customer_id), None)
        trainer_id = subscription_grep_id.trainer_id
        trainer_grep_id = next((obj for obj in self.trainers if obj.id == trainer_id), None)
        exercise_id = subscription_grep_id.exercise_id
        exercise_grep = next((obj for obj in self.plans if obj.id == exercise_id), None)
        equipment_id = exercise_grep.equipment_id
        equipment_grep_id = next((obj for obj in self.equipment if obj.id == equipment_id), None)
        plan_id = exercise_grep.id
        plan_grep_id = next((obj for obj in self.plans if obj.id == plan_id), None)
        # to_print = [repr(subscription_grep_id), repr(customer_id), repr(trainer_id),
        # repr(equipment_id), repr(plan_id)]
        # print(f' test print\n sub_grep_id: {subscription_grep_id} \n cust_id: {customer_id} \n train_id: {trainer_id}'
        #       f'\n exercise_id: {exercise_id}\n exercise_grep: {exercise_grep}\n
        #       equ_id: {equipment_id} \n plan_id: {plan_id}')
        to_print = [repr(subscription_grep_id),
                    repr(customer_grep_id),
                    repr(trainer_grep_id),
                    repr(equipment_grep_id),
                    repr(plan_grep_id)]
        return '\n'.join(to_print)
