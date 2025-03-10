import win32com.client
from win32com.client import WithEvents
import re

class EmailEventHandler:
    def OnOpen(self):
        """Triggered when an email is opened."""
        email_subject = self.Subject
        email_sender = self.SenderEmailAddress
        email_body = self.Body

        print(f"Email Opened: {email_subject}")
        print(f"From: {email_sender}")
        
        # Analyze the email content
        self.analyze_email(email_body)

    def analyze_email(self, body):
        """Analyze the email body for safety."""
        print("Analyzing email content...")
        links = re.findall(r'(https?://[^\s]+)', body)
        print(f"Links found: {links}")
        
        if any("suspicious-domain" in link for link in links):  # Replace with actual checks
            print("Warning: This email contains unsafe links!")
        else:
            print("The email seems safe.")

def monitor_outlook():
    import pythoncom

    pythoncom.CoInitialize()
    """Set up monitoring for opened emails in Outlook."""
    outlook = win32com.client.DispatchWithEvents("Outlook.Application", EmailEventHandler)
    print("Monitoring Outlook for opened emails...")

    # Make Outlook visible
    outlook_explorer = outlook.ActiveExplorer()
    if outlook_explorer is None:
        # If no active explorer, create a new one
        outlook.Session.GetNameSpace("MAPI").GetDefaultFolder(6).Display()
    else:
        # Bring the existing explorer to the front
        outlook_explorer.Display()
    
    # Keep the script running
    while True:
        pythoncom.PumpWaitingMessages()

if __name__ == "__main__":
    monitor_outlook()