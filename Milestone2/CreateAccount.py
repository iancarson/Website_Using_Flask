'''
It handles the http request for creating a checking account
'''
from db import Transaction
from flask import flash, redirect

from Milestone2.Account import Account


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