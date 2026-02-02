class Phone:

    max_battery = 100

    def __init__(self, model, battery):
        self.model = model
        self.battery = battery


    def charge(self, amount):
        self.battery += amount
        if self.battery > Phone.max_battery:
            self.battery = Phone.max_battery

    def use_phone(self, amount):
        self.battery -= amount
        if self.battery < 0:
            self.battery = 0

   
    def show_battery_level(self):
        print(f"Battery level: {self.battery}%")

    
    @staticmethod
    def is_low_battery(level):
        if level < 20:
            print("Turn on low power mode")