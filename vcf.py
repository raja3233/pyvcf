def vcfReader(file):
    '''Reads the contact file and returns all text'''
    file_obj = open(file,'r')
    contacts_data = file_obj.read()
    return contacts_data

def vcfParser(text):
    '''Takes Contacts text and return records of contacts'''
    import re
    recordRE = re.compile(r"BEGIN:VCARD\s(?:.*\s)+?END:VCARD")
    records= recordRE.findall(text)
    contacts ={}
    for record in records:
        fnRE = re.compile(r'(FN):(.*)')
        preRE = re.compile(r'(pref):(.*)')
        nameRecord = fnRE.findall(record)
        numberRecord = preRE.findall(record)
        contactName = nameRecord[0][1] if nameRecord else None
        contactNumber = numberRecord[0][1].replace('\xa0'," ") if numberRecord else None
        contacts[contactName] = contactNumber
    return contacts
