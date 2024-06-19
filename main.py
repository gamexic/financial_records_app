from models.financial import FinancialRecord
from services.database_service import DatabaseService


# * Función para crear un registro/nueva cuenta
def create_new_account():
    
    # * Crear una instancia de DatabaseService
    db_service = DatabaseService('db/database.db')
    
    # * Crear una instancia de FinancialRecord

    # Solicitamos al usuario los datos del registro
    id = input("User ID: ")
    description = input("Description: ")
    amount = float(input("Amount: "))
    type = "new_account"

    # Agrupamos los datos en un objeto
    new_record = FinancialRecord(id=id, description=description, amount=amount, type=type)

    # * Agregar el registro a la base de datos
    db_service.add_record(new_record)


# * Función para hacer un ingreso
def create_new_income():
    db_service = DatabaseService('db/database.db')
    id = input("User ID: ")
    description = input("Description: ")
    amount = float(input("Amount: "))
    type = "income"

    new_record = FinancialRecord(id=id, description=description, amount=amount, type=type)
    db_service.add_money(new_record)


# * Función para hacer un gasto
def create_new_expense():
    db_service = DatabaseService('db/database.db')
    id = input("User ID: ")
    description = input("Description: ")
    amount = float(input("Amount: "))
    type = "expense"

    new_record = FinancialRecord(id=id, description=description, amount=amount, type=type)
    db_service.add_money(new_record)


# * Función para obtener todos los registros
def get_all_records():
    db_service = DatabaseService('db/database.db')
    records = db_service.get_records()
    return records


# * Función para obtener el balance total
def get_total_balance():
    db_service = DatabaseService('db/database.db')
    records = db_service.get_records()
    total_balance = 0
    id = int(input("User ID: "))
    for record in records:
        if record[0] == id:
            if record[3] == "income" or record[3] == "new_account":
                total_balance += record[2]
            elif record[3] == "expense":
                total_balance -= record[2]
    return total_balance


# * Función para obtener el balance de ingresos
def get_income_balance():
    db_service = DatabaseService('db/database.db')
    records = db_service.get_records()
    income_balance = 0
    id = int(input("User ID: "))
    for record in records:
        if record[0] == id:
            if record[3] == "income" or record[3] == "new_account":
                income_balance += record[2]
    return income_balance


# * Función para obtener el balance de gastos
def get_expense_balance():
    db_service = DatabaseService('db/database.db')
    records = db_service.get_records()
    expense_balance = 0
    id = int(input("User ID: "))
    for record in records:
        if record[0] == id:
            if record[3] == "expense":
                expense_balance += record[2]
    return expense_balance



def main():
    db_service = DatabaseService('db/database.db')
    db_service.create_table()

    while True:
        print("1. Create new account")
        print("2. Create new income")
        print("3. Create new expense")
        print("4. Get all records")
        print("5. Get total balance")
        print("6. Get income balance")
        print("7. Get expense balance")
        print("8. Exit")
        option = input("Option: ")

        if option == "1":
            create_new_account()
        elif option == "2":
            create_new_income()
        elif option == "3":
            create_new_expense()
        elif option == "4":
            records = get_all_records()
            for record in records:
                print(record)
        elif option == "5":
            total_balance = get_total_balance()
            print(total_balance)
        elif option == "6":
            income_balance = get_income_balance()
            print(income_balance)
        elif option == "7":
            expense_balance = get_expense_balance()
            print(expense_balance)
        elif option == "8":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
