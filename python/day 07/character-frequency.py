v = input("Enter string: ").lower()

freq = {}

for char in v:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for char, count in freq.items():
    print(f"{char} : {count}")