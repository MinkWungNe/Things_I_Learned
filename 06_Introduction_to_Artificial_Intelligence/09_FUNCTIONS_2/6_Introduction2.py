import random

def create_username(first_name, last_name):
    username = first_name[0]+last_name

    username = username.lower()
    return username


def create_password():
    password = str(random.randint(1000,9999))
    return password

def create_database(customer):
    db = {}

    for khach in customer:
        username = create_username(khach[0], khach[1])

        password = create_password()

        db[username] = password
    n_customers = len(db)

    return db, n_customers

# TEST
customer = [['Maria', 'Lopez'], ['Julia', 'Smith'], ['Mohammed', 'Seid']]

db, customerCount = create_database(customer)

print(db)
print('Customer count:', customerCount)