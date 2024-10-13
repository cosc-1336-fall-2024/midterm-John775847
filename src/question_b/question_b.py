#write functions here, don't add input('') statements here!
def get_miles_per_hour(kilometers, minutes):
    if (kilometers > 0 and minutes > 0):
        return (kilometers *  0.621371) / (minutes / 60)
    else:
        return "Invalid arguments"
