h = 6.626e-34
c = 3e8

def specific_charge(charge, mass):
    if mass == 0:
        return 0
    return abs(charge / mass)

def compton_wavelength(mass):
    if mass == 0:
        return 0
    return h / (mass * c)
