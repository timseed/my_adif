from adif import adif
import argparse

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


    def header():
        print(str.format("QSO\tDate\tTime\tFreq\tMode\tSent\tRcv"))


    def format_date(dt_str):
        # The Date string looks like this
        #    20160728
        if len(dt_str) == 8:
            new_date = dt_str[0:4] + '-' + dt_str[4:-2] + '-' + dt_str[6:]
            return new_date
        else:
            return dt_str


    def format_time(tm_str):
        # The time string looks like this
        #    122103
        if len(tm_str) == 6:
            new_time = tm_str[0:2] + ':' + tm_str[2:-2] + ':' + tm_str[4:]
            return new_time
        else:
            return tm_str


    args = parser.parse_args()
    a = adif.adif(args.adif_file)
    doneheader = False
    if len(args.call):
        CALL = str(args.call).upper()
        rec = 0
        for l in a:
            rec = rec + 1
            if rec % 5 == 0 and args.debug == True:
                print("Processed " + str(rec))
            fields = a.parse_line(l)
            if 'call' in fields and 'mode' in fields and 'freq' in fields \
                    and 'qso_date' in fields and 'time_on' in fields \
                    and 'rst_sent' in fields and 'rst_rcvd' in fields:
                if fields['call'] == CALL:
                    if doneheader == False:
                        header()
                        doneheader = True
                        print(str.format('{}\t{}\t{}\t{}\t{}\t{}\t{}', fields['call'], format_date(fields['qso_date']),
                                         format_time(fields['time_on']), fields['freq'], fields['mode'],
                                         fields['rst_sent'], fields['rst_rcvd']))
                        # else:
                        #    print("Bad ADIF Format")
    else:
        print("Error: No Callsign given.")

print("Finished")
