

import random
import csv


CSV_FILE = 'testFile1.csv'
# csv file to work with.

def main():

    csv_read()

    csv_write()

    csv_read()

    

def csv_write():
# append an entry to the csv file.

    entry_index = random.randint(1, 1000)
    entry_name = 'billy butcher'
    entry_color = 'black'
    entry_food = 'ice cream'

    csv_file = open(CSV_FILE, 'a')
    csv_file.write(f'{entry_index},{entry_name},{entry_color},{entry_food}\n')
    #csv_writer = csv.writer(csv_file)
    #csv_writer.writerow(['22', 'billy butcher', 'black', 'ice cream'])
    # add an entry to csv file.

    csv_file.close()
    # close csv file.


def csv_read():
# read csv file and display formatted output.

    csv_file = open(CSV_FILE)
    parsed_csv = csv.reader(csv_file)
    # open and parse csv file. 

    line_number = 0
    for line in parsed_csv:
    # iterate over file lines. 

        #print(line)

        if line_number == 0:
            print()
            print(f'{"# " * 36}#')
            print('#{:^8} {:^20} {:^20} {:^20}#'.format(line[0], line[1],
                line[2], line[3]))
            print(f'{"# " * 36}#')
        # print column headers.

        else:
            print('#{:^8}#   {:<17}#   {:<17}#   {:<17}#'.format(line[0], 
                line[1], line[2], line[3]))
        # print data in file. 

        line_number += 1
        # increments line counter. 

    else:
        print(f'{"# " * 36}#')
        print()
    # print footer. 

    csv_file.close()
    # close file after getting info. 

main()