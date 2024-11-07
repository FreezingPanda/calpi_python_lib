import calpi
from calpi import calpiinfo


# Create an instance of the calpiinfo class
pi_calculator = calpiinfo()

# Get 20 digits of Pi
pi_digits = pi_calculator.calpi(20, 1000)

# Convert the digits to binary
pi_binary = pi_calculator.binaryencode(pi_digits)

# Decode the binary back to text
decoded_result = pi_calculator.binarydecode(pi_binary)

# Print the result
print(f"Original Pi digits: {pi_digits}")
print(f"Binary representation: {pi_binary}")
print(f"Decoded text: {decoded_result}")
