def remove_duplicates(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

# Example usage:
input_str = "HelloWorld"
output_str = remove_duplicates(input_str)
print(f"Original string: {input_str}")
print(f"String after removing duplicates: {output_str}")
