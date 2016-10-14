import re
def vcfReader(file):
    '''Reads the contact file and returns all text'''
    file_obj = open(file,'r')
    contacts_data = file_obj.read()
    return contacts_data

def vcfParser(text):
    '''Takes Contacts text and return records of contacts'''
    #Regular expression for each VCARD
    recordRE = re.compile(r"BEGIN:VCARD\s(?:.*\s)+?END:VCARD") 
    records= recordRE.findall(text)
    contacts ={}
    for record in records:
        contactName = _fetch_value('FN', record)
        contactNumber = _fetch_value('pref', record)
        contacts[contactName] = contactNumber
    return contacts

def _fetch_value(key, record):
    '''Take the type and return the value of the type'''
    regex = re.compile(r'(%s):(.*)' % (key))
    resultGroup = regex.findall(record)
    value = resultGroup[0][1].replace('\xa0'," ") if resultGroup else None
    return value
