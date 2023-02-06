from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count for the company
    # ucid-sl248 , date - 12/3/22
    # don't do SELECT *
    query = "SELECT id, name, address, city, country, state, zip, website, (SELECT COUNT(*) FROM IS601_MP2_Employees WHERE company_id=companies.id) as employees FROM IS601_MP2_Companies companies"
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = [("name", "Name"), ("city", "City"), ("country", "Country"), ("state", "State")]
    # TODO search-2 get name, country, state, column, order, limit request args
    # ucid-sl248 , date - 12/3/22
    name = request.args.get('name', '' )
    country = request.args.get('country', '' )
    state = request.args.get('state', '' )
    column = request.args.get('column', '' )
    order = request.args.get('order', '' )
    limit = request.args.get('limit', '' )
    if name != '' or country != '' or state != '':
        query += " WHERE "

    # TODO search-3 append a LIKE filter for name if provided
    # ucid-sl248 , date - 12/3/22
    if name != '':
        name = f"%{name}%"
        query += " name LIKE %s"
        args.append(name)
    # TODO search-4 append an equality filter for country if provided
    # ucid-sl248 , date - 12/3/22
    if country != '':
        if list(query.split(" "))[-2] != 'WHERE':
            query += "AND"
        query += " country = %s"
        args.append(country)
    # TODO search-5 append an equality filter for state if provided
    # ucid-sl248 , date - 12/3/22
    if state != '':
        if list(query.split(" "))[-2] != 'WHERE':
            query += "AND"
        query += " state = %s"
        args.append(state)
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    # ucid-sl248 , date - 12/3/22
    if column != '':
        query += f" ORDER BY {column} {order}"
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # ucid-sl248 , date - 12/3/22
    if limit != '':
        limit = limit
    else:
        limit = 10
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    # ucid-sl248 , date - 12/3/22
    try:
        limit = int(limit)
    except:
        flash('Limit must be an integer', "error")

    if limit < 1 or limit > 100:
        flash('Limit must be greater than 1 and less than or equal to 100', "error")

    if column == '':
        query += f" ORDER BY id asc"

    query += f" LIMIT %s"
    args.append(limit)
    
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        # ucid-sl248 , date - 12/3/22
        print(str(e))
        flash("There was an error getting company records", "error")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        # ucid-sl248 , date - 12/3/22
        if 'name' in request.form:
            name = request.form['name']
        else:
            name = ""

        if 'address' in request.form:
            address = request.form['address']
        else:
            address = ""

        if 'city' in request.form:
            city = request.form['city']
        else:
            city = "" 

        if 'state' in request.form:
            state = request.form['state']
        else:
            state = "" 

        if 'country' in request.form:
            country = request.form['country']
        else:
            country = "" 

        if 'zip' in request.form:
            zipcode = request.form['zip']
        else:
            zipcode = "" 

        if 'website' in request.form:
            website = request.form['website']
        else:
            website = "" 

        has_error = False # use this to control whether or not an insert occurs

        # TODO add-2 name is required (flash proper error message)
        # ucid-sl248 , date - 12/3/22
        if name == "":
            flash("Company's name is required", "error")
            has_error = True
        # TODO add-3 address is required (flash proper error message)
        # ucid-sl248 , date - 12/3/22
        if address == "":
            flash('Address is required', "error")
            has_error = True
        # TODO add-4 city is required (flash proper error message)
        # ucid-sl248 , date - 12/3/22
        if city == "":
            flash('City is required', "error")
            has_error = True
        # TODO add-5 state is required (flash proper error message)
        # ucid-sl248 , date - 12/3/22
        if state == "":
            flash('State is required', "error")
            has_error = True
        # TODO add-6 country is required (flash proper error message)
        # ucid-sl248 , date - 12/3/22
        if country == "":
            flash('Country is required', "error")
            has_error = True
        # TODO add-7 website is not required
        # ucid-sl248 , date - 12/3/22
        if website == "":
            pass
        
    
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP2_Companies (name, address, city, country, state, zip, website)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, name, address, city, country, state, zipcode, website
                ) # <-- TODO add-8 add query and add arguments
                
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                # ucid-sl248 , date - 12/3/22
                print(str(e))
                flash("There was an error creating the company record", "error")
        
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    # ucid-sl248 , date - 12/3/22
    if request.args.get('id', '' ) == '':
        flash('id is required', "error")

    row = {}

    id = request.args.get('id', '' )
    if id != '': # TODO update this for TODO edit-1
        if request.method == "POST":
            result = DB.selectOne("SELECT id, name, address, city, country, state, zip, website, (SELECT COUNT(*) FROM IS601_MP2_Employees WHERE company_id=companies.id) as employee_count FROM IS601_MP2_Companies companies WHERE id=%s", id)
            if result.status:
                row = result.row

            if 'name' in request.form:
                name = request.form['name']
            else:
                name = row['name']

            if 'address' in request.form:
                address = request.form['address']
            else:
                address = row['address']

            if 'city' in request.form:
                city = request.form['city']
            else:
                city = row['city']

            if 'state' in request.form:
                state = request.form['state']
            else:
                state = row['state']

            if 'country' in request.form:
                country = request.form['country']
            else:
                country = row['country']

            if 'zip' in request.form:
                zipcode = request.form['zip']
            else:
                zipcode = row['zip']

            if 'website' in request.form:
                website = request.form['website']
            else:
                website = row['website']

            has_error = False # use this to control whether or not an insert occurs

            # TODO add-2 name is required (flash proper error message)
            # ucid-sl248 , date - 12/3/22
            if name == "":
                flash("Company's name is required", "error")
                has_error = True
            # TODO add-3 address is required (flash proper error message)
            # ucid-sl248 , date - 12/3/22
            if address == "":
                flash('Address is required', "error")
                has_error = True
            # TODO add-4 city is required (flash proper error message)
            # ucid-sl248 , date - 12/3/22
            if city == "":
                flash('City is required', "error")
                has_error = True
            # TODO add-5 state is required (flash proper error message)
            # ucid-sl248 , date - 12/3/22
            if state == "":
                flash('State is required', "error")
                has_error = True
            # TODO add-6 country is required (flash proper error message)
            # ucid-sl248 , date - 12/3/22
            if country == "":
                flash('Country is required', "error")
                has_error = True
            # TODO add-7 website is not required
            # ucid-sl248 , date - 12/3/22
            if website == "":
                pass
            
            
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            data = [name, address, city, state, country, zipcode, website]
            data.append(id)
            
            try:
                # TODO edit-9 fill in proper update query
                # ucid-sl248 , date - 12/3/22
                result = DB.update("""
                UPDATE IS601_MP2_Companies SET name=%s, address=%s, city=%s, state=%s, country=%s, zip=%s, website=%s WHERE id=%s
                """, *data)
                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-10 make this user-friendly
                # ucid-sl248 , date - 12/3/22
                print(str(e))
                flash("There was an error updating the company record", "error")
        try:
            # TODO edit-11 fetch the updated data
            # ucid-sl248 , date - 12/3/22
            result = DB.selectOne("SELECT id, name, address, city, country, state, zip, website, (SELECT COUNT(*) FROM IS601_MP2_Employees WHERE company_id=companies.id) as employee_count FROM IS601_MP2_Companies companies WHERE id=%s", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            # ucid-sl248 , date - 12/3/22
            print(str(e))
            flash("There was an error retrieving the employee record", "error")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", company=row)

@company.route("/delete", methods=["GET"])
def delete():
    if request.args.get('id', '' ) == '':
        flash('id is required', "error")

    id = request.args.get('id', '' )
    # TODO delete-1 delete company by id (unallocate any employees)
    # ucid-sl248 , date - 12/3/22
    try:
        pass
        employees_result = DB.update("""
                UPDATE IS601_MP2_Employees SET company_id=null WHERE company_id=%s
                """, id)

        result = DB.delete("DELETE FROM IS601_MP2_Companies WHERE id=%s", id)
        if result.status:
            # TODO delete-4 ensure a flash message shows for successful delete
            # ucid-sl248 , date - 12/3/22
            flash("Company record successfully deleted", "success")
    except Exception as e:
        # TODO edit-9 make this user-friendly
        # ucid-sl248 , date - 12/3/22
        print(str(e))
        flash("There was an error deleting company record", "error")

    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # ucid-sl248 , date - 12/3/22
    return redirect(url_for('company.search', name="", country="", state="",order="asc", column="", limit=10))