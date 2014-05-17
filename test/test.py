from mongoassist import Model, Q, F


def testF0():
    assert dict(F("field") > 2) == {"field": {"$gt": 2}}

def testF1():
    assert dict(F("field").inc(3)) == {"$inc": {"field": 3}}

def testF2():
    assert dict(F("field").set(5)) == {"$set": {"field": 5}}

def testF3():
    assert dict(F("field").anything("haha")) == {"$anything": {"field": "haha"}}

def testQ0():
    assert dict(Q.inc(Q("field", 3))) == {"$inc": {"field": 3}}

def testQ1():
    pass
