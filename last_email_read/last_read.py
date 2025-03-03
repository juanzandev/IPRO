import imaplib

# Replace these with your credentials.
USERNAME = ""
# For Gmail, you might need to use an App Password.
PASSWORD = ""

# Connect to Gmail's IMAP server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

try:
    mail.login(USERNAME, PASSWORD)
except imaplib.IMAP4.error as e:
    print("Login failed:", e)
    exit(1)

# Select the inbox
mail.select("inbox")

# Search for all emails in the inbox
status, data = mail.search(None, "ALL")
email_ids = data[0].split()

if not email_ids:
    print("No emails found in the inbox.")
else:
    # Get the last email ID (assuming the list is in ascending order)
    last_email_id = email_ids[-1]

    # Fetch the flags for the last email
    status, data = mail.fetch(last_email_id, "(FLAGS)")
    if status != "OK":
        print("Failed to fetch email flags.")
    else:
        # The fetched data contains the flags in a string format.
        # Check if the b'\\Seen' flag is in the data.
        if b"\\Seen" in data[0]:
            print("opened")
        else:
            print("not opened")

# Logout from the server
mail.logout()
