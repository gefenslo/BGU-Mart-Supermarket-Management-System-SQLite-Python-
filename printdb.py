from persistence import *

def print_table(name, records):
    print(name)
    for record in records:
        print(record)
    print()  

def print_detailed_employees_report():
    query = """
   SELECT e.name, e.salary, b.location, 
       COALESCE(SUM(CASE WHEN a.quantity < 0 THEN ABS(a.quantity * p.price) ELSE 0 END), 0) as total_sales_income
        FROM employees e
            LEFT JOIN branches b ON e.branche = b.id
            LEFT JOIN activities a ON e.id = a.activator_id 
            LEFT JOIN products p ON a.product_id = p.id
            GROUP BY e.id, e.name, e.salary, b.location
            ORDER BY e.name;
    """
    results = repo.execute_query(query)
    for result in results:
        name, salary, location, total_sales_income = result
        print(f"{name} {salary} {location} {total_sales_income}")

import sqlite3

def print_detailed_activity_report():
    conn = sqlite3.connect("bgumart.db")
    cursor = conn.cursor()

    query = """
    SELECT 
        a.date, 
        p.description, 
        a.quantity,
        CASE 
            WHEN a.quantity < 0 THEN e.name 
            ELSE 'None' 
        END AS seller_name,
        CASE 
            WHEN a.quantity > 0 THEN s.name 
            ELSE 'None' 
        END AS supplier_name
    FROM activities a
    JOIN products p ON a.product_id = p.id
    LEFT JOIN employees e ON a.activator_id = e.id AND a.quantity < 0
    LEFT JOIN suppliers s ON a.activator_id = s.id AND a.quantity > 0
    ORDER BY a.date ASC;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()
    for result in results:
        
        date, desc, qty, seller, supplier = result
        print(f"('{desc}', {qty}, {repr(seller)}, '{repr(supplier)}','{date}')")


def main():
    print_table("Activities", sorted(repo.activities.find_all(), key=lambda a: a.date))
    print_table("Branches", sorted(repo.branches.find_all(), key=lambda b: b.id))
    print_table("Employees", sorted(repo.employees.find_all(), key=lambda e: e.id))
    print_table("Products", sorted(repo.products.find_all(), key=lambda p: p.id))
    print_table("Suppliers", sorted(repo.suppliers.find_all(), key=lambda s: s.id))

    print("Employees report")
    print_detailed_employees_report()
    print()
    print("Activities report")
    print_detailed_activity_report()

if __name__ == '__main__':
    main()