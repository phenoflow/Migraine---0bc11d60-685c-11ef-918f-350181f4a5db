# phekb, 2024.

import sys, csv, re

codes = [{"code":"346.1","system":"icduncat"},{"code":"346.11","system":"icduncat"},{"code":"346.12","system":"icduncat"},{"code":"346.13","system":"icduncat"},{"code":"346.7x","system":"icduncat"},{"code":"G43.0x","system":"icduncat"},{"code":"346","system":"icduncat"},{"code":"346.01","system":"icduncat"},{"code":"346.02","system":"icduncat"},{"code":"346.03","system":"icduncat"},{"code":" 346.5x","system":"icduncat"},{"code":" 346.6x","system":"icduncat"},{"code":"G43.1x","system":"icduncat"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('migraine-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["migraine---icduncat-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["migraine---icduncat-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["migraine---icduncat-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
