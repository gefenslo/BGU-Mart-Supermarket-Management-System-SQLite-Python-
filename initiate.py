from persistence import *

import sys
import os

def add_branche(splittedline : list[str]):
    branch_id = splittedline[0]
    branch_name = splittedline[1]
    branch_size = splittedline[2]
    repo.branches.insert(Branche(branch_id, branch_name, branch_size))


def add_supplier(splittedline : list[str]):
    supplier_id = splittedline[0]
    supplier_name = splittedline[1]
    supplier_contact = splittedline[2]
    repo.suppliers.insert(Supplier(supplier_id, supplier_name, supplier_contact))

def add_product(splittedline : list[str]):
    product_id = splittedline[0]
    product_description = splittedline[1]
    product_price = splittedline[2]
    product_quantity = splittedline[3]
    repo.products.insert(Product(product_id, product_description, product_price, product_quantity))

def add_employee(splittedline : list[str]):
    employee_id = splittedline[0]
    employee_name = splittedline[1]
    employee_salary = splittedline[2]
    employee_branch = splittedline[3]
    repo.employees.insert(Employee(employee_id, employee_name, employee_salary, employee_branch))

adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo._close()
    # uncomment if needed
    # if os.path.isfile("bgumart.db"):
    #     os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)