"""
from passlib.hash import sha256_crypt

password = input("Enter the password: ")

if password is None: 
    raise "Password absent"

secure_password = sha256_crypt.encrypt(str(password))

print(f"Original password: {password} \n")
print(f"Encrpyt password: {secure_password}")
"""

import pkg_resources

installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
   for i in installed_packages])
print(installed_packages_list)