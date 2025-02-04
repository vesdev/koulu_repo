import argparse
import urllib.request
import climage
import tempfile

parser = argparse.ArgumentParser(prog="cat", description="What the unix cat should be")
parser.add_argument("error")

with tempfile.TemporaryDirectory() as tmp:
    args = parser.parse_args()
    file = tmp + args.error + "jpg"
    urllib.request.urlretrieve(f"https://http.cat/{args.error}", file)

    output = climage.convert(file)
    print(output)
