class Customer:
    emails=[]
    def __init__(self, firstName, lastName, customerID, email):
        self.firstName = firstName
        self.lastName = lastName
        self.customerID = customerID
        self.email = email
        Customer.emails.append(email)
		
        

		
def allEmails():
	"""
	Returns a list of all customers' email
	"""
	return Customer.emails
