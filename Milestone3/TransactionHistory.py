
import datetime
from flask import Flask, render_template
from flask_paginate import Pagination, get_page_parameter
from django.db.models import Q
from sqlalchemy.engine import Transaction
from Milestone1.auth.models import User


class TransactionHistoryForm:
    def __init__(self, data):
        self.data = data
        self.errors = {}
        self.cleaned_data = {}
        self.is_valid()

    def is_valid(self):
        # Check if the start date is valid
        try:
            self.cleaned_data['start_date'] = datetime.strptime(self.data['start_date'], '%Y-%m-%d')
        except (KeyError, ValueError):
            pass
        # Check if the end date is valid
        try:
            self.cleaned_data['end_date'] = datetime.strptime(self.data['end_date'], '%Y-%m-%d')
        except (KeyError, ValueError):
            pass
        # Check if the transaction type is valid
        if self.data['transaction_type'] in ['deposit', 'withdraw', 'transfer']:
            self.cleaned_data['transaction_type'] = self.data['transaction_type']
        return True


def transactionHistory(request):
    # Get the transactions
    transactions = Transaction.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
    # Create the form
    form = TransactionHistoryForm(request.GET)
    if form.is_valid():
        # Get the data from the form
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        transaction_type = form.cleaned_data['transaction_type']
        # Filter the transactions
        if start_date:
            transactions = transactions.filter(date__gte=start_date)
        if end_date:
            transactions = transactions.filter(date__lte=end_date)
        if transaction_type:
            transactions = transactions.filter(type=transaction_type)
    page = request.args.get(get_page_parameter(), type=int, default=1)
    # Paginate the transactions
    transactions = Pagination(page=page, total=User.count(),  record_name='transactions', per_page=10)
    return render_template('TransactionPage.html', transactions=transactions, form=form)