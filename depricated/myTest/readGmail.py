import imaplib
import email
from email.header import decode_header

# Account credentials
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = "kalebaustgen@gmail.com"
PASSWORD = "dcaz lcxq amtm xraf"  # Use App Password if 2FA is enabled

def clean(text):
    """Clean text for creating folder names or filenames."""
    return "".join(c if c.isalnum() else "_" for c in text)

def get_recent_emails(n=10):
    try:
        # Connect to the server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        # Login to the account
        mail.login(EMAIL_ACCOUNT, PASSWORD)
        # Select the mailbox (in this case, inbox)
        mail.select("inbox")

        # Search for all emails
        status, messages = mail.search(None, "ALL")
        # Get the list of email IDs
        email_ids = messages[0].split()
        # Get the last n email IDs
        latest_email_ids = email_ids[-n:]

        for num in reversed(latest_email_ids):
            # Fetch the email by ID
            status, msg_data = mail.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    # Parse a bytes email into a message object
                    msg = email.message_from_bytes(response_part[1])
                    # Decode email sender
                    from_ = msg.get("From")
                    # Decode email subject
                    subject, encoding = decode_header(msg.get("Subject"))[0]
                    if isinstance(subject, bytes):
                        # If it's a bytes type, decode to str
                        subject = subject.decode(encoding if encoding else "utf-8")
                    print(f"From: {from_}")
                    print(f"Subject: {subject}")

                    # If the email message is multipart
                    if msg.is_multipart():
                        # Iterate over email parts
                        for part in msg.walk():
                            # Extract the content type of the email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            try:
                                # Get the email body
                                body = part.get_payload(decode=True).decode()
                                if content_type == "text/plain" and "attachment" not in content_disposition:
                                    # Print text/plain emails and skip attachments
                                    print(f"Body: {body}")
                            except:
                                pass
                    else:
                        # Extract content type of email
                        content_type = msg.get_content_type()
                        # Get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            print(f"Body: {body}")

                    print("=" * 50)

        # Close the connection and logout
        mail.close()
        mail.logout()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_recent_emails()
