# Save this code in a file named emails.py
import re
from collections import defaultdict

def solution(S, C):
    # Split the input string into individual names
    names = S.split(", ")

    # Normalize the company name
    company = C.lower()

    # Dictionary to track the number of times an email has been used
    email_count = defaultdict(int)
    
    # Result list to collect the output
    result = []

    for name in names:
        # Split the name into parts: first, optional middle, and last
        name_parts = name.split()

        # First name initial
        first_initial = name_parts[0][0].lower()

        # Middle name initial (if exists)
        middle_initial = name_parts[1][0].lower() if len(name_parts) == 3 else ""

        # Last name processing (sanitize and truncate)
        last_name = name_parts[-1]
        last_name = last_name.replace('-', '')  # remove hyphens
        last_name = last_name[:8].lower()  # truncate to 8 characters and lowercase
        
        # Build the email address
        email_base = first_initial + (middle_initial if middle_initial else '') + last_name
        email_address = email_base + "@" + company + ".com"

        # Handle duplicates by checking the email count
        email_count[email_address] += 1
        if email_count[email_address] > 1:
            email_address = email_base + str(email_count[email_address]) + "@" + company + ".com"

        # Add the result in the required format
        result.append(f"{name} <{email_address}>")
    
    # Join all results with ", " and return the final string
    return ", ".join(result)

# Example test case
S = "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker"
C = "Example"

# Call the solution function and print the result
print(solution(S, C))
