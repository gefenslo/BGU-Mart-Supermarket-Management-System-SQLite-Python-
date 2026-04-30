# BGU Mart Supermarket Management System

A Python and SQLite-based system for managing supermarket chains, including employees, suppliers, products, branches, inventory, and activity logging.

## Features

- **Database Initialization:** Create and populate the database from a configuration file.
- **Activity Management:** Process sales and supply actions with inventory validation.
- **Comprehensive Reporting:** Print the current state of the database and generate detailed employee and activity reports.
- **Modular Design:** Separate scripts for initialization, actions, and reporting.

## Project Structure

- `initiate.py` — Initializes the database and loads initial data from a config file.
- `action.py` — Processes sales and supply activities from an actions file.
- `printdb.py` — Prints all tables and generates detailed reports.
- `dbtools.py`, `persistence.py` — (Optional) Helper modules for database operations.
- `config.txt` — Example configuration file for initial data.
- `action.txt` — Example actions file for activities.

## Usage

1. **Initialize the Database**
	```sh
	python3 initiate.py config.txt
	```

2. **Process Activities**
	```sh
	python3 action.py action.txt
	```

3. **Print Database and Reports**
	```sh
	python3 printdb.py
	```

## Table Structure

- **employees:** id, name, salary, branch
- **suppliers:** id, name, contact_information
- **products:** id, description, price, quantity
- **branches:** id, location, number_of_employees
- **activities:** product_id, quantity, activator_id, date

## Reports

- **Employees Report:** Name, salary, branch location, total sales income.
- **Activities Report:** Date, product, quantity, seller/supplier names.

## Requirements

- Python 3.9+
- SQLite3 (standard with Python)

## How It Works

1. `initiate.py` creates a fresh database and loads initial data.
2. `action.py` updates inventory and logs activities based on actions.
3. `printdb.py` prints all tables and generates reports using SQL queries.


