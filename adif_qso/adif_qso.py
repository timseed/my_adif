from adif import adif
import argparse


class adif_qso(object):
    '''
    Check an ADIF file for a previous QSO
    This can be useful for QSL card work - or checking FOC Members you have spoken to etc
    '''

    def __init__(self, adif_filename, debug=False):
        '''
        Initialize the class
        :param adif_filename: needs and ADIF Filename
        :param debug: Defaults to False
        '''
        self.a = adif(adif_filename)
        self.doneheader = False
        self.debug = debug

    def check_call(self, call, toprint=False):
        '''
        Check the Call

        :param call: the Callsign say a45wg or m0fgc
        :param toprint: True or False. If True then the basic QSO data is printed to the screen.
                        if False: No screen output is produced
        :return:   If matched - an array with a dictionary of the QSO Details is returned.
        '''

        previous_qso=[]
        CALL = str(call).upper().lstrip().rstrip()
        rec = 0
        for l in self.a:
            rec += 1
            if rec % 5 == 0 and self.debug == True:
                print("Processed " + str(rec))
            fields = self.a.parse_line(l)
            if 'call' in fields and 'mode' in fields and 'freq' in fields \
                    and 'qso_date' in fields and 'time_on' in fields \
                    and 'rst_sent' in fields and 'rst_rcvd' in fields:
                if fields['call'] == CALL:
                    if toprint == True:
                        if self.doneheader == False:
                            self.header()
                            self.doneheader = True
                            print(str.format('{}\t{}\t{}\t{}\t{}\t{}\t{}', fields['call'],
                                             self.format_date(fields['qso_date']),
                                             self.format_time(fields['time_on']), fields['freq'], fields['mode'],
                                             fields['rst_sent'], fields['rst_rcvd']))

                    previous_qso.append(fields)
        return previous_qso

    def header(self):
        '''
        Simple Header for Output
        :return:  None
        '''
        print(str.format("QSO\tDate\tTime\tFreq\tMode\tSent\tRcv"))

    def format_date(self, dt_str):
        '''
        Internal Date reformatting.
        by default ISO Int format not locale
        :param dt_str:  datestring looks like 20160728
        :return: YYYY-MM-DD
        '''
        if len(dt_str) == 8:
            new_date = dt_str[0:4] + '-' + dt_str[4:-2] + '-' + dt_str[6:]
            return new_date
        else:
            return dt_str

    def format_time(self, tm_str):
        '''
        Internal Time reformatting.
        by default ISO Int Time format not locale
        :param tm_str: timestring looks like 122103
        :return:   HH:MM:SS
        '''
        if len(tm_str) == 6:
            new_time = tm_str[0:2] + ':' + tm_str[2:-2] + ':' + tm_str[4:]
            return new_time
        else:
            return tm_str


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process Adif File.')
    parser.add_argument('--file', dest='adif_file',
                        default='NoFile.adif',
                        help='Enter the name of the adif file')

    parser.add_argument('--call', dest='call',
                        default='',
                        help='Enter the name of the Call Sign you want')
    parser.add_argument('--debug', dest='debug',
                        default='True',
                        help='Turn on Debugging')

    args = parser.parse_args()
    qso_check = adif_qso(args.adif_file)
    data=qso_check.check_call(args.call, toprint=True)
