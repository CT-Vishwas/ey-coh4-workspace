def is_nonlocal_ip(ip_address: str) -> bool:
    '''
    Returns if an IP Address is non-local(public)
    '''
    fields = ip_address.split(".") 
    if (fields[0] == "10") or (fields[0] == "172" and int(fields[1]) >= 16 and int(fields[1]) <= 31) or (fields[0] == "192" and fields[1] == "168") :
        return False
    
    return True
    
def username_extracter(email: str) -> str:
    '''
    Returns username from email id.
    '''
    return email[:email.find('@')]

def add(a,b, c=10):
    return a + b + c

if __name__ == '__main__':
    uname = username_extracter("vishwas@cloudthat.com")
    print(f"Username is: {uname}")

    print(f"Sum of 23 & 45 & c is {add(23,45)}")

    print(f"Sum of 23 & 45 & c=100 is {add(23,45, c=100)}")