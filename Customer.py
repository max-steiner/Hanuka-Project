
class Customer:
    # customer class for database maintenance
    def __init__(self, customer_id, fname, lname, address, mobile):
        self.customer_id = customer_id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.mobile = mobile

    def __repr__(self):
        return f'[Customer], Customer id: {self.customer_id}, First Name: {self.fname}\n' \
               f'Last Name: {self.lname}\n' \
               f'Address:  {self.address}\n'\
               f'Mobile: {self.mobile}\n' \
               f'__________________'

    def __str__(self):
        return f'--------\n' \
               f'[Customer]\n' \
               f'Customer id: {self.customer_id}\n' \
               f'First Name: {self.fname}\n' \
               f'Last Name: {self.lname}\n' \
               f'Address:  {self.address}\n'\
               f'Mobile: {self.mobile}\n' \
               f'__________________'

