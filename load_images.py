import os
import pandas as pd
import requests
import json
import uuid
from tqdm import tqdm

import click

@click.command()
@click.option('--inpath', help='in path')
@click.option('--outdir', help='out dir')
def main(inpath, outdir):
    already_downloaded = set()

    for row in tqdm(open(inpath, "r")):
        row = json.loads(row)
        if row["id"] not in already_downloaded and "extended_entities" in row:
            ee = row["extended_entities"]
            if "media" in ee:
                for m in ee["media"]:
                    url = m["media_url"]

                    r = requests.get(url)
                    file_name = "{}_{}_{}".format(
                        str(uuid.uuid4()),
                        row["id"],
                        url.split("/")[-1]
                    )
                    with open(os.path.join(outdir, file_name), 'wb') as f:
                        f.write(r.content)

                    already_downloaded.add(row["id"])

if __name__ == "__main__":
    main()