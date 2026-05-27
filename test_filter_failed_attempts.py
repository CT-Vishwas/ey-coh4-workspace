d1 = {
    "vishwas": 9,
    "john": 2,
    "rani": 5,
    "dheeraj": 1
}

print(d1)
# l1 = list(filter(lambda x: x[1]>3, d1.items()))
# Filtering a list using list comprehension
l1 = [(k,v) for k,v in d1.items() if v > 3]
# print(l1)
# d2 = {}
# d2.update(l1)
# print(d2)
# filtering a dictionary using dictionary comprehension
d2 = {k:v for k,v in d1.items() if v > 3}
print(d2)