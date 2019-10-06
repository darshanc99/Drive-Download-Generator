import sys

if len(sys.argv) < 2:
    link = input("Enter the link: ")
else:
    link = sys.argv[1]

baselink = "https://drive.google.com/uc?export=download&id="
new = link.split('/')[5]
new = baselink+new
print("New link:",new)
