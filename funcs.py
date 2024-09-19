##THESE ARE THE FUNCTIONS USED TO CONVERT THE NUMBERS TO THE DIFFERENT SYSTEMS


#To convert from decimal to binary
def decimal_to_binary(decimal):
    number = bin(decimal)[2:]
    return number

#to convert from decimal to hex...
def decimal_to_hex(hexa):
    number = hex(hexa)[2:].upper() 
    return number

#from decimal to octal...
def decimal_to_octal(octal):
    number = oct(octal)[2:]
    return number

##TO CONVERT FROM BINARY TO OTHER SYSTEMS
#from binary to decimal
def binary_to_decimal(bina):
    number = int(bina, 2)
    return number

#from binary to hex...
def binary_to_hex(bina):
    new = binary_to_decimal(bina)
    number = decimal_to_hex(new)
    return number

#from binary to aoctal
def binary_to_octal(bina):
    new = binary_to_decimal(bina)
    number = decimal_to_octal(new)
    return number

##FROM HEXADECIMAL TO OTHER SYSTEMS
#from hexa to decimal
def hexa_to_decimal(hexa):
    number = int(hexa, 8)
    return number

#from hexa to binary
def hexa_to_binary(hexa):
    new = hexa_to_decimal(hexa)
    number = decimal_to_hex(new)
    return number

#from hexa to octal
def hexa_to_octal(hexa):
    new = hexa_to_decimal(hexa)
    number = decimal_to_octal(new)
    return number

##FROM OCTAL TO OTHER SYSTEMS
#from octal to decimal
def octal_to_decimal(octal):
    number = int(octal, 16)
    return number

#from octal to binary:
def octal_to_binary(octal):
    new = octal_to_decimal(octal)
    number = decimal_to_binary(new)
    return number

#from octal to hexa
def octal_to_hexa(octal):
    new = octal_to_decimal(octal)
    number = decimal_to_hex(new)
    return number
