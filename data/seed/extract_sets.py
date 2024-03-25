# extract_sets.py - Get unique sets of field data from a Public Body CSV file.
#                   Write them out to files. Write a CSV file that can be
#                   uploaded via the Admin website.
#

import csv
import sys
from itertools import chain


# Fields in a Public Body CSV file are:
field_names = [
    "id",
    "name",
    "email",
    "contact",
    "address",
    "url",
    "classification",
    "jurisdiction__slug",
    # old field name: "tags",
    "categories",
    "other_names",
    "website_dump",
    "description",
    "request_note",
    "parent__name",
]

def load_data(csv_file):
    """Return a list of dicts from the rows in csv_file."""
    rs = []
    with open(csv_file, "r") as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            rs.append(row)
    return rs

def fix_tag_field(value):
    """Returns a new value without blanks following commas separating multiple
       tag values.
    """
    tvs = [t.strip() for t in value.split(",")]
    new_value = ",".join(tvs)
    return new_value

def clean_str(s):
    return s.strip().replace('"', '')

def get_tag_values(atag):
    """Return a list of tags from atag.
       Tags composed of multiple words have the double quotes removed.
    """
    if type(atag) == str:
        return list(map(clean_str, atag.split(",")))
    return []

# Fix the classification in a row.
#   Before fix:
#     (out) 87: Department of Business Economic Development Tourism
#     (out) 88: Department of Business Economic Development Tourism
#   After fix:
#     rs[87]['classification'] # 'Department of Business, Economic Development & Tourism'
#     rs[88]['classification'] # 'Department of Business, Economic Development & Tourism'
def fix_dup_classf(row):
    """Modifies row by replacing a duplicate classification if needed.
       Returns nothing.
    """
    classf = row['classification']
    if classf.strip() == "Department of Business Economic Development Tourism":
        row['classification'] = "Department of Business, Economic Development & Tourism"

# Change tags field to categories field.
def tags_to_categories(row):
    """Modifies row by setting the categories field to fixed tags field value.
       Returns nothing.
    """
    row['categories'] = fix_tag_field(row['tags'])
    if 'tags' in row:
        del row['tags']

def save_to_file(lst, fn):
    """Write lst to fn."""
    with open(fn, 'w') as fout:
        for item in lst:
            fout.write(f"{item}\n")

def save_to_csv(lst, fn):
    """Write lst as CSV to fn."""
    with open(fn, 'w') as fout:
        writer = csv.DictWriter(fout, fieldnames=field_names)
        writer.writeheader()
        for item in lst:
            writer.writerow(item)

def main(csv_file):
    """Read in the data from csv_file. Extract the field values that we need to
       load into tables before public body data can loaded from a CSV file.
    """
    rs = load_data(csv_file)
    len(rs)

    # Get a list of unique parent names.
    p_names = set([ r['parent__name'] for r in rs if len(r['parent__name']) != 0 ])
    print("Saving parent names.")
    save_to_file(p_names, "parent_names.txt")

    # Get a list of unique tag values to be put in the PubliBodyTag table.
    #   Examples of tag field values:
    #     tags[4] # '"capital improvements", CIP, budget'
    #     tags[3] # 'stadium'
    tags = set([r['tags'] for r in rs if len(r['tags']) != 0])
    tag_values = sorted(set(list(chain.from_iterable([get_tag_values(t) for t in tags]))))
    print("Saving tag values.")
    save_to_file(tag_values, "tag_values.txt")

    # Get a list of unique jurisdiction slugs. These should match the names in the
    # Jurisdiction table.
    j_slugs = set([r['jurisdiction__slug'] for r in rs if len(r['jurisdiction__slug']) != 0])
    print("Saving jurisdiction slugs.")
    save_to_file(j_slugs, "jurisdiction_slugs.txt")

    # Get a list of unique classifications.
    classfs = set([r['classification'] for r in rs if len(r['classification']) != 0])
    classfs.discard("Department of Business Economic Development Tourism")
    cfs = list(classfs)
    cfs.sort()
    print("Saving classifications.")
    save_to_file(cfs, "classifications.txt")

    # Fix the classification and categories fields in the rows of Public
    # bodies.
    for r in rs:
        fix_dup_classf(r)
        tags_to_categories(r)

    # Rows with a parent name need to come after rows that don't have any
    # parent name.
    rs.sort(key=lambda r: r['parent__name'])
    print("Saving corrected public bodies.")
    save_to_csv(rs, "public-bodies-fixed.csv")

if __name__ == "__main__":
    prog = sys.argv[0]

    if len(sys.argv) < 2:
        print(f"usage: python {prog} csv_file", file=sys.stderr)
        sys.exit(1)

    csv_file = sys.argv[1]
    main(csv_file)

