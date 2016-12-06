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

    args = parser.parse_args()
    a = adif.adif(args.adif_file)
    if len(args.call):
        CALL=str(args.call).upper()
        rec=0
        for l in a:
            rec=rec+1
            if rec%5==0 and args.debug==True:
                print("Processed "+str(rec))
            fields = a.parse_line(l)
            if 'call' in fields and 'mode' in fields and 'freq' in fields and 'qso_date' in fields and 'time_on' in fields:
                if fields['call']==CALL:
                    print(str.format('{} {} {}',fields['call'],fields['freq'],fields['mode']))
            #else:
            #    print("Bad ADIF Format")
    else:
        print("Error: No Callsign given.")

print("Finished")