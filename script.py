import sys
import requests
from math import ceil

if len(sys.argv) < 2:
    link = input("Enter the link: ")
else:
    link = sys.argv[1]

baselink = "https://drive.google.com/uc?export=download&id="
new = link.split('/')[5]
new = baselink+new
print("New link:",new)

if len(sys.argv) > 2 and sys.argv[-1] == '--download':
    print("Downloading the file....", end="")
    res = requests.get(new)
    args = res.headers['Content-Disposition']
    args = args.split(";")
    filename = args[-2].split("\"")[-2]
    print("named '{}'".format(filename))

    download_file = open(filename,'wb')
    download_size = int(res.headers['content-length'])

    for chunk in res.iter_content(ceil(download_size/100)):
        download_file.write(chunk)

    print('Download successful!')
