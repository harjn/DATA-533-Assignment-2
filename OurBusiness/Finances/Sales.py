class Sale:
    totalSales=0
    def __init__(self, itemName, cost, saleDate, employeeID):
        self.itemName = itemName
        self.cost = cost
        self.saleDate = saleDate
        self.employeeID = employeeID
        
        totalSales += cost 
        
    def totalSales(self):
        return totalSales