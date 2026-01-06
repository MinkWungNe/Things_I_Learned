import setupdatabase as sdb     # Module name can't have special character | 'sdb' is a name assigned to the Module.
# from setupdatabase import create_username as cu -> import only create_username function.

username = sdb.create_username('John', 'Gelb')
print(username)

customer = [['Maria', 'Lopez'], ['Julia', 'Smith'], ['Mohammed', 'Seid']]
db, customerCount = sdb.create_database(customer)

print(db)
print('Customer count:', customerCount)