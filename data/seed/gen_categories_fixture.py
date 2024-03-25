# gen_categories_fixture.py - Generate a JSON file with the individual category
#                             values in separate records to be loaded as a
#                             fixture.
#

import json
import sys
from slugify import slugify
from pathlib import Path


def load_data(text_file):
    """Return a list of tags from the rows in test_file."""
    rs = []
    with open(text_file, "r") as fin:
        rs = fin.readlines()
    return rs

# Category entry is a dict with model, pk, and fields keys.
# The fields value is a dict with name, slug, path, depth, numchild, and
# is_topic keys.
def category_from(name, counter):
    """Return a category dict from name and counter.
    """
    num = int(counter)
    return {
        "model": "publicbody.category",
        #"pk": 1,                     # can omit
        "fields": {
            "name": name.strip(),
            "slug": slugify(name.strip()),
            "path": f"{num:04d}",   # required and unique
            "depth": 1,
            "numchild": 0,
            "is_topic": False
        }
    }

def save_to_json(cs, fn):
    """Write a list of category dicts as a JSON document into fn."""
    with open(fn, "w") as fout:
        fout.write("[\n") # opening for JSON document

        for c in cs[:-1]:
            fout.writelines(json.dumps(c, indent=4))
            fout.write(",\n")

        # Don't add a comma after the last dict.
        fout.writelines(json.dumps(cs[-1], indent=4))
        fout.write("\n]") # closing for JSON document


def main(src_file, dst_file):
    lines = load_data(src_file)

    # Generate category dicts from list of tag values.
    cats = []
    for i, line in enumerate(lines):
        cats.append(category_from(line.strip(), i+1))

    save_to_json(cats, dst_file)


if __name__ == "__main__":
    prog = sys.argv[0]

    if len(sys.argv) < 2:
        print(f"usage: python {prog} tag_values_file", file=sys.stderr)
        sys.exit(1)

    tag_path = Path(sys.argv[1])
    out_file = f"{tag_path.stem}.json"

    main(tag_path, out_file)

