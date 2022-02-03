import logging

logging.basicConfig(filename='C:\\Users\\test1\Documents\Subbu\Learnings\Data Science\Python\Tasks\loggingfile.txt', level=logging.INFO, format = '%(asctime)s %(levelname)-8s %(message)s')

def loginfo(fname, type, t1, t2):
    if type == 'i':
        if t2 == None:
            logging.info('The function %s is called to process %s' %(fname,t1))
        else:
            logging.info('The function %s is called to process %s and %s' %(fname,t1,t2))
    elif type == 'c':
        logging.info('The function %s is completed' %(fname))

def logerror(fname,exc):
    logging.error('The function %s errored out without processing' %(fname))
    logging.error(exc)

def tpcount(t1,var):
    '''This function will return the count number of times a var is present in tuple tp'''
    loginfo('tpcount', 'i', t1, var)
    try:
        count = 0
        for i in t1:
            if var == i:
                count += 1
        return count
    except Exception as e:
        logerror('tpcount',e)
    finally:
        loginfo('tpcount','c',None,None)

def tpindex(t1,var):
    '''This function will return the index of the first occuring index of the value var'''
    loginfo('tpindex','i',t1,var)
    try:
        for i in range(len(t1)):
            if var == t1[i]:
                return i
    except Exception as e:
        logerror('tpindex',e)
    finally:
        loginfo('tpindex','c',None,None)