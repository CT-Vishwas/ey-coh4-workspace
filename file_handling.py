# fh = open("./data/sample.csv")
# # data = fh.read()
# data = fh.readlines()
# print(data)
# fh.close()

# using context manager
try: 
    with open("./data/sample1.csv", "x") as fh:
        data = fh.read()
        print(data)
except FileNotFoundError:
    print("file you are trying to read does not exist")
except Exception:
    print("General Exception Occured")
finally:
    print("Finally is called")