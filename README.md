# fpassword

The need of this script came up when Revelation went missing on Fedora 31
https://bugzilla.redhat.com/show_bug.cgi?id=1765902

This script loads your local KDBX file and searches in your database the most
relevant information 

Please replace the following lines with the files that match your environment

```
KDBX files 
db_kdbx = '/path/to/you/file.kdbx'
db_key = '/path/to/you/file.kdbx'
db_password = 'MySuperSecurePassword'
```

## Usage 
```
[batman@batcave fpassword]$ ./fpassword.py --help 
usage: fpassword.py [-h] string

Find & copy passwords to your clipboard from a KDBX file

positional arguments:
  string      String to find

optional arguments:
  -h, --help  show this help message and exit
```
