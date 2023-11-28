import psycopg2
import uuid


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="scm",
            user="postgres",
            password="pass1")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn


def add_supplier(supplier_name, contact_information, product_categories):
    """ Add a new supplier to the Suppliers table """
    conn = connect()
    try:
        with conn:
            with conn.cursor() as cur:
                supplier_id = uuid.uuid4()
                cur.execute(
                    f"INSERT INTO Suppliers (SupplierID, SupplierName, ContactInformation, ProductCategoriesSupplied) VALUES "
                    f"('{supplier_id}', '{supplier_name}', '{contact_information}', ARRAY['{product_categories}']);")

                print("Supplier added with ID:", supplier_id)
    finally:
        conn.close()
        return supplier_id



def select_suppliers():
    """ Select all suppliers from the Suppliers table """
    conn = connect()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM Suppliers")
                suppliers = cur.fetchall()
                for supplier in suppliers:
                    print(supplier)
    finally:
        conn.close()


def update_supplier(supplier_id, supplier_name):
    """ Update a supplier's name in the Suppliers table """
    conn = connect()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE Suppliers SET SupplierName = '{supplier_name}' "
                            f"WHERE SupplierID = '{supplier_id}'")

                print("Supplier updated with ID:", supplier_id)
    finally:
        conn.close()


def delete_supplier(supplier_id):
    """ Delete a supplier from the Suppliers table """
    conn = connect()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM Suppliers WHERE SupplierID = '{supplier_id}'")
                print("Supplier deleted with ID:", supplier_id)
    finally:
        conn.close()


def get_data_distribution_details():
    """ Get data distribution details from the Citus cluster """
    conn = connect()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT 
                        logicalrelid AS table_name,
                        pg_dist_shard.shardid,
                        nodename,
                        nodeport,
                        shardminvalue,
                        shardmaxvalue
                    FROM pg_dist_shard 
                    JOIN pg_dist_placement ON pg_dist_shard.shardid = pg_dist_placement.shardid
                    JOIN pg_dist_node ON pg_dist_placement.groupid = pg_dist_node.groupid;
                """)
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    finally:
        conn.close()

# Example usage
get_data_distribution_details()



# Example usage
# add_supplier('Supplier A', 'Contact Info', ['Category1', 'Category2'])
# select_suppliers()
# update_supplier(uuid.UUID('your-supplier-id-here'), 'New Supplier Name')
# delete_supplier(uuid.UUID('your-supplier-id-here'))

supplier_id = add_supplier("Supplier-1", "+1-9900220033", "Electronics")
print("After Addition: ")
select_suppliers()

update_supplier(supplier_id, "Electronic Supplier")
print("After Update: ")
select_suppliers()
delete_supplier(supplier_id)
print("After Deletion: ")
select_suppliers()

