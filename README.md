# Common Helper Files

File and filesystem related helper functions.

## Known Issues
It seems that recent versions of setuptools can't handle a "." in the requirements list.
Therfore, [hurry.filesize](https://pypi.python.org/pypi/hurry.filesize) must be installed manually in advance.

```sh
$ sudo -EH pip3 install hurry.filesize
``` 

