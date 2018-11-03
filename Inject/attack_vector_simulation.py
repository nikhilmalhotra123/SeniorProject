# -*- coding: utf-8 -*-
"""
Inserts the different type of threats into the Enron dataset
"""

import random
import requests
from inject import Inject


class AttackVectorSimulation:
    """Class"""
    obj = []
    attack_type = ""
    number_of_threats = 0
    emails = 0
    urls = 0
    attachments = 0

    def __init__(self, input_obj, emails, urls, attachments):
        self.obj = input_obj
        self.emails = emails
        self.urls = urls
        self.attachments = attachments

    def insert_threats(self):
        """Inserts the threats into the emails"""
        threats_attach = []
        threats_email = []
        threats_url = []
        urls = []
        email_with_attach = []

        # Finds emails with references to attachments to put attachment threat
        count = 0
        for i in self.obj:
            if i['message'].find("attach") + i['message'].find("attachment") + \
                    i['message'].find("attached") > 0:
                email_with_attach.append(self.obj[count])
            count += 1

        # Randomly selects which emails to modify
        for i in range(0, self.attachments):
            threats_attach.append(random.randint(0, len(email_with_attach)))

        for i in range(0, self.emails):
            threats_email.append(random.randint(0, len(self.obj)))

        for i in range(0, self.urls):
            threats_url.append(random.randint(0, len(self.obj)))

        # Gets list of malicious urls
        url_list = requests.get('https://isc.sans.edu/feeds/suspiciousdomains_High.txt',
                                auth=('user', 'pass')).text.split("\n")
        for url in url_list:
            if url[0:1] != "#" and url != "Site":
                urls.append(url)

        # Inserts email threats by replace end of an email address with a fake email
        for i in threats_email:
            try:
                current_email = self.obj[i]['message']
                self.obj[i]['attachment'] = ""

                start_from = current_email.find("From:")
                first_end = current_email.find("\n", start_from)
                body = current_email[start_from + 6:first_end]
                at_loc = body.find("@")
                self.obj[i]['message'] = self.obj[i]['message'].replace(body, body[0:at_loc]
                                                                        + "@hacked.com")
            except Exception:
                pass

        # Inserts malicious urls to the end of emails
        for i in threats_url:
            try:
                current_email = self.obj[i]['message']
                self.obj[i]['attachment'] = ""

                start = current_email.find("http")
                end = current_email.find(" ", start)
                insert_url = urls[random.randint(0, len(urls) - 1)]
                self.obj[i]['message'] += current_email[0:start] + " HERE IS THE BAD URL https://www."\
                                          + insert_url + " " + current_email[end:len(current_email)]
            except Exception:
                pass

        # Inserts attachments as another key, value pair
        for i in threats_attach:
            try:
                self.obj[i]['attachment'] = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-" \
                                            "ANTIVIRUS-TEST-FILE!$H+H*"
            except Exception:
                pass

        # Updates global email storage with new email set
        Inject.obj = self.obj
