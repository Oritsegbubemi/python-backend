# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 21:58:28 2021

@author: Gbubemi
"""

class Budget:
    """Instantiate objects based on different budget categories."""

    def __init__(self, name):
        """Initialize the category."""
        self.name = name
        self.ledger = list()
        self.funds = 0


    def deposit(self, amount):
        """Method to deposit a certain amount."""
        self.ledger.append({"amount": amount})
        self.funds += amount


    def withdraw(self, amount):
        """Method to withdraw a certain amount."""
        if self.check_funds(amount):
            amount *= -1
            self.ledger.append({"amount": amount})
            self.funds += amount
            return True
        else:
            return False


    def get_balance(self):
        """Method to returns current balance."""
        return self.funds


    def transfer(self, amount, budget_category):
        """Method to transfer money from one category to another."""
        if self.check_funds(amount):
            amount *= -1
            self.ledger.append({"amount": amount, "description": f"Transfer to {budget_category.name}"})
            budget_category.ledger.append({"amount": amount * -1, "description": f"Transfer from {self.name}"})
            self.funds += amount
            budget_category.funds -= amount
            return True
        else:
            return False


    def check_funds(self, amount):
        """Method to check if funds are available for certain amount."""
        if amount < self.funds:
            return True
        else:
            return False

        
food = Budget("Food")
food.deposit(500)
food.withdraw(200)
print(food.get_balance())



        