from calpi import calpiinfo

# Create an instance of calpiinfo
pi_calculator = calpiinfo()

# Get user input
user_input = input("Input string or number: ")

# Call the binaryencode method on the instance to get the binary encoding
endcoding = pi_calculator.binaryencode(user_input)

# Print the binary encoding
print("Binary Encoding:", endcoding)

# Call the binarydecode method on the instance to decode the binary string
decoding = pi_calculator.binarydecode(endcoding)

# Print the decoded string
print("Decoded String:", decoding)
