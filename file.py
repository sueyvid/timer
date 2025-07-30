# file.py
import os

class File:
    def __init__(self, name=None):
        """
            Create a instance of a file.
            Can receive a name and create a file with that name.
        """
        self._name = name

    @property
    def name(self):
        """
            Return the filename.
        """
        return self._name
    
    @name.setter
    def name(self, value: str):
        """
            Set the filename.
            Accepts str.
            If other type is received, an error will be raised.
        """
        if value == "":
            self.delete()
            self._name = ""
        elif type(value) != str:
            raise TypeError(f"The type {type(value)} isn't accepts")
        elif self.wasCreate():
            self._change_file(value)
        else:
            self._name = value

    def wasCreate(self):
        """
            If the file already exist, returns True.
        """
        if self._name:
            return True if os.path.exists(self._name) else False
        else:
            return False
    
    def read(self):
        """
            Use for reading the content of the file.
        """
        with open(self._name) as f:
            content = f.read()

        return content
    
    def append(self, text: str | list):
        """
            To append content to the file.
            Accepts str or list.
            If other type is received, an error will be raised.
        """
        self._writing_to_file(text, "a")

    def write(self, text: str | list):
        """
            To overwrite the existing content to the file.
            Accepts str or list.
            If other type is received, an error will be raised.
        """
        self._writing_to_file(text, "w")

    def create(self):
        """
            If the file already exist, an error will be raised.
        """
        if self.wasCreate():
            raise FileExistsError("The file already exist")
        
        f = open(self._name, "x")
        f.close()

    def delete(self):
        """
            To delete a file.
        """
        if self.wasCreate():
            os.remove(self._name)

    def _writing_to_file(self, text, mode):
        """
            An internal method, it really write the file.
        """
        if type(text) == list:
            with open(self._name, mode=mode) as f:
                t = ""
                for i in text:
                    t += str(i) + "\n"
                f.write(t)
        elif type(text) == str:
            with open(self._name, mode=mode) as f:
                if text.endswith("\n"):
                    f.write(text)
                else:
                    f.write(f"{text}\n")
        else:
            raise TypeError(f"The type {type(text)} isn't accepts")

    def _change_file(self, value):
        """
            If the filename is changed, this method is called.
        """
        content = self.read()
        self.delete()
        self.name = value
        self.create()
        self.write(content)