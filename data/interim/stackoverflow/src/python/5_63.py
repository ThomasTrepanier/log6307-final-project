import csv

class CSV_Translater(object):
    """ Output file-like object that translates characters. """
    def __init__(self, f, old, new):
        self.f = f
        self.old = old
        self.new = new
    def write(self, s):
        self.f.write(s.replace(self.old, self.new))
    def close(self):
        self.f.close()
    def flush(self):
        self.f.flush()

my_new_row = ['6', 'abc6', 'xyz6']


with open('data.csv', "r+") as filehandle:
    reader = csv.reader(filehandle)
    with open('out_test.csv', "w") as opfile:
        translater = CSV_Translater(opfile, ',', ', ')
        writer = csv.writer(translater, delimiter=',')
        for row in reader:
            writer.writerow(row)
        writer.writerow(my_new_row)
