import re
import argparse

class adif(object):
    '''
    adif Parsing class
    '''

    def __init__(self, fname):
        '''
        Initializer
        :param fname: Filename of the ADIF file to parse
        '''
        self.fname = fname
        self.ifp = open(fname, 'rt')

    def __iter__(self):
        return self

    def __next__(self):
        '''
        Iterator
        :return:    a Line from the ADIF file. You need to check if it is a header or a data line
        '''
        line = self.ifp.readline()
        if line=='':
            self.reset_file_pointer()
            raise StopIteration
        else:
            return line

    def reset_file_pointer(self):
        self.ifp.seek(0,0)

    def parse_line(self, line):
        '''
        Parse the line. If the line is an ADIF data record parse it and return a dictionary with the data.
        The data is all Uppercase and space stripped (Makes call-sign and frequency easier downstream).
        :param line: Regex is used to check it is an ADIF data line not a header
        :return: A dictionary of fields and data values.
        '''
        d = {}
        re_fld = re.compile(r'[<]([a-z_]+)[:]([0-9]+)[>]([A-Za-z0-9\.]+)')
        data = re_fld.findall(line)
        for a in data:
            d[a[0]] = str(a[2]).upper().lstrip().rstrip()
        return d


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process Adif File.')
    parser.add_argument('--file', dest='adif_file',
                        default='NoFile.adif',
                        help='Enter the name of the adif file')

    args = parser.parse_args()
    a = adif(args.adif_file)
    lines = 2000
    cnt=1618
    for l in a:
        cnt=cnt-1
        fields = a.parse_line(l)
        if cnt==0:
            junk=1
        if 'call' in fields and 'mode' in fields and 'freq' in fields:
            print(str.format('{} {} {}',fields['call'],fields['freq'],fields['mode']))
            lines -= 1
            if lines < 0:
                break
