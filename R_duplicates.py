def duplicates(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

input_str = "TOYOTA COROLLA"
output_str = duplicates(input_str)
print("Original string: " + input_str)
print("String after removing duplicates: " + output_str)

