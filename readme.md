# SCM Database Management System

This SCM (Supply Chain Management) system is designed to manage supplier data efficiently using a Citus cluster, which extends PostgreSQL to provide a distributed database system. The system is Dockerized for ease of deployment and scaling.

## Features

- Manage supplier data (add, select, update, delete).
- View data distribution details in the Citus cluster.

## Setup

To set up and run this application, you need Docker and Docker Compose installed on your machine.

### Starting the Citus Cluster

1. **Start the Cluster**: Run the following command to start the Citus master and worker nodes:

   ```bash
   docker-compose up -d
Initialize the Database: The insert_data.sql and schema.sql files are used to initialize the database. These are added to the volume of the Docker application using the Docker Compose file.

To run the script file using the psql command, execute:

   ```bash
docker exec -it master psql -U postgres -d scm -f /usr/local/bin/schema.sql
docker exec -it master psql -U postgres -d scm -f /usr/local/bin/insert_data.sql
```
Python Script Usage
The Python script provided interacts with the SCM database to perform various operations.

Prerequisites
Ensure Python is installed.

Install the psycopg2 package:

```bash
pip install psycopg2-binary
```

### Running the Script
The script contains functions to add, select, update, and delete suppliers, as well as to view data distribution details.

To use the script, simply call the desired function. Example usage is provided in the script comments.

Functions
```python add_supplier(supplier_name, contact_information, product_categories): Add a new supplier.
select_suppliers(): List all suppliers.
update_supplier(supplier_id, supplier_name): Update a supplier's details.
delete_supplier(supplier_id): Remove a supplier.
get_data_distribution_details(): Get details of how data is distributed across the Citus cluster.
```
# Example Usage
```python

# Add a new supplier
supplier_id = add_supplier("Supplier-1", "+1-9900220033", "Electronics")

# View all suppliers
print("After Addition: ")
select_suppliers()

# Update a supplier's details
update_supplier(supplier_id, "Electronic Supplier")
print("After Update: ")
select_suppliers()

# Delete a supplier
delete_supplier(supplier_id)
print("After Deletion: ")
select_suppliers()
```
### Note
1. Modify the database connection parameters in the connect function of the Python script as per your environment.
2. Ensure the Citus cluster is up and running before executing the script.