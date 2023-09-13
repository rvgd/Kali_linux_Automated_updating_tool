#!/usr/bin/env python

import subprocess

#subprocess.call("sudo -s", shell =True)
subprocess.call("sudo apt update", shell =True)
print("\n\n[+] UPDATE COMPLETED...\n\n")
subprocess.call("sudo apt upgrade --fix-missing -y", shell =True)
print("\n\n[+] UPGRADE COMPLETED...\n\n")
subprocess.call("sudo apt full-upgrade -y", shell =True)
print("\n\n[+] Full-UPDATE COMPLETED...\n\n")
subprocess.call("sudo apt dist-upgrade -y", shell =True)
print("\n\n[+] Disk-UPDATE COMPLETED...\n\n")
subprocess.call("sudo apt autoremove -y", shell =True)
print("\n\n[+] Autoremove COMPLETED...\n\n")
print("[+] UPDATE DONE...")


