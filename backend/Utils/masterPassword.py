import uuid

SHIF = [
    68,  #'D'
    111, #'o'
    114, #'r'
    115, #'s'
    97,  #'a'
    45,  #'-'
    67,  #'C'
    111, #'o'
]

def get_master_password():
    mac = uuid.getnode()
    mac = str(mac)
    master_pass = ''
    for i,char in enumerate(mac):
        asci = ord(char)
        asci = (asci + SHIF[i%len(SHIF)]) + i
        asci = asci % (125 - 33) + 33
        master_pass = master_pass + chr(asci)

    return master_pass
5


if __name__ == '__main__':
    print(get_master_password())