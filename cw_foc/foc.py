import re

from adif_qso import adif_qso


class foc(object):
    '''
    First Class Operators - a CW club dedicated to good operating, skills and friendship.
    '''


    def __init__(self):
        '''
        Purpose of this class is to parse the FOC CW Membership list
        This text can be extracted from http://www.g4foc.org/members
        The text is straight foward with the exception of the Associate member flag which results in the REGEX
        Being a little more complex than it may have needed. The CallSign definition does not handle /P /M etc
        '''
        self.junk = 0
        self.members = []

    def parse(self, filename='members.txt'):
        '''
        parse the FOC text file.

        :param filename: defaults to 'members.txt'
        :return:  Nothing
        '''
        with open(filename, "r") as infile:
            for line in infile:
                if re.match(r'^[0-9]+', line):
                    # print("Like looks Ok" + line)
                    parts = line.split('|')
                    for cs in parts:
                        # print(str.format('<{}>',cs))
                        found = re.match(r'([0-9]+)[ ]+[A]?[ ]+([A-Z0-9]+)', cs.lstrip())
                        if found is not None:
                            #print(str.format('Call {}', found.groups()[1]))
                            self.members.append(found.groups()[1])


if __name__ == "__main__":
    fo = foc()
    fo.parse()
    #Now load my ADIF File
    qso_check=adif_qso('a45wg.adif')
    for cs in fo.members:
        #print("Checking "+cs)
        qso_data=qso_check.check_call(cs)
        if qso_data is not None:
            print(str.format("Worked FOC {}",qso_data['call']))
