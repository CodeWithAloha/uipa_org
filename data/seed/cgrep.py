# cgrep.py - Grep for a string in the specified field of a CSV file.
#            Prints the first field and the specified field where the string
#            matches the value in the specified field.
#

import csv
import sys


def get_fields(csv_file):
    """Return a list of field names from csv_file."""
    with open(csv_file, "r") as fin:
        reader = csv.reader(fin)
        header = next(reader)

    return header

def load_data(csv_file):
    """Return a list of dicts from the rows in csv_file."""
    rs = []

    with open(csv_file, "r") as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            rs.append(row)

    return rs

def find_string(string, field, rows):
    """Print the first field and the field for rows where string is in
       field.
    """
    num_found = 0

    if len(rows) > 0:
        first_field = list(rows[0].keys())[0]
        for row in rows:
            if string.strip() in row[field].strip():
                num_found += 1
                print(f"{first_field}: {row[first_field]} => {row[field]}")

    print(f"Found {num_found} records", file=sys.stderr)

def main(string, field, csv_file):
    rows = load_data(csv_file)

    if len(rows) < 1:
        print(f"No records in {csv_file}", file=sys.stderr)
    else:
        field_names = list(rows[0].keys())
        if not field in field_names:
            print(f"{csv_file} does not have a {field} field", file=sys.stderr)
        else:
            find_string(string, field, rows)

def usage():
    print(f"usage: python {prog} (string field | -l) csv_file", file=sys.stderr)
    print(f"   Search for string in field of csv_file", file=sys.stderr)
    print(f"   or list fields of csv_file.", file=sys.stderr)


if __name__ == "__main__":
    prog = sys.argv[0]
    do_list = False
    string = ""
    field = ""
    csv_file = ""
    field_names = []

    if len(sys.argv) == 3:
        if sys.argv[1] == "-l":
            do_list = True
            csv_file = sys.argv[2]
    elif len(sys.argv) > 3:
        string = sys.argv[1]
        field = sys.argv[2]
        if string.startswith("-") or field.startswith("-"):
            csv_file = ""
        else:
            csv_file = sys.argv[3]

    if csv_file == "":
        usage()
        sys.exit(1)

    if do_list:
        field_names = get_fields(csv_file)
        for field in field_names:
            print(field, file=sys.stderr)
    else:
        main(string, field, csv_file)

