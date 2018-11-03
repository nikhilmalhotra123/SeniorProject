from email.mime.text import MIMEText
import random
from Inject import Inject


class Workflow:

    # Helper methods
    def generate_from_email(self):
        from_emails = ["noreply@microsoft.com", "noreply@amazon.com", "noreply@facebook.com", "noreply@google.com"]
        return from_emails[random.randint(0, len(from_emails) - 1)]

    def generate_subject(self):
        subjects = ["Password Reset", "Invoice for...", "Your Order Has Been Shipped", "Your Order Is On Its Way", "Order Confirmation for Order Number #" + str(random.randint(10000000000, 99999999999))]
        return subjects[random.randint(0, len(subjects) - 1)]

    # Creates and returns workflow emails
    def create_workflow_emails(self):
        # Change to user input
        number_of_emails = 10
        emails = []

        for i in range(number_of_emails):
            text = "This is a placeholder"

            msg = MIMEText(text)
            msg["From"] = self.generate_from_email()
            msg["To"] = "Placeholder"
            msg["Subject"] = self.generate_subject()
            temp = {"file": 12345, "message": str(msg), "attachment": ""}

            emails.append(temp)

        return emails
