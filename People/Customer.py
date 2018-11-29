class Customer:
    emails=[]
    def __init__(self, customerID, email):
        self.customerID = customerID
        Customer.emails.append(email)
        
    def allEmails(self):
        return Customer.emails