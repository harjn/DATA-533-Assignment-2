class Sale:
    totalSales=0
    def __init__(self, itemName, cost, saleDate, employeeID, customerID):
        self.itemName = itemName
        self.cost = cost
        self.saleDate = saleDate
        self.employeeID = employeeID
		self.customerID = customerID
        
        totalSales += cost 
        
    def totalSales(self):
        return totalSales