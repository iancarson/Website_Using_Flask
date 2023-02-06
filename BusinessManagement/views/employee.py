from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    # ucid-sl248 , date - 12/3/22
    query = "SELECT employees.id as id, first_name, last_name, email, companies.id as company_id, COALESCE(companies.name, 'N/A' ) as company_name FROM IS601_MP2_Employees employees LEFT JOIN IS601_MP2_Companies companies ON employees.company_id=companies.id"
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = [("first_name", "First Name"), ("last_name", "Last Name"), ("email", "Email"), ("company_name", "Company Name")]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    # ucid-sl248 , date - 12/3/22
    first_name = request.args.get('fn', '' )
    last_name = request.args.get('ln', '' )
    email = request.args.get('email', '' )
    company_id = request.args.get('company', '' )
    column = request.args.get('column', '' )
    order = request.args.get('order', '' )
    limit = request.args.get('limit', '' )
    if first_name != '' or last_name != '' or email != '' or company_id != '':
        query += " WHERE "
    # TODO search-3 append like filter for first_name if provided
    # ucid-sl248 , date - 12/3/22
    if first_name != '':
        first_name = f"%{first_name}%"
        query += " first_name LIKE %s"
        args.append(first_name)
    # TODO search-4 append like filter for last_name if provided
    # ucid-sl248 , date - 12/3/22
    if last_name != '':
        if list(query.split(" "))[-2] != 'WHERE':
            query += "AND"
        last_name = f"%{last_name}%"
        query += " last_name LIKE %s"
        args.append(last_name)
    # TODO search-5 append like filter for email if provided
    # ucid-sl248 , date - 12/3/22
    if email != '':
        if list(query.split(" "))[-2] != 'WHERE':
            query += "AND"
        email = f"%{email}%"
        query += " email LIKE %s"
        args.append(email)
    # TODO search-6 append equality filter for company_id if provided
    # ucid-sl248 , date - 12/3/22
    if company_id != '':
        if list(query.split(" "))[-2] != 'WHERE':
            query += "AND"
        query += " company_id LIKE %s"
        args.append(company_id)
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # ucid-sl248 , date - 12/3/22
    if column != '':
        query += f" ORDER BY {column} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # ucid-sl248 , date - 12/3/22
    if limit != '':
        limit = limit
    else:
        limit = 10
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    # ucid-sl248 , date - 12/3/22
    try:
        limit = int(limit)
    except:
        flash('Limit must be an integer', "error")

    if limit < 1 or limit > 100:
        flash('Limit must be greater than 1 and less than or equal to 100', "error")

    # if column == '':
    #     query += f" ORDER BY id asc"

    query += f" LIMIT %s"
    args.append(limit)
    
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        # ucid-sl248 , date - 12/3/22
        print(str(e))
        flash("There was an error getting employee records", "error")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # ucid-sl248 , date - 12/3/22
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        
        if 'company' in request.form:
            company = request.form['company']
        else:
            company = ""

        form_error = False
        # TODO add-2 first_name is required (flash proper error message)
        # ucid-sl248 , date - 12/3/22
        if first_name == "":
            flash('First name is required', "error")
            form_error = True
        # TODO add-3 last_name is required (flash proper error message)
        # ucid-sl248 , date - 12/3/22
        if last_name == "":
            flash('Last name is required', "error")
            form_error = True
        # TODO add-4 company (may be None)
        # ucid-sl248 , date - 12/3/22
        if company == "":
            company = None
        # TODO add-5 email is required (flash proper error message)
        # ucid-sl248 , date - 12/3/22
        if email == "":
            flash('Email is required', "error")
            form_error = True
        
        if form_error == True:
            return redirect(request.url)
        
        try:
            result = DB.insertOne("""
            INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
            VALUES (%s, %s, %s, %s)
            """, first_name, last_name, email, company
            ) # <-- TODO add-6 add query and add arguments
            if result.status:
                flash("Created Employee Record", "success")
        except Exception as e:
            # TODO add-7 make message user friendly
            # ucid-sl248 , date - 12/3/22
            print(str(e))
            flash("There was an error creating the employee record", "error")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    # ucid-sl248 , date - 12/3/22
    if request.args.get('id', '' ) == '':
        flash('id is required', "error")

    row = {}

    id = request.args.get('id', '' )
    if id != '': # TODO update this for TODO edit-1
        if request.method == "POST":
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # ucid-sl248 , date - 12/3/22
            result = DB.selectOne("SELECT employees.id as id, first_name, last_name, email, companies.id as company_id, IF(name is not null, name,'N/A') as company_name FROM IS601_MP2_Employees employees LEFT JOIN IS601_MP2_Companies companies ON employees.company_id=companies.id WHERE employees.id=%s", id)
            if result.status:
                row = result.row

            if 'first_name' in request.form:
                first_name = request.form['first_name']
            else:
                first_name = row['first_name']

            if 'last_name' in request.form:
                last_name = request.form['last_name']
            else:
                last_name = row['last_name']

            if 'email' in request.form:
                email = request.form['email']
            else:
                email = row['email']

            if 'company' in request.form:
                company_id = request.form['company']
            else:
                company_id = row['company_id']
        
            form_error = False
            # TODO add-2 first_name is required (flash proper error message)
            # ucid-sl248 , date - 12/3/22
            if first_name == "":
                flash('First name is required', "error")
                form_error = True
            # TODO add-3 last_name is required (flash proper error message)
            # ucid-sl248 , date - 12/3/22
            if last_name == "":
                flash('Last name is required', "error")
                form_error = True
            # TODO add-4 company (may be None)
            # ucid-sl248 , date - 12/3/22
            if company_id == "":
                company_id = None
            # TODO add-5 email is required (flash proper error message)
            # ucid-sl248 , date - 12/3/22
            if email == "":
                flash('Email is required', "error")
                form_error = True
            
            # if form_error == True:
                # return redirect(request.url)
            
            data = [first_name, last_name, company_id, email]
            data.append(id)
            try:
                # TODO edit-6 fill in proper update query
                # ucid-sl248 , date - 12/3/22
                result = DB.update("""
                UPDATE IS601_MP2_Employees SET first_name=%s, last_name=%s, company_id=%s, email=%s WHERE id=%s
                """, *data)
                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-7 make this user-friendly
                # ucid-sl248 , date - 12/3/22
                print(str(e))
                flash("There was an error updating the employee record", "error")

        try:
            # TODO edit-8 fetch the updated data (including company_name)
            # company_name should be 'N/A' if the employee isn't assigned to a copany
            # ucid-sl248 , date - 12/3/22
            result = DB.selectOne("SELECT employees.id as id, first_name, last_name, email, companies.id as company_id, IF(name is not null, name,'N/A') as company_name FROM IS601_MP2_Employees employees LEFT JOIN IS601_MP2_Companies companies ON employees.company_id=companies.id WHERE employees.id=%s", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            # ucid-sl248 , date - 12/3/22
            print(str(e))
            flash("There was an error retrieving the employee record", "error")
    # TODO edit-10 pass the employee data to the render template
    # ucid-sl248 , date - 12/3/22
    return render_template("edit_employee.html", employee=row)

@employee.route("/delete", methods=["GET"])
def delete():
    if request.args.get('id', '' ) == '':
        flash('id is required', "error")

    id = request.args.get('id', '' )
    # TODO delete-1 delete employee by id
    # ucid-sl248 , date - 12/3/22
    try:
        result = DB.delete("DELETE FROM IS601_MP2_Employees WHERE id=%s", id)
        if result.status:
            # TODO delete-4 ensure a flash message shows for successful delete
            # ucid-sl248 , date - 12/3/22
            flash("Employee record successfully deleted", "success")
    except Exception as e:
        # TODO edit-9 make this user-friendly
        # ucid-sl248 , date - 12/3/22
        print(str(e))
        flash("There was an error deleting employee record", "error")
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # # ucid-sl248 , date - 12/3/22    
    return redirect(url_for('employee.search', first_name="", last_name="", email="", company="", order="asc", column="", limit=10))