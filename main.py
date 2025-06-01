import os
prompt = int(input("""
What do you want to install

1- libreoffice
2- test.py

> """))

if prompt == 1:
    os.system("sudo pacman -S libreoffice-fresh")
else:
    os.system("curl 172.233.44.224/AutoInstaller/test.py >> test.py")

