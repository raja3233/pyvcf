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
        contactName = fnRE.findall(record)[0][1]
        print contactName
    #     contactNumber = preRE.findall(record)[0][1]
    #     contacts[contactName] = contactNumber
    # return contacts


contacts_data = vcfReader('/Users/ganesh/Documents/contacts.vcf')
records = vcfParser(contacts_data)
print('records inthe contacts are', len(records))
print(contacts)
