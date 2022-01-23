class Contract:
    hourly_rate = 30
    
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        self.active = True
        
    def spend_hours(self, hours_spent):
        if hours_spent > self.hours:
            raise ValueError("Not enough hours on this contact to do that")
            
        self.hours -= hours_spent
        self.active = self.hours > 0
        return hours_spent * Contract.hourly_rate
            
    def __str__(self):
        if self.active:
            return f"Contract with {self.name} is still active, {self.hours} hours remaining."
        else:
            return f"Contract with {self.name} is inactive."
        
    @classmethod
    def add_inflation(cls, inflation_percent=1):
        new_rate = Contract.increase_percentage(cls.hourly_rate, inflation_percent)
        cls.hourly_rate = round(new_rate, 2)
        
    @staticmethod
    def increase_percentage(value, percentage):
        return value * (1 + percentage/100)
            
        
contract1 = Contract("A", 40)
contract2 = Contract("B", 50)

Contract.add_inflation(2)
print(f"New hourly rate after inflation: {Contract.hourly_rate}")

total_owed = 0
total_owed += contract1.spend_hours(40)
total_owed += contract2.spend_hours(30)

print(f"We owe £{total_owed} for this week's work.")
