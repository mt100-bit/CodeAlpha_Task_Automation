import re

#Read the text file
with open("sample_text.txt", "r") as file:
    text = file.read()

#Extract email addresses
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

#Display the extracted email addresses
print(emails)  

#Save the extracted emails to a new file
with open("extracted_emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")


print("Email addresses saved successfully.")