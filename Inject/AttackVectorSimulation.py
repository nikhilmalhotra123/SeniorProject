import json
import random
import requests
from Inject import Inject
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class AttackVectorSimulation:

    obj = []
    attack_type = ""
    number_of_threats = 0

    def __init__(self, input_obj, input_attack, input_threats):
        self.obj = input_obj
        self.attack_type = input_attack
        self.number_of_threats = input_threats

    def insert_threats(self):

        threats = []
        urls = []
        emailWAttach = []

        # Finds emails with references to attachments to put attachment threat
        if self.attack_type == "attachment":
            a = 0
            for i in self.obj:
                if i['message'].find("attach") + i['message'].find("attachment") + i['message'].find("attached") > 0:
                    emailWAttach.append(self.obj[a])
                a += 1
            for i in range(0, self.number_of_threats):
                threats.append(random.randint(0, len(emailWAttach)))

        else:
            for i in range (0, self.number_of_threats):
                threats.append(random.randint(0, len(self.obj)))

        # Gets an updated list of malicious urls
        if self.attack_type == "url":
            r = requests.get('https://isc.sans.edu/feeds/suspiciousdomains_High.txt', auth=('user', 'pass'))
            list = r.text.split("\n")
            for url in list:
                if url[0:1] != "#" and url != "Site":
                    urls.append(url)

        # Injects the threats
        for i in threats:
            currentEmail = self.obj[i]['message']
            self.obj[i]['attachment'] = ""

            # Determines which threat needs to be inserted and inserts it
            if self.attack_type == "email":
                # Replaces the end of an email address with a fake email
                startFrom = currentEmail.find("From:")
                firstEnd = currentEmail.find("\n", startFrom)
                body = currentEmail[startFrom + 6:firstEnd]
                at = body.find("@")
                self.obj[i]['message'] = self.obj[i]['message'].replace(body, body[0:at] + "@hacked.com")

            elif self.attack_type == "url":
                # Adds message to end of email
                start = currentEmail.find("http")
                end = currentEmail.find(" ", start)
                insertUrl = urls[random.randint(0, len(urls)-1)]
                self.obj[i]['message'] += currentEmail[0:start] + " HERE IS THE BAD URL https://www." + insertUrl + " " + currentEmail[end:len(currentEmail)]

            elif self.attack_type == "attachment":
                # Adds attachment as another key, value pair
                self.obj[i]['attachment'] = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

        # Updates global email storage with new email set
        Inject.obj = self.obj

