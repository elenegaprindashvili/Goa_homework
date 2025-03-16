def validate_pin(pin):
    if not pin.isdigit(): #pin mxolod cifrebia.
        return False
    if len(pin) != 4 and len(pin) != 6: #pinis sigrdze marto unda iyos 4 an 6
        return False
    return True