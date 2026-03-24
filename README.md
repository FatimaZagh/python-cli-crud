# Python CLI Products CRUD

Minimal Command-Line Interface (CLI) tool to perform CRUD operations on products using Python, SQLAlchemy, and PostgreSQL.

---

## Features

- List all products
- Add a new product
- Get product by ID
- Update a product
- Delete a product

---

## Technologies Used

- Python 3.14+
- PostgreSQL
- SQLAlchemy ORM
- Click (CLI library)
- python-dotenv (for environment variables)
- psycopg2-binary (PostgreSQL driver)

---

## Setup Instructions

1. **Clone the repository**  
```bash
git clone https://github.com/FatimaZagh/python-cli-crud.git
cd python-cli-crud


Install dependencies
pip install -r requirements.txt

Configure environment variables
Create a .env file in the root directory with your PostgreSQL URL:
DATABASE_URL=postgresql://username:password@localhost:5432/products_db


DATABASE_URL=postgresql://username:password@localhost:5432/products_db
createdb products_db


# Add products
python -m app.cli add "Laptop" 1000
python -m app.cli add "Mouse" 50

# List products
python -m app.cli list

# Get product by ID
python -m app.cli get 1

# Update product
python -m app.cli update 1 "Laptop Updated" 1200

# Delete product
python -m app.cli delete 1


Fatima Zaghlol
