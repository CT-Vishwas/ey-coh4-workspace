
inp_str = input("Enter input string: ")

char_counts = {}
for chr in inp_str:
    char_counts[chr] = char_counts.get(chr, 0) + 1

print(f"Frequencies: \n{char_counts}")