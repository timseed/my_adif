import re
from adif_qso import *

class foc(object):
    def __init__(self):
        # Purpose of this class is to parse the FOC CW Membership list
        # This text can be extracted from http://www.g4foc.org/members
        self.junk = 0
        self.members = []

    def parse(self, filename='members.txt'):
        with open(filename, "r") as infile:
            for line in infile:
                if re.match(r'^[0-9]+', line):
                    # print("Like looks Ok" + line)
                    parts = line.split('|')
                    for cs in parts:
                        # print(str.format('<{}>',cs))
                        found = re.match(r'([0-9]+)[ ]+[ A ]?([A-Z0-9]+)[ ]+([A-Za-z ]+)', line)
                        if found is not None:
                            print(str.format('Call {}', found.groups()[1]))
                            self.members.append(found.groups()[1])


if __name__ == "__main__":
    fo = foc()
    fo.parse()
    #Now load my ADIF File
    qso_check = adif_qso('a45wg.adif')
    for cs in fo.members:
        print("Checking "+cs)
        qso_check.check_call(cs)

