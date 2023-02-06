'''
This class will handle the Post method for the Withdraw page.
For withdraw, add a check to make sure they can’t withdraw more money
than the account has
'''
from db import Transaction
from flask import flash, redirect, render_template


class WithdrawForm:
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


def withdraw(request):
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            # Get the data from the form
            user = request.user
            amount = form.cleaned_data['amount']
            # Check if the user has enough money
            if user.balance >= amount:
                # Update the user's balance
                user.balance -= amount
                user.save()
                # Create the transaction
                transaction = Transaction(sender=user, receiver=None, amount=amount)
                transaction.save()
                # Show the success message
                flash('Withdraw successful!', 'success')
                #messages.success(request, 'Withdraw successful!')
                return redirect('withdraw')
            else:
                # Show the error message
                flash('You do not have enough money!', 'error')
                #messages.error(request, 'Insufficient balance!')
                return redirect('withdraw')
    else:
        form = WithdrawForm()
    return render_template('withdraw.html', form=form)