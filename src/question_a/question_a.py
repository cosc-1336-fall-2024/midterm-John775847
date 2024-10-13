#write functions here, don't add input('') statements here!

def get_assessment_value(property_value):
    return property_value * 0.6

def get_tax_assessed(acre_assesment):
    return round((acre_assesment/100)*0.72, 2)
    #Round to 2 digits because 100 ¢ in a $.
