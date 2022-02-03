from mypythonpkg.logpkg import logmod as lg
from mypythonpkg.listpkg import listmod as ls

def stadd(s1,var):
    '''This function will add the variable var to the last of the set s1 passed in'''
    lg.loginfo('stadd','i',s1,var)
    try:
        l1 = list(s1)
        l1 = ls.lsappend(l1,var)
        return set(l1)
    except Exception as e:
        lg.logerror('stadd',e)
    finally:
        lg.loginfo('stadd','c',None,None)

def stclear(s1):
    '''This function will clear the set passed in'''
    lg.loginfo('stclear','i',s1,None)
    try:
        return s1([])
    except Exception as e:
        lg.logerror('stclear',e)
    finally:
        lg.loginfo('stclear','c',None,None)

def stcopy(s1):
    '''This function will copy set s1 to another set s2'''
    lg.loginfo('stcopy','i',s1,None)
    try:
        if type(s1) == set:
            return s1
        else:
            lg.logerror('stcopy', 'The passed parameter is not a type of Set')
    except Exception as e:
        lg.logerror('stcopy',e)
    finally:
        lg.loginfo('stcopy','c',None,None)

def stdifference(s1,s2):
    '''This function will return a new set with unmatched between the sets. i.e., all elements present in first set and not in second set'''
    lg.loginfo('stdifference','i',s1,s2)
    try:
        l1 = list(s1)
        l2 = list(s2)
        s3 = set([])
        for i in l1:
            if ls.lscount(l2,i) == 0:
                stadd(s3,i)
        else:
            return s3
    except Exception as e:
        lg.logerror('stdifference',e)
    finally:
        lg.loginfo('stdifference','c',None,None)

def stdifference_update(s1,s2):
    '''This function will return a new set by removing all matched with unmatched between the sets. i.e., all elements present in first set and not in second set'''
    lg.loginfo('stdifference_update', 'i',s1, s2)
    try:
        l1 = list(s1)
        l2 = list(s2)
        s3 = set([])
        for i in l2:
            if ls.lscount(l1, i) == 0:
                stadd(s3, i)
        else:
            return s3
    except Exception as e:
        lg.logerror('stdifference_update', e)
    finally:
        lg.loginfo('stdifference_update', 'c', None, None)

def stdiscard(s1,var):
    '''This function removes a value var from the set s1'''
    lg.loginfo('stdiscard','i',s1,var)
    try:
        s2 = set([])
        for i in s1:
            if i != var:
                stadd(s2,i)
        return s2
    except Exception as e:
        lg.logerror('stdiscard',e)
    finally:
        lg.loginfo('stdiscard','c',None,None)

def stintersection(s1,s2):
    '''This function returns a set which have common elements of 2 sets'''
    lg.loginfo('stintersection','i',s1,s2)
    try:
        l2 = list(s2)
        s3 = set([])
        for i in s1:
            if ls.lscount(l2,i) > 0:
                stadd(s3,i)
        return s3
    except Exception as e:
        lg.logerror('stintersection',e)
    finally:
        lg.loginfo('stintersection','c',None,None)

def stintersection_update(s1,s2):
    '''This function returns a set with the intersection between two sets'''
    lg.loginfo('stintersection_update','i',s1,s2)
    try:
        l1 = list(s1)
        s1 = set([])
        for i in s2:
            if ls.lscount(l1, i) > 0:
                stadd(s1, i)
        return s1
    except Exception as e:
        lg.logerror('stintersection_update', e)
    finally:
        lg.loginfo('stintersection_udpate', 'c', None, None)

def stisdisjoint(s1,s2):
    '''This function returns True if there are no common elements between two sets passed in'''
    lg.loginfo('stdisjoint','i',s1,s2)
    try:
        match_found = False
        l1 = list(s1)
        for i in s2:
            if ls.lscount(l1, i) > 0:
                match_found = True
                break
        if match_found == True:
            return False
        else:
            return True
    except Exception as e:
        lg.logerror('stdisjoint', e)
    finally:
        lg.loginfo('stdisjoint', 'c', None, None)

def stissubset(s1,s2):
    '''This function returns True if first set s1 is subset of another set s2'''
    lg.loginfo('stissubset', 'i', s1, s2)
    try:
        match_not_found = False
        l2 = list(s2)
        for i in s1:
            if ls.lscount(l2, i) != 0:
                match_not_found = True
                break
        if match_not_found == True:
            return False
        else:
            return True
    except Exception as e:
        lg.logerror('stissubset', e)
    finally:
        lg.loginfo('stissubset', 'c', None, None)

def stissuperset(s1,s2):
    '''This function returns True if second set s2 is present in first set s1'''
    lg.loginfo('std', 'i', s1, s2)
    try:
        match_not_found = False
        l1 = list(s1)
        for i in s2:
            if ls.lscount(l1, i) != 0:
                match_not_found = True
                break
        if match_not_found == True:
            return False
        else:
            return True
    except Exception as e:
        lg.logerror('stissuperset', e)
    finally:
        lg.loginfo('stissuperset', 'c', None, None)

def stpop(s1):
    '''This function returns a set by removing last element of a set'''
    lg.loginfo('stpop','i',s1,None)
    try:
        l1 = list(s1)
        l1 = ls.lspop(l1,(len(l1)-1))
        s1 = set(l1)
        return s1
    except Exception as e:
        lg.logerror('stpop',e)
    finally:
        lg.loginfo('stpop','c',None,None)

def stremove(s1,var):
    '''This function removes a value var from the set s1 and if var not found exception will be raised'''
    lg.loginfo('stremove', 'i', s1, var)
    try:
        if len(s1) == 0:
            lg.logerror('stremove', 'The passed in set does not have any elements')
            return
        s2 = set([])
        for i in s1:
            if i != var:
                stadd(s2, i)
        return s2
    except Exception as e:
        lg.logerror('stremove', e)
    finally:
        lg.loginfo('stremove', 'c', None, None)

def stsymmetric_difference(s1,s2):
    '''This function will return a set by combining both the sets passed in'''
    lg.loginfo('stsymmetric_difference','i',s1,s2)
    try:
        for i in s2:
            stadd(s1,i)
        else:
            return s1
    except Exception as e:
        lg.logerror('stsymmetric_difference',e)
    finally:
        lg.loginfo('stsymmetric_difference','c',None,None)

def stsymmetric_difference_update(s1,s2):
    '''This function will update set s1 by combining both the sets passed in'''
    lg.loginfo('stsymmetric_difference_update','i',s1,s2)
    try:
        for i in s2:
            stadd(s1, i)
        else:
            return s1
    except Exception as e:
        lg.logerror('stsymmetric_difference_update', e)
    finally:
        lg.loginfo('stsymmetric_difference_update', 'c', None, None)

def stunion(s1,s2):
    '''This function return a set by merging both the sets passed in'''
    lg.loginfo('stsymmetric_difference_update', 'i', s1, s2)
    try:
        for i in s2:
            stadd(s1, i)
        else:
            return s1
    except Exception as e:
        lg.logerror('stunion', e)
    finally:
        lg.loginfo('stunion', 'c', None, None)

def stupdate(*args):
    '''This function return a set by merging all the sets passed in'''
    lg.loginfo('stupdate', 'i', *args, None)
    try:
        s1 = set([])
        for st in args:
            s1 = s1 | st
        else:
            return s1
    except Exception as e:
        lg.logerror('stupdate', e)
    finally:
        lg.loginfo('stupdate', 'c', None, None)