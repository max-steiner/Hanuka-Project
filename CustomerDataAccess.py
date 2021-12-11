import sqlite3 as sq


# STEP 2. Creating a special class for accessing the database of customers.
# The separate functions, that were created in STEP 1, were used here.
class CustomerDataAccess:
    # Data access class for accessing the database of customers.

    def __init__(self, file_path):
        self.con = sq.connect(file_path)
        self.file_path = file_path
        self.cursor = self.con.cursor()

    def check_item(self, _id):
        self.cursor.execute('SELECT * FROM customer')
        self.con.commit()
        id_db = [row[0] for row in self.cursor]
        return _id in id_db

    def check_fname(self, fname):
        self.cursor.execute('SELECT * FROM customer')
        self.con.commit()
        fname_db = [row[1] for row in self.cursor]
        return fname in fname_db

    def print_all_customers(self):
        self.cursor.execute('SELECT * FROM customer')
        self.con.commit()
        print('All customers: ')
        print('________________')
        for row in self.cursor:
            print([row[0]], '>>>', *row[1:3], '<<<')
            print(row[3])
            print(f'mobile: {row[4]}', '\n')

    def insert_customer(self, customer):  # customer is the customer class instance
        if self.check_item(int(customer.customer_id)):
            print('\n')
            print('The customer with this id already exists.')
        elif self.check_fname(customer.fname):
            print('\n')
            answer = str(input('''Are you sure?" Customer with this first name already exists in the database.
If you want to make changes press [1]: '''))
            if answer != '1':
                print("OK. NO changes.")
            else:
                _id = customer.customer_id
                fname_new = customer.fname
                lname_new = customer.lname
                address_new = customer.address
                mobile_new = customer.mobile
                self.cursor.execute(f"INSERT INTO customer (customer_id, fname, lname, address, mobile) "
                                    f"VALUES({_id}, '{fname_new}', '{lname_new}', '{address_new}', '{mobile_new}')")
                self.con.commit()
                print('\n')
                print('The customer is inserted\n')
        else:
            _id = customer.customer_id
            fname_new = customer.fname
            lname_new = customer.lname
            address_new = customer.address
            mobile_new = customer.mobile
            self.cursor.execute(f"INSERT INTO customer (customer_id, fname, lname, address, mobile) "
                                f"VALUES({_id}, '{fname_new}', '{lname_new}', '{address_new}', '{mobile_new}')")
            self.con.commit()
            print('\n')
            print('The customer is inserted\n')

    def delete_customer(self, _id):
        cursor = self.cursor
        cursor.execute(f'''SELECT fname, lname FROM customer WHERE customer_id = {_id}''')
        customer_dell = cursor.fetchall()
        if customer_dell:
            cursor.execute(f'''DELETE FROM customer WHERE customer_id = {_id}''')
            self.con.commit()
            print(f'Information about the customer with id = {_id} ({customer_dell[0][0]} {customer_dell[0][1]}) '
                  f'has been removed from the database.\n')
        else:
            print(f'''Customer with id = {_id} in the database is not registered.\n''')

    def get_customer_by_id(self, _id):
        cursor = self.cursor
        cursor.execute(f'''SELECT * FROM customer WHERE customer_id = {_id}''')
        customer_by_choice = cursor.fetchall()
        self.con.commit()
        if customer_by_choice:
            print(f'''Information about the customer with id = {_id}:
            {customer_by_choice[0][1]} {customer_by_choice[0][2]}
            {customer_by_choice[0][3]}
            {customer_by_choice[0][4]}\n''')
        else:
            print(f'''Customer with id = {_id} in the database is not registered.\n''')

    def get_all_customers(self):
        self.cursor.execute('''SELECT * FROM customer''')
        all_customers_list = self.cursor.fetchall()
        self.con.commit()
        return all_customers_list

    def update_customer(self, _id, customer):
        cursor = self.cursor
        cursor.execute(f'''SELECT * FROM customer WHERE customer_id = {_id}''')
        customer_update = cursor.fetchall()
        if customer_update:
            cursor.execute(f"UPDATE customer SET customer_id = {customer.customer_id} WHERE customer_id = {_id} ")
            cursor.execute(f"UPDATE customer SET fname = '{customer.fname}' WHERE customer_id = {_id} ")
            cursor.execute(f"UPDATE customer SET lname = '{customer.lname}' WHERE customer_id = {_id} ")
            cursor.execute(f"UPDATE customer SET address = '{customer.address}' WHERE customer_id = {_id} ")
            cursor.execute(f"UPDATE customer SET mobile = {customer.mobile} WHERE customer_id = {_id} ")
            self.con.commit()
            print('\n')
            print('Data updated')
        else:
            print('\n')
            print(f'''Customer with id = {_id} in the database is not registered.\n''')

    def __repr__(self):
        return f'CustomerDataAccess {self.file_path}.'

    def __str__(self):
        return f'CustomerDataAccess: {self.file_path}.'
