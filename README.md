# Projects
projects built with python
This password generator uses the string.printable constant, which contains all the printable ASCII characters. It then removes whitespace characters and generates a random password by choosing random characters from the remaining set of characters using the secrets.choice() function.

The secrets.choice() function is similar to the random.choice() function, but it uses the system's secure random number generator, so the generated passwords are cryptographically secure.

Note that the length of the generated password may be less than the specified length, because the secrets.choice() function only generates characters that are safe to use in URLs and may not generate all the possible characters. However, this should not be a problem in most cases.
