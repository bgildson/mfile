# -*- coding: utf-8 -*-

class MFile:

    def __init__(self, path):
        import shutil
        if not shutil.os.path.exists(path) or not shutil.os.path.isfile(path):
            raise Exception('File not exist!')
        self._path = path
        self._s = shutil

    def __repr__(self):
        return "<File: '%s'>" % self.path

    @property
    def directory(self):
        return self._s.os.path.dirname(self._path)

    @directory.setter
    def directory(self, value):
        if not self._s.os.path.exists(value):
            raise Exception('Destination directory does not exist!')
        self.path = self._s.os.path.join(value, self.full_name)

    @property
    def exists(self):
        return self._s.os.path.exists(self._path)

    @property
    def extension(self):
        return self.path.split('.')[-1]

    @extension.setter
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
    def name(self, value):
        new_path = self._s.os.path.join(self.directory, value + '.' + self.extension)
        self._s.os.rename(self._path, new_path)
        self._path = new_path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if not self._s.os.path.exists(self._s.os.path.dirname(value)):
            raise Exception('Destination directory does not exist!')
        self._s.move(self._path, value)
        self._path = value

    def copy(self, destine, select_copied=False):
        self._s.copy(self._path, destine)
        if select_copied: self._path = self._s.os.path.join(destine, self.full_name)

    def move(self, destine):
        self.directory = destine

    def open(self):
        self._s.os.startfile(self._path)

    def rename(self, name):
        self.name = name