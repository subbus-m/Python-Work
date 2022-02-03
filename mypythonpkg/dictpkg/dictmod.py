from mypythonpkg.listpkg import listmod as ls
from mypythonpkg.logpkg import logmod as lg

def dtclear(d1):
    '''This function will clear the dictionary passed in'''
    lg.loginfo('dtclear','i',d1,None)
    try:
        return {}
    except Exception as e:
        lg.logerror('dtclear',e)
    finally:
        lg.loginfo('dtclear','c',None,None)

def dtcopy(d1):
    '''This function will copy data from one dictionary to another d1 to d2'''
    lg.loginfo('dtcopy','i',d1,None)
    try:
        return d1
    except Exception as e:
        lg.logerror('dtcopy',e)
    finally:
        lg.loginfo('dtcopy','c',None,None)

def dtfromkeys(t1,var):
    '''This function will return the dictionary created from a iterable keys and values variable'''
    lg.loginfo('dtfromkeys','i',t1,var)
    try:
        d1 = {}
        from collections.abc import Iterable
        if isinstance(t1,Iterable):
            for i in t1:
                d1[i] = var
            else:
                return d1
        else:
            lg.logerror('dtfromkeys','The keys (var) needs to be an Iterable')
    except Exception as e:
        lg.logerror('dtfromkeys',e)
    finally:
        lg.loginfo('dtfromkeys','c',None,None)

def dtget(d1,key):
    '''This function will return the value of the key of a dictionary'''
    lg.loginfo('dtget','i',d1,key)
    try:
        return d1[key]
    except Exception as e:
        lg.logerror('dtget',e)
    finally:
        lg.loginfo('dtget','c',None,None)

def dtitems(d1):
    '''This function returns the items of the dictionary'''
    lg.loginfo('dtitems', 'i', d1, None)
    try:
        kvlist = []
        keylist = list(dtkeys(d1))
        valuelist = list(dtvalues(d1))
        for i in range(len(keylist)):
            t1 = (keylist[i],valuelist[i])
            kvlist = ls.lsappend(kvlist,t1)
        else:
            return kvlist
    except Exception as e:
        lg.logerror('dtitems', e)
    finally:
        lg.loginfo('dtitems', 'c', None, None)

def dtkeys(d1):
    '''This function returns the keys of the dictionary'''
    lg.loginfo('dtkeys','i',d1,None)
    try:
        l1 = []
        d1_reverse = {value : key for key, value in d1.items()}
        for i in d1_reverse:
            l1 = ls.lsappend(l1,d1_reverse[i])
        return l1
    except Exception as e:
        lg.logerror('dtkeys',e)
    finally:
        lg.loginfo('dtkeys','c',None,None)

def dtpop(d1, var):
    '''This function returns a dictionary by deleting the key passed'''
    lg.loginfo('dtpop','i',d1,var)
    try:
        match = False
        for i in d1.keys():
            if i == var:
                del d1[i]
                match = True
                break
        if match == False:
            lg.logerror('dtpop', 'The Key passed in is not found in the dictionary')
        else:
            return d1
    except Exception as e:
        lg.logerror('dtpop',e)
    finally:
        lg.loginfo('dtpop','c',None,None)

def dtpopitem(d1):
    '''This function returns a dictionary by deleting last element of the dictionary'''
    lg.loginfo('dtpopitem','i',d1,None)
    try:
        lskey = []
        for i in d1:
            lskey = ls.lsappend(lskey,i)
        else:
            lenlskey = len(lskey) - 1
            lastkey = lskey[lenlskey]
            del d1[lastkey]
        return d1
    except Exception as e:
        lg.logerror('dtpopitem',e)
    finally:
        lg.loginfo('dtpopitem','c',None,None)

def dtsetdefault(d1,key,val):
    '''This function inserts key value pair to dictionary d1. If value val is None, it will insert as Null'''
    lg.loginfo('dtsetdefault','i',d1,key)
    try:
        d1[key] = val
        return d1
    except Exception as e:
        lg.logerror('dtsetdefault',e)
    finally:
        lg.loginfo('dtsetdefault','c',None,None)

def dtupdate(d1,d2):
    '''This function will append the both dictionaries passed in d1 --> d2'''
    lg.loginfo('dtupdate','i',d1,d2)
    try:
        for k in d2:
            d1[k] = d2[k]
        else:
            return d1
    except Exception as e:
        lg.logerror('dtupdate',e)
    finally:
        lg.loginfo('dtupdate','c',None,None)

def dtvalues(d1):
    '''This function will return the list of values of a dictionary'''
    lg.loginfo('dtvalues','i',d1,None)
    try:
        l1 = []
        for i in d1:
            l1 = ls.lsappend(l1,d1[i])
        else:
            return l1
    except Exception as e:
        lg.logerror('dtvalues',e)
    finally:
        lg.loginfo('dtvalues','c',None,None)

