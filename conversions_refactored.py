class Temperature:
    """docstring for Temperature"""
    def __init__(self, temp_C):
        self.temp_C = temp_C

    def temperature_C_to_K(self):
        print(self.temp_C + 273.15)

    def temperature_C_to_F(self):
        print ((self.temp_C*1.8)+32)

    def temperature_F_to_C(self):
        print((self.temp_C - 32.0) * 5.0 / 9.0)

    def temperature_F_to_K(self):
        print(273.5 + ((self.temp_C - 32.0) * (5.0/9.0)))

    def temperature_K_to_C(self):
        print(self.temp_C - 273.15)

    def temperature_K_to_F(self):
        print(1.8 * (self.temp_C - 273.15) + 32)

    def converter_Mi_to_Ya(self):
        print (self.temp_C*1760)

    def converter_Mi_to_Me(self):
        print (self.temp_C*1609.34)

    def converter_Ya_to_Mi(self):
        print (self.temp_C*0.000568182)

    def converter_Ya_to_Me(self):
        print (self.temp_C*0.9144)

    def converter_Me_to_Mi(self):
        print(self.temp_C*0.000621371)

    def converter_Me_to_Ya(self):
        print (self.temp_C*1.09361)

# print("1 for Celsius in Kelvin, 2 Celsius in Fahrenheit")
# print("3 for Fahrenheit in Celsius, 4 Fahrenheit in Kelvin")
# print("5 for Kelvin in Celsius, 6 Kelvin in Fahrenheit")
# print("7 for Miles in Yard, 8 Miles in Meter")
# print("9 for Yard in Miles, 10 Yard in Meter")
# print("11 for Meter in Miles, 12 Meter in Yard")

print("celsius, kelvin, fahrenheit")
print("meter, miles, yard")

temp_list = ['celsius', 'kelvin', 'fahrenheit']
dis_list = ['meter', 'miles', 'yard']

fromUnit = raw_input("Type your fromUnit :- ").lower()
toUnit = raw_input("Type your toUnit :- ").lower()

try:
    temp_C = int(raw_input("value"))
    if fromUnit in temp_list and toUnit in temp_list:
        convValue = Temperature(temp_C)
        if fromUnit == 'celsius' and toUnit == 'kelvin':
            convValue.temperature_C_to_K()

        if fromUnit == 'celsius' and toUnit == 'fahrenheit':
            convValue.temperature_C_to_F() 

        if fromUnit == 'fahrenheit' and toUnit == 'celsius':
            convValue.temperature_F_to_C() 

        if fromUnit == 'fahrenheit' and toUnit == 'kelvin':
            convValue.temperature_F_to_K() 

        if fromUnit == 'kelvin' and toUnit == 'celsius':
            convValue.temperature_K_to_C() 

        if fromUnit == 'kelvin' and toUnit == 'fahrenheit':
            convValue.temperature_K_to_F()
    else:
        if fromUnit in dis_list and toUnit in dis_list:
            if fromUnit == 'miles' and toUnit == 'yard':
                convValue.converter_Mi_to_Ya()

            if fromUnit == 'miles' and toUnit == 'meter':
                convValue.converter_Mi_to_Me()

            if fromUnit == 'yard' and toUnit == 'miles':
                convValue.converter_Ya_to_Mi()

            if fromUnit == 'yard' and toUnit == 'meter':
                convValue.converter_Ya_to_Me()

            if fromUnit == 'meter' and toUnit == 'miles':
                convValue.converter_Me_to_Mi()

            if fromUnit == 'meter' and toUnit == 'yard':
                convValue.converter_Me_to_Ya()
        else:
            print (fromUnit.lower()+" can not convert "+ toUnit.lower())
except Exception as e:
    print (e)

# try:
#     converter = int (raw_input("Enter your converter type"))
#     temp_C = int (raw_input("Enter value"))
#     



# except Exception as e:
#     print (e)
