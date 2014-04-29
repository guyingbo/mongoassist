mongoassist
===========

A very simple mongodb client wrapper.


Usage
-----
```
from mongoassist import Model as _Model


class Model(_Model):
    __dburi__ = "mongodb://127.0.0.1:27017"
    __database__ = "dbname"


class User(Model):
    __collection__ = "users"
    @property
    def fullname(self):
        return self["lastname"] + " " + self["firstname"]


user = User()
user["firstname"] = "wukong"
user["lastname"] = "sun"
assert user.fullname == "wukong sun"
user.save()

User.findOne()
User.findDocs()
User.findDocs({"lastname": "sun"})

Admin = User.clone("admins")
Admin.updateDocs({"firstname": "xxx"}, {"$set": {"lastname": "abc"}})
```
