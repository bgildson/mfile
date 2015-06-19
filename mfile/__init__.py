# -*- coding: utf-8 -*-

class MFile:

    def _exists(func):
        def params(self, *args, **kwargs):
            if not self.exists:
                raise Exception('File not exists!')
            return func(self, *args, **kwargs)
        return params

    def __init__(self, path):
        from datetime import datetime
        import shutil
        self._d = datetime
        self._s = shutil
        if not shutil.os.path.exists(path) or not shutil.os.path.isfile(path):
            raise Exception('File not exists!')
        self._path = path

    def __repr__(self):
        return "<File: '%s'>" % self.path

    @property
    def directory(self):
        return self._s.os.path.dirname(self._path)

    @property
    @_exists
    def date_creation(self):
        return self._d.fromtimestamp(self._s.os.path.getctime(self.path))

    @property
    @_exists
    def date_modification(self):
        return self._d.fromtimestamp(self._s.os.path.getmtime(self.path))

    @directory.setter
    @_exists
    def directory(self, value):
        if not self._s.os.path.exists(value):
            raise Exception('Destination directory does not exists!')
        self.path = self._s.os.path.join(value, self.full_name)

    @property
    def exists(self):
        return self._s.os.path.exists(self._path)

    @property
    def extension(self):
        return self.path.split('.')[-1]

    @extension.setter
    @_exists
    def extension(self, value):
        new_path = self._s.os.path.join(self.directory, self.name + '.' + value)
        self._s.os.rename(self._path, new_path)
        self._path = new_path

    @property
    def full_name(self):
        return self._path.split(self._s.os.path.sep)[-1]

    @property
    def name(self):
        return '.'.join(self._path.split(self._s.os.path.sep)[-1].split('.')[:-1])

    @name.setter
    @_exists
    def name(self, value):
        new_path = self._s.os.path.join(self.directory, value + '.' + self.extension)
        self._s.os.rename(self._path, new_path)
        self._path = new_path

    @property
    def path(self):
        return self._path

    @path.setter
    @_exists
    def path(self, value):
        if not self._s.os.path.exists(self._s.os.path.dirname(value)):
            raise Exception('Destination directory does not exist!')
        self._s.move(self._path, value)
        self._path = value

    @property
    def size(self):
        return self._s.os.path.getsize(self.path)

    @_exists
    def copy(self, destine, select_copied=False):
        self._s.copy(self._path, destine)
        if select_copied: self._path = self._s.os.path.join(destine, self.full_name)

    def move(self, destine):
        self.directory = destine

    @_exists
    def open(self):
        self._s.os.startfile(self._path)

    @_exists
    def remove(self):
        self._s.os.remove(self._path)

    def rename(self, name):
        self.name = name