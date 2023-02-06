'''
Create a User Account.
'''
import string
from datetime import datetime
from random import random


class Account:
    # Account class with the following attributes:A unique 12 digit account number
    # Account type (checking, savings, world)
    # Account balance
    # Date created
    # Date modified
    # User associated with the account
    def __init__(self, user, account_type):
        self.user = user
        self.account_type = account_type
        self.account_number = self.generate_account_number()
        self.balance = 0
        self.date_created = datetime.datetime.now()
        self.date_modified = datetime.datetime.now()

    def generate_account_number(self):
        # Generate a random 12 digit/character value
        # must regenerate if a duplicate collision occurs
        return ''.join(random.choice(string.digits) for _ in range(12))