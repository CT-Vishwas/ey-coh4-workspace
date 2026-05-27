def is_nonlocal_ip(ip_address):
    fields = ip_address.split(".") 
    if (fields[0] == "10") or (fields[0] == "172" and int(fields[1]) >= 16 and int(fields[1]) <= 31) or (fields[0] == "192" and fields[1] == "168") :
        return False
    
    return True
    
def username_extracter(email):
    return email[:email.find('@')]

def add(a,b):
    return a + b

if __name__ == '__main__':
    uname = username_extracter("vishwas@cloudthat.com")
    print(f"Username is: {uname}")

    print(f"Sum of 23 & 45 is {add(23,45)}")