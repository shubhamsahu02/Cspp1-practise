"""Compare_AB"""
def compare_ref(parameter):
    """Defining the function for the type"""
    return type(parameter)
VARA = "12"
VARB = 12

STRING_TYPE = "string"
if compare_ref(VARA) == compare_ref(STRING_TYPE)  or compare_ref(VARB) == compare_ref(STRING_TYPE):
    print("String Involved")
elif VARA > VARB:
    print("Bigger")
elif VARA == VARB:
    print("Equal")
else:
    print("Smaller")
