import click
import json
from tqdm import tqdm


@click.command()
@click.option('--inf', help='in file')
@click.option('--outf', help='out file')
@click.option('--outformat', help='string format output ids')
def main(inf, outf, outformat="{id_}"):
    ids = []
    for row in tqdm(open(inf, "r")):

        row = json.loads(row)

        if "quoted_status_id_str" in row and row["quoted_status_id_str"] is not "":
            ids.append(row["id"])

    with open(outf, "w") as fout:
        fout.write("\n".join(
            [outformat.format(id_=id_) for id_ in ids]
        ))

if __name__ == "__main__":
    main()