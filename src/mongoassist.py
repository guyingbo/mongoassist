# -*- coding: utf-8 -*-
from pymongo import MongoClient
import gridfs


class Model(dict):
    __database__ = None
    __collection__ = None
    __dburi__ = None
    @classmethod
    def getClient(cls):
        if hasattr(cls, "_client"):
            client = cls._client
        else:
            client = MongoClient(cls.__dburi__)
            cls._client = client
        return client

    @classmethod
    def getCollection(cls):
        return cls.getClient()[cls.__database__][cls.__collection__]

    @classmethod
    def getDatabase(cls):
        return cls.getClient()[cls.__database__]

    @classmethod
    def saveDoc(cls, *args, **kw):
        return cls.getCollection().save(*args, **kw)

    @classmethod
    def findOne(cls, *args, **kw):
        kw["as_class"] = cls
        return cls.getCollection().find_one(*args, **kw)

    @classmethod
    def findNewestOne(cls, *args, **kw):
        kw["as_class"] = cls
        kw["sort"] = [("_id", -1)]
        return cls.getCollection().find_one(*args, **kw)

    @classmethod
    def findDocs(cls, *args, **kw):
        kw["as_class"] = cls
        return cls.getCollection().find(*args, **kw)

    @classmethod
    def updateDocs(cls, *args, **kw):
        return cls.getCollection().update(*args, **kw)

    @classmethod
    def removeDocs(cls, *args, **kw):
        return cls.getCollection().remove(*args, **kw)

    @classmethod
    def insertDocs(cls, *args, **kw):
        return cls.getCollection().insert(*args, **kw)

    @classmethod
    def group(cls, key, condition, initial, reduce, finalize=None):
        return cls.getCollection().group(key, condition, initial, reduce, finalize)

    @classmethod
    def distinct(cls, *args, **kw):
        return cls.getCollection().distinct(*args, **kw)

    @classmethod
    def mapReduce(cls, *args, **kw):
        return cls.getCollection().map_reduce(*args, **kw)

    @classmethod
    def ensureIndex(cls, key_or_list, cache_for=300, **kwargs):
        cls.getCollection().ensure_index(key_or_list, cache_for, **kwargs)

    @classmethod
    def createIndex(cls, key_or_list, cache_for=300, **kwargs):
        cls.getCollection().create_index(key_or_list, cache_for, **kwargs)

    @classmethod
    def runCommand(cls, command, check=True, **kwargs):
        return cls.database.command(command, cls.__collection__, check, **kwargs)

    @classmethod
    def dropCollection(self):
        return cls.getCollection().drop()

    @classmethod
    def aggregate(cls, pipeline):
        return cls.getCollection().aggregate(pipeline)

    @classmethod
    def findAndModify(cls, *args, **kw):
        kw["as_class"] = cls
        return cls.getCollection().find_and_modify(*args, **kw)

    @classmethod
    def clone(cls, collection, database=None, name=None, doc=None):
        if name is None:
            name = cls.__name__
        dic = {}
        dic["__collection__"] = collection
        if database is not None:
            dic["__database__"] = database
        if doc is not None:
            dic["__doc__"] = doc
        return type(name, (cls,), dic)

    def __hash__(self):
        return hash(self["_id"])

    def deleteDoc(self):
        self.getCollection().remove(self["_id"])

    def save(self, *args, **kw):
        return self.getCollection().save(self, *args, **kw)

    def updateSelf(self, *args, **kw):
        return self.updateDocs({"_id": self["_id"]}, *args, **kw)


class Storage(Model):
    __database__ = None
    __collection__ = None
    @classmethod
    def getGridFS(cls):
        return gridfs.GridFS(cls.getClient()[cls.__database__], cls.__collection__)

    @classmethod
    def put(cls, data, **kwargs):
        return cls.getGridFS().put(data, **kwargs)

    @classmethod
    def new_file(cls, **kwargs):
        return cls.getGridFS().new_file(**kwargs)

    @classmethod
    def list(cls):
        return cls.getGridFS().list()

    @classmethod
    def getFile(cls, file_id):
        return cls.getGridFS().get(file_id)

    @classmethod
    def deleteFile(cls, file_id):
        return cls.getGridFS().delete(file_id)

    @classmethod
    def exists(cls, document_or_id=None, **kwargs):
        return cls.getGridFS().exists(document_or_id=document_or_id, **kwargs)

    @classmethod
    def getLastVersion(cls, filename=None, **kwargs):
        return cls.getGridFS().get_last_version(filename, **kwargs)

    @classmethod
    def getVersion(cls, filename=None, version=-1, **kwargs):
        return cls.getGridFS().get_version(filename, version, **kwargs)

    @classmethod
    def getCollection(cls):
        return cls.getClient()[cls.__database__][cls.__collection__+".files"]
