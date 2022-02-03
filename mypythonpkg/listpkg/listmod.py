from mypythonpkg.logpkg import logmod as lg

def lsappend(ls1,var):
    '''This function is to append the value lists passed in to the end of the list'''
    lg.loginfo('lsappend', 'i', ls1, var)
    try:
        ls1 = ls1 + [var]
        return ls1
    except Exception as e:
        lg.logerror('lsappend', e)
    finally:
        lg.loginfo('lsappend', 'c', None, None)

def lsclear(ls1):
    '''This function is used to clear the list'''
    lg.loginfo('lsclear', 'i', ls1, None)
    # There are many methods to clear a list i.e., using 'del' keyword which deletes list or clear method
    # or reinitialization to empty list. Apart from this we have used another method to clear the list here.
    try:
        # Clearing list using *= 0
        ls1 *= 0
        return  ls1
    except Exception as e:
        lg.logerror('lsclear', e)
    finally:
        lg.loginfo('lsclear', 'c', None, None)

def lscopy(ls1):
    '''This function is to copy one list to another list'''
    lg.loginfo('lscopy', 'i', ls1,None)
    try:
        return ls1
    except Exception as e:
        lg.logerror('lscopy', e)
    finally:
        lg.loginfo('lscopy', 'c', None, None)

def lscount(ls1, var):
    '''This function returns the number of times a value is present in the list'''
    lg.loginfo('lscount', 'i', ls1, var)
    try:
        count = 0
        for i in ls1:
            if i == var:
                count += 1
        return count
    except Exception as e:
        lg.logerror('lscount', e)
    finally:
        lg.loginfo('lscount', 'c', None, None)

def lsextend(ls1,var):
    '''This function appends the elements of an iterable object passed in'''
    lg.loginfo('lsextend', 'i', ls1, var)
    try:
        from collections.abc import Iterable
        if isinstance(var, Iterable):
            ls2 = list(var)
            ls1 = ls1 + ls2
            return ls1
        else:
            lg.logerror('lsextend', 'The lsextend can be used only with iterable objects')
            return
    except Exception as e:
        lg.logerror('lsextend', e)
    finally:
        lg.loginfo('lsextend', 'c', None, None)

def lsindex(ls1, var):
    '''This function returns the first occuring index of value'''
    lg.loginfo('lsindex', 'i', ls1, var)
    try:
        for i in range(len(ls1)):
            if ls1[i] == var:
                return i
        else:
            lg.logerror('lsindex', 'The passed value is not found in the list')
    except Exception as e:
        lg.logerror('lsindex', e)
    finally:
        lg.loginfo('lsindex', 'c', None, None)

def lsinsert(ls1,indx,var):
    '''This function inserts the value to the index on the list passed in'''
    lg.loginfo('lsinsert', 'i', ls1, var)
    try:
        ls2 = []
        for i in range(len(ls1)):
            if i == indx:
                ls2 = lsappend(ls2,var)
                ls2 = lsappend(ls2,ls1[i])
            else:
                ls2 = lsappend(ls2,ls1[i])
        else:
            return ls2
    except Exception as e:
        lg.logerror('lsinsert', e)
    finally:
        lg.loginfo('lsinsert', 'c', None,None)

def lspop(ls1,indx):
    '''This function remove the value from the list at index passed in'''
    lg.loginfo('lspop','i',ls1,indx)
    try:
        ls2 = []
        for i in range(len(ls1)):
            if i == indx:
                pass
            else:
                ls2 = lsappend(ls2,ls1[i])
        else:
            return ls2
    except Exception as e:
        lg.logerror('lspop', e)
    finally:
        lg.loginfo('lspop','c', ls1,indx)

def lsremove(ls1,var):
    '''This function will return a list by removing first occurance of the value passed in'''
    lg.loginfo('lsremove','i',ls1,var)
    ls2 = []
    found = False
    try:
        for i in ls1:
            if i == var and found == False:
                found = True
            else:
                ls2 = lsappend(ls2, i)
        else:
            return ls2
    except Exception as e:
        lg.logerror('lsremove', e)
    finally:
        lg.loginfo('lsremove', 'c', ls1, var)

def lsreverse(ls1):
    '''This function will return a list by reversing the list passed in'''
    lg.loginfo('lsreverse','i',ls1,None)
    try:
        ls2 = ls1[::-1]
        return ls2
    except Exception as e:
        lg.logerror('lsreverse', e)
    finally:
        lg.loginfo('lsreverse', 'c', None,None)

def lssort(ls1):
    '''This function will return a list by sorting'''
    lg.loginfo('lssort', 'i',ls1,None)
    try:
        ls2 = []
        while ls1:
            minimum = ls1[0]  # arbitrary number in list
            for x in ls1:
                if x < minimum:
                    minimum = x
            ls2 = lsappend(ls2,minimum)
            ls1 = lsremove(ls1,minimum)
        return ls2
    except Exception as e:
        lg.logerror('lssort', e)
    finally:
        lg.loginfo('lssort','c',None,None)