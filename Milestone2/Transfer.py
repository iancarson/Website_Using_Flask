
from docarray.array.queryset.lookup import Q
from rich.markup import render
from sqlalchemy.engine import Transaction
from Milestone1.auth.models import User
#Import messages from Flask
from flask import Flask, render_template, request, redirect, url_for, flash, session, abort

class TransferFundsForm:
    def __init__(self, data=None):
        self.data = data
        self.cleaned_data = {}
        self.errors = {}

    def is_valid(self):
        # Check if the receiver exists
        try:
            self.cleaned_data['receiver'] = User.objects.get(username=self.data['receiver'])
        except User.DoesNotExist:
            self.errors['receiver'] = 'Receiver does not exist!'
            return False
        # Check if the amount is valid
        try:
            self.cleaned_data['amount'] = float(self.data['amount'])
        except ValueError:
            self.errors['amount'] = 'Amount is not valid!'
            return False
        return True




def transferFunds(request):
    if request.method == 'POST':
        form = TransferFundsForm(request.POST)
        if form.is_valid():
            # Get the data from the form
            sender = request.user
            receiver = form.cleaned_data['receiver']
            amount = form.cleaned_data['amount']
            # Check if the sender has enough money
            if sender.balance >= amount:
                # Update the sender's balance
                sender.balance -= amount
                sender.save()
                # Update the receiver's balance
                receiver.balance += amount
                receiver.save()
                # Create the transaction pair
                transaction = Transaction(sender=sender, receiver=receiver, amount=amount)
                transaction.save()
                # Show the success message
                flash('Transfer successful!', 'success')
                #messages.success(request, 'Transfer successful!')
                return redirect('transferFunds')
            else:
                # Show the error message
                flash('You do not have enough money!', 'error')
                #messages.error(request, 'Insufficient balance!')
                return redirect('transferFunds')
    else:
        form = TransferFundsForm()
    return render_template('transfer.html', form=form)

'''
Render the transaction history page'''
def transactionHistory(request):
    # Get the transactions
    transactions = Transaction.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
    return render_template('transactionPage.html', transactions=transactions)

'''
The message framework is used to show the user-friendly messages.
'''
