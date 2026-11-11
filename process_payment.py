def process_payment(student_name, cource_fee, paid_amount):

    def validate_payment():
        if paid_amount <= 0:
            return False
        if paid_amount > cource_fee:
            return False
        return True

    def calculate_balance():
        return cource_fee - paid_amount

    def generate_receipt(balance):
        print("--- Payment Receipt ---")
        print("-------------")
        print("student name :",student_name)
        print("cource fee :",cource_fee)
        print("paid amount :",paid_amount)
        print("balance :",balance)

    if validate_payment():
        balance = calculate_balance()
        generate_receipt(balance)
    else:
        print("Payment validation failed. Please check the amounts.")




process_payment("John Doe", 5000, 3000)