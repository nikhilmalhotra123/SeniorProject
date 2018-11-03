import json


class Inject:
    obj = []

    # Files
    read_File = '/Users/nikhilmalhotra/emails.json'
    write_File = '/Users/nikhilmalhotra/emailsTest.json'
    attach_File = "/Users/nikhilmalhotra/Downloads/eicar.com.txt"

    # Reads JSON file
    def read(self):
        # Loads JSON version of Enron
        with open(self.read_File, 'r') as fp:
            self.obj = json.load(fp)

    # Overwrites final file with threats
    def write(self):
        with open(self.write_File, 'w+') as fp:
            self.obj = json.dump(self.obj, fp)

    # Helper methods
    def get_obj(self):
        return self.obj

    def set_obj(self, obj):
        self.obj = obj
