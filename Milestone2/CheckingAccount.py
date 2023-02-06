
import string
from datetime import datetime
from random import random

from flask import flash, redirect
from sqlalchemy.engine import Transaction


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

#Load the
def createCheckingAccount(request):
    # Get the user
    user = request.user
    # Check if the user has enough money
    if user.balance >= 5:
        # Update the user's balance
        user.balance -= 5
        user.save()
        # Create the account
        account = Account(user=user, account_type='checking')
        account.save()
        # Create the transaction pair
        transaction = Transaction(sender=user, receiver=account, amount=5, balance_change=-5)
        transaction.save()
        # Show the success message
        flash('Account created successfully!', 'success')
        return redirect('accounts')
    else:
        # Show the error message
        flash('You do not have enough money!', 'error')
        return redirect('accounts')
