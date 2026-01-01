import re


class User:
    def __init__(self, first_name, last_name, email):
        self._first_name = first_name
        self._last_name = last_name
        self._email = None
        self._email = email

    @property
    def first_name(self):

        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
            self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not re.match(r'^[\w\.-]+@[\w\.]+\.\w+$', value):
            self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not re.match(r'^[\w\.-]+@[\w\.]+\.\w+$', value):
            self._email = value


student = User("Demmi", "Hounnik", "an32@felix.com")
student2 = User("Kristina", "Kaser", "angel@gmail.com")

print(student.first_name)
print(student.last_name)
print(student.email)
print(student2.first_name)
print(student2.last_name)
print(student2.email)
