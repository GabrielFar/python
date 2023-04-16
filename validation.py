# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# # if (username) and ("." in domain):
# if (username) and (domain.endswith("gmail.com")):
#     print("Valid")
# else:
#     print("Invalid")

# ---------------------------------------------------------------------------------------------------------------------

import re

email = input("What's your email? ").strip()
# regex
# \w  = numeros e letras
if re.search(r"^[\w.]+@(gmail|hotmail)\.com$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
