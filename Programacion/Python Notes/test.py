

class Converter:
    @staticmethod
    def km_to_miles(km):
        return km * 0.621371
    
    @staticmethod
    def celcius_to_fahrenheit(celcius):
        return (celcius * 9/5) + 32
    
print(Converter.km_to_miles(10))  
print(Converter.celcius_to_fahrenheit(25))     