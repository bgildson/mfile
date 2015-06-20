MFile
======

Class used to easily manage one file using one python object.

Install
======

```sh
$ git clone https://github.com/gildson/mfile.git
$ cd mfile
$ python setup.py install
...
Finished processing dependencies for MFile==0.1
```

Using MFile
======

This file structure will be used to the demonstrations

```
    U:\
    ├── folder_a\
    ├── folder_b\
    └── doc.txt
```

**Importing and creating one object of MFile passing the file path by parameter**
```py
>>> from mfile import MFile
>>> file = MFile('U:\\doc.txt')
```

**This time the object have the following attributes**
```py
>>> file.name
'doc'
>>> file.extension
'txt'
>>> file.full_name
'doc.txt'
>>> file.directory
'U:\\'
>>> file.path
'U:\\doc.txt'
>>> file.exists
True
>>> # returns a datetime object with the datetime of creation
>>> file.date_creation
datetime.datetime(2015, 6, 14, 19, 42, 18, 950604)
>>> # returns a datetime object with the datetime of last modification
>>> file.date_modification
datetime.datetime(2015, 6, 14, 19, 42, 53, 255959)
>>> # returns a value numeric with the size of the file in bytes
>>> file.size
19456
```

**... and the following methods**

**.move(detine_path)**
```py
>>> # moves the file to directory passed by parameter
>>> file.move('U:\\folder_a')
>>> # verify, the selected file is the same that the moved file
>>> file.path
'U:\\folder_a\\doc.txt'
```
```
    Current structure of the files
    U:\
    ├── folder_a\
    │   └── doc.txt
    └── folder_b\
```

**.copy(destine_path, select_copied=False)**
```py
>>> # copies the file to directory passed by parameter
>>> file.copy('U:\\folder_b')
>>> # verify, the path is the same that before. The file just was copied and the selected file is the origin file.
>>> file.path
'U:\\folder_a\\doc.txt'
```
```
    Current structure of the files
    U:\
    ├── folder_a\
    │   └── doc.txt
    ├── folder_b\
    │   └── doc.txt
```

**.copy(destine_path, select_copied=False)**
```py
>>> # copies the file to directory passed by parameter and select the destination file
>>> file.copy('U:\\', True)
>>> # verify, the file was copied and the path was changed to same destination file path
>>> file.path
'U:\\doc.txt'
```
```
    Current structure of the files
    U:\
    ├── folder_a\
    │   └── doc.txt
    ├── folder_b\
    │   └── doc.txt
    └── doc.txt
```

**.rename(new_name)**
```py
>>> # renames the file
>>> file.rename('doc_renamed')
>>> file.path
'U:\\doc_renamed.txt'
```
```
    Current structure of the files
    U:\
    ├── folder_a\
    │   └── doc.txt
    ├── folder_b\
    │   └── doc.txt
    └── doc_renamed.txt
```

**.open()**
```py
>>> # execute/open the file
>>> file.open()
```

**Some things can be done interacting with the attributes**
```py
>>> # renames the file
>>> file.name = 'module'
>>> # the same that: file.rename('module')
>>> file.path
'U:\\module.txt'

>>> # changes the file extension
>>> file.extension = 'py'
>>> file.path
'U:\\module.py'

>>> file.directory = 'U:\\folder_a'
>>> # the same that: file.move('U:\\folder_a')
>>> file.path
'U:\\folder_a\\module.py'
```
```
    Current structure of the files
    U:\
    ├── folder_a\
    │   ├── doc.txt
    │   └── module.py
    ├── folder_b\
    │   └── doc.txt
```
Careful when handling .path (.path can change directory, name and extension)
```py
>>> # changing the path
>>> file.path = 'U:\\module.py'
>>> # check above, was necessary to know the name and the extension of the file to change just the directory
>>> file.path
'U:\\module.py'
```
Is indicated use .path just when is necessary change more than 1 property

**All operations overwrite the destination file, if any.**
```py
>>> # set the name and path of the file
>>> file.path = 'U:\\doc.txt'
```
```
    Current structure of the files
    U:\
    ├── folder_a\
    │   └── doc.txt
    ├── folder_b\
    │   └── doc.txt
    └── doc.txt
```
```py
>>> # overwrite the destination file
>>> file.directory = 'U:\\folder_a'
>>> file.path
'U:\\folder_a\\doc.txt'
```
```
    Current structure of the files
    U:\
    ├── folder_a\
    │   └── doc.txt
    ├── folder_b\
    │   └── doc.txt
```

**Remove the file from disk**
```py
>>> file.remove()
```
```
    Current structure of the files
    U:\
    ├── folder_a\
    ├── folder_b\
    │   └── doc.txt
```