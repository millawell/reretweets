import os
import click
import json

@click.command()
@click.option('--indir', help='in dir')
@click.option('--outpath', help='out path')
def main(indir, outpath, unique=True):

    if unique:
        already_covered = set()

    rows = []
    for fn in os.listdir(indir):
        if ("replies" in fn
            and not fn.startswith(".")
            and not fn.startswith("_")
            and fn.endswith(".jsonl")
            ):

            with open(os.path.join(indir, fn)) as fin:
                for row in fin:
                    row_json = json.loads(row)
                    row_id = row_json["id"]
                    if not unique or row_id not in already_covered:
                        rows.append(row.strip())
                        already_covered.add(row_id)

    with open(outpath, "w") as fout:
        fout.write("\n".join(rows))

if __name__ == "__main__":
    main()