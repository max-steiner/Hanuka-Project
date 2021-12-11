import sqlite3 as sq
from Customer import Customer
from CustomerDataAccess import CustomerDataAccess
import sys

con = sq.connect('mydb.db')
cursor = con.cursor()


# STEP 1. Creating separate functions for maintaining the database of customers.
def print_all_customers():
    cursor.execute("SELECT * FROM customer")
    print('All customers: ')
    print('________________')
    for row in cursor:
        print([row[0]], '>>>', *row[1:3], '<<<')
        print(row[3])
        print(f'mobile: {row[4]}', '\n')


def insert_customer(customer):  # customer is the customer class instance
    while type(customer) is not Customer:
        customer = input('Input a correct data: ')
    fname_new = customer.fname
    lname_new = customer.lname
    address_new = customer.address
    mobile_new = customer.mobile
    cursor.execute(f'''INSERT INTO customer (fname, lname, address, mobile) 
    VALUES({fname_new}, {lname_new}, '{address_new} '{mobile_new})''')


def create_customer():  # this is an optional function to use when checking the code
    print('''Enter the customer details. After each input press [Enter]''')
    print()
    customer_id = int(input("Enter the new customer id: "))
    fname = str(input("Enter the first name of the customer: "))
    lname = str(input("Enter the last name of the customer: "))
    address = str(input("Enter the address of the customer: "))
    mobile = str(input("Enter the mobile number of customer: "))
    customer_new = Customer(customer_id, fname, lname, address, mobile)
    return customer_new


def delete_customer(_id):
    cursor.execute(f'''SELECT fname, lname FROM customer WHERE customer_id = {_id}''')
    customer_dell = cursor.fetchall()
    if customer_dell:
        cursor.execute(f'''DELETE FROM customer WHERE customer_id = {_id}''')
        print(f'Information about the customer with id = {_id} ({customer_dell[0][0]} {customer_dell[0][1]}) '
              f'has been removed from the database.\n')
    else:
        print(f'''Customer with id = {_id} in the database is not registered.\n''')


def get_all_customers():
    cursor.execute('''SELECT * FROM customer''')
    all_customers_list = cursor.fetchall()
    return all_customers_list


def get_customer_by_id(_id):
    cursor.execute(f'''SELECT * FROM customer WHERE customer_id = {_id}''')
    customer_with_id = cursor.fetchone()
    return customer_with_id


def update_customer(_id, customer):
    while type(customer) is not Customer:
        input('Input a correct data: ')
    fname_new = customer.fname
    lname_new = customer.lname
    address_new = customer.address
    mobile_new = customer.mobile
    cursor.execute(f'''UPDATE customer SET fname = {fname_new}, lname = {lname_new}, 
    address = {address_new}, mobile = {mobile_new} WHERE customer_id = {_id}''')


# STEP 2. Using a specially created class (DAO) for maintaining the database of customers.
dao = CustomerDataAccess('mydb.db')

# Creating an instance by the class Customer to test the program:
Mahmud = Customer(customer_id=10, fname='Mahmud', lname='Aliyev',
                  address='5503425, Moscow, Tverskaya st. 1/10', mobile='0772345647')


# STEP 3. Creating a user interface for database maintenance with using special class CustomerDataAccess.
def use_db():
    print('\n' * 100)
    print('''To use the database of customers input the
number of menu item and press [Enter]:
             1 - Get all customers
             2 - Get customers by id
             3 - Insert customer
             4 - Delete customer
             5 - Update customers
             6 - Exit\n''')
    user_choice = input('Input your choice: ')

    while user_choice.isalpha() or user_choice not in ['1', '2', '3', '4', '5', '6']:
        user_choice = input('Input error. Please enter correct data: ')
    user_choice = int(user_choice)

    if user_choice == 1:
        dao.print_all_customers()
    elif user_choice == 2:
        _id = int(input('Input customer id: '))
        dao.get_customer_by_id(_id)
#        customer_by_choice = dao.get_customer_by_id(_id)
    elif user_choice == 3:
        customer = create_customer()
        dao.insert_customer(customer)
    elif user_choice == 4:
        _id = int(input('Input customer id: '))
        dao.delete_customer(_id)
    elif user_choice == 5:
        _id = int(input('Input customer id: '))
        print('Create and input an instance of customer within the Customer class to update.\n')
        customer = create_customer()
        dao.update_customer(_id, customer)
    else:
        print('The session has been completed')
        sys.exit()


#  The main loop
def main():
    session = True
    while session:
        use_db()
        con.commit()
        session = input('To return to the main menu press any key and [Enter]: ')
    con.close()


main()

