link = input("Enter the link:")
baselink = "https://drive.google.com/uc?export=download&id="
new = link.split('/')[5]
new = baselink+new
print("New link:",new)