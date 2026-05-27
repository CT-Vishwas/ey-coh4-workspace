def username_extracter(email):
    return email[:email.find('@')]

def add(a,b):
    return a + b

if __name__ == '__main__':
    uname = username_extracter("vishwas@cloudthat.com")
    print(f"Username is: {uname}")

    print(f"Sum of 23 & 45 is {add(23,45)}")