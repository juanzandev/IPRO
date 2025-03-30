import imaplib
import email
from email.header import decode_header
import webbrowser 
import os

# account credentials
username = "kaustgen@hawk.iit.edu"
password = "gI_Love_c@ke_so_Much_54"

# office 365 IMAP server
imap_server = "outlook.office365.com"

# To create folders without spaces and special characters
def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL(imap_server, port=993)

# authenticate
imap.login(username, password)

