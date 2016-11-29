import re


class adif(object):
    def __init__(self, fname):
        self.fname = fname

        self.ifp = open(fname, 'rt')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.ifp.readline()
        if line is None:
            raise StopIteration
        else:
            return line

    def parse_line(self, line):
        d = {}
        re_fld = re.compile(r'[<]([a-z_]+)[:]([0-9]+)[>]([A-Za-z0-9\.]+)')
        data = re_fld.findall(line)
        for a in data:
            d[a[0]] = a[2]
        return d


if __name__ == "__main__":
    a = adif('/Users/tim/PycharmProjects/my_adif/a45wg.adif')
    lines = 20
    for l in a:
        fields = a.parse_line(l)
        if 'call' in fields and 'mode' in fields and 'freq' in fields:
            print(str.format('{} {} {}',fields['call'],fields['freq'],fields['mode']))
            lines -= 1
            if lines < 0:
                break
