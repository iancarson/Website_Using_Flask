import io
import csv
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.##
        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)

        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not
        # ucid - sl248 - 12/03/2022
        if file.filename.lower().endswith(('.csv')) == False:
            # Code should check if the file is a .csv file otherwise reject with a flash
            flash('Selected file is not a .csv', "warning")
            return redirect(request.url)

        if file and secure_filename(file.filename):
            companies = []
            employees = []
            company_query = """
            INSERT INTO IS601_MP2_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE address = %(address)s, city = %(city)s, country=%(country)s, state=%(state)s, zip=%(zip)s, website=%(website)s 
            """
            employee_query = """
            INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, last_name = %(last_name)s, email = %(email)s, company_id = (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            # TODO importcsv-2 read the csv file stream as a dict
            # ucid - sl248 - 12/03/2022
            reader = csv.DictReader(stream)
            for row in reader:
                # print(row) #example
                # TODO importcsv-3 extract company data and append to company list as a dict only with company data
                # ucid - sl248 - 12/03/2022
                company = {
                    "name": row['company_name'],
                    "address": row['address'],
                    "city": row['city'],
                    "country": row['country'],
                    "state": row['state'],
                    "zip": row['zip'],
                    "website": row['web'],
                }
                if row["company_name"]  != '' and row["address"]  != '' and row["city"]  != '' and row["state"]  != '' and row["country"]  != '':
                    companies.append(company)
                # TODO importcsv-4 extract employee data and append to employee list as a dict only with employee data
                # ucid - sl248 - 12/03/2022
                employee = {
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "email": row['email'],
                    "company_name": row['company_name'],
                }
                if row["first_name"] != '' and row["last_name"] != '' and row["email"] != '':
                    employees.append(employee)
            
            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    # TODO importcsv-5 display flash message about number of companies inserted
                    # ucid - sl248 - 12/03/2022
                    if result.status == True:
                        companies_count_query = """SELECT COUNT(id) FROM `IS601_MP2_Companies`"""
                        flash(f"Inserted or updated {len(companies)} companies", "success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no companies were loaded
                # ucid - sl248 - 12/03/2022
                flash("No companies were loaded", "info")
            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    # TODO importcsv-7 display flash message about number of employees loaded
                    # ucid - sl248 - 12/03/2022
                    if result.status == True:
                        employees_count_query = """SELECT COUNT(id) FROM `IS601_MP2_Employees`"""
                        flash(f"Inserted or updated {len(employees)} employees", "success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-8 display flash message (info) that no companies were loaded
                # ucid - sl248 - 12/03/2022
                flash("No employees were loaded", "info")
    return render_template("upload.html")
