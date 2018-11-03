# MailHarness

* The goal of this project is to insert threats in the Enron email dataset to simulate cyberattacks and create workflow emails
*
* This code can change the second half of an email address while keeping the Sender's name the same.
* For example, johndoe@enron.com will be changed to johndoe@hacked.com
* The person receiving the email will still see it as being set by John Doe but in reality, it is a malicious email
*
* This code can also add/replace urls in the body of the emails with a malicious url from the list found at https://isc.sans.edu/feeds/suspiciousdomains_High.txt
*
* Third, this code can insert an attachment that simulates a virus and is used for testing purposes
*
* To Run the code:
* Run Main.py in terminal with the arguments in the respective order: email addresses, urls, attachments, and workflow emails
* For each argument, put the number of emails you want changed to insert that threat
*
* The following example will change the email address in 2 emails, insert urls in 4 emails, attach attachments in 3 emails, and create 6 workflow emails
* python3 Main.py 2 4 3 6
*
* Use -h for help
