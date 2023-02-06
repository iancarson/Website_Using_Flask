'''
It handles the Post method for the Deposit html page.
'''
from db import Transaction
from flask import flash, redirect, render_template


class DepositForm:
    def __init__(self, data=None):
        self.data = data
        self.cleaned_data = {}
        self.errors = {}

    def is_valid(self):
        # Check if the amount is valid
        try:
            self.cleaned_data['amount'] = float(self.data['amount'])
        except ValueError:
            self.errors['amount'] = 'Amount is not valid!'
            return False
        return True


def deposit(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            # Get the data from the form
            user = request.user
            amount = form.cleaned_data['amount']
            # Update the user's balance
            user.balance += amount
            user.save()
            # Create the transaction
            transaction = Transaction(sender=None, receiver=user, amount=amount)
            transaction.save()
            # Show the success message
            flash('Deposit successful!', 'success')
            #messages.success(request, 'Deposit successful!')
            return redirect('deposit')
    else:
        form = DepositForm()
    return render_template('deposit.html', form=form)