import secrets
import string

def generate_password(length):
  # Get all the printable ASCII characters
  chars = string.printable

  # Remove whitespace characters
  chars = chars.replace(" ", "")
  chars = chars.replace("\t", "")
  chars = chars.replace("\n", "")
  chars = chars.replace("\r", "")

  # Generate a random password
  password = ""
  for _ in range(length):
    password += secrets.choice(chars)

  return password

# Generate a password with 10 characters
password = generate_password(10)
print(password)
