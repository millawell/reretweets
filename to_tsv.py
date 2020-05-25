import json
import pandas as pd

import click

@click.command()
@click.option('--inf', help='in path')
@click.option('--outf', help='out path')
@click.option('--inspect', help='break point on completion', default=False)
def main(inf, outf, inspect):
    rows = []
    for row in open(inf, "r"):
        rows.append(json.loads(row))

    df = pd.DataFrame(rows)

    df = df.drop_duplicates(subset=['id'])

    df.to_csv(outf, sep="\t")

    if inspect:
        import pdb; pdb.set_trace()


if __name__ == "__main__":
    main()