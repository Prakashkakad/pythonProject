# import re
# import pandas as pd

# # Load the Excel file
# excel_file = 'C:/Users/wowse/PycharmProjects/pythonProject/email_to_sort.xlsx'
# df = pd.read_excel(excel_file)

# # Assuming emails are in a column named 'Email'
# emails = df['Email'].tolist()

# # Comprehensive regular expression pattern for validating an email
# email_pattern = re.compile(
#     (r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# )

# # Function to filter out incorrect emails
# def filter_emails(email_list):
#     correct_emails = [email for email in email_list if email_pattern.match(email)]
#     incorrect_emails = [email for email in email_list if not email_pattern.match(email)]
#     return correct_emails, incorrect_emails

# # Using the function to sort the emails
# correct, incorrect = filter_emails(emails)

# print("Correct emails:", correct)
# print("Incorrect emails:", incorrect)
e = int(input("Please Enter your age : "))