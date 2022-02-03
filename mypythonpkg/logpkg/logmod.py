import logging

logging.basicConfig(filename='C:\\Users\\test1\Documents\Subbu\Learnings\Data Science\Python\Tasks\loggingfile.txt', level=logging.INFO, format = '%(asctime)s %(levelname)-8s %(message)s')

def loginfo(fname, type, l1, l2):
    if type == 'i':
        if l2 == None:
            logging.info('The function %s is called to process %s' %(fname,l1))
        else:
            logging.info('The function %s is called to process %s and %s' %(fname,l1,l2))
    elif type == 'c':
        logging.info('The function %s is completed' %(fname))

def logerror(fname,exc):
    logging.error('The function %s errored out without processing' %(fname))
    logging.error(exc)