# Base class (general Device)
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        print(f"Device: {self.brand} {self.model}")

    def power_on(self):
        print(f"{self.brand} {self.model} is powering on 🔋")


# Derived class (Smartphone)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)   # Call parent constructor
        self.os = os
        self.storage = storage
        self.__battery = 100  # private attribute (encapsulation)
    
    # Encapsulation: control battery access
    def get_battery(self):
        return f"Battery at {self.__battery}%"
    
    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"Charged 🔌 → {self.get_battery()}")
    
    # Polymorphism: override method
    def power_on(self):
        print(f"{self.brand} {self.model} is booting into {self.os} 📱")

    # Extra methods
    def take_photo(self):
        print(f"{self.brand} {self.model} takes a photo 📸")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.model} 📲")


# Another derived class (Tablet) to show polymorphism
class Tablet(Device):
    def power_on(self):
        print(f"{self.brand} {self.model} is starting in tablet mode 💻")


# --- Demo ---
phone1 = Smartphone("Apple", "iPhone 15", "iOS", "256GB")
phone2 = Smartphone("Samsung", "Galaxy S24", "Android", "512GB")
tablet1 = Tablet("Microsoft", "Surface Pro 9")

# Use methods
phone1.info()
phone1.power_on()
phone1.take_photo()
phone1.install_app("WhatsApp")
phone1.charge(15)

print("\n--- Polymorphism in action ---")
devices = [phone1, phone2, tablet1]
for d in devices:
    d.power_on()  # Each behaves differently!
