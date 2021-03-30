import pymongo
import passwords
  
DatabaseName = "MRS"
usr = "student"
pwd = passwords.DBPASSWORD

def connect():
    return(_connect(usr,pwd))

def _connect(user, password):
    '''
    returns the mongo client instance
    '''
    client = pymongo.MongoClient("mongodb+srv://{0}:{1}@clusterepf.bajt7.mongodb.net/{2}?retryWrites=true&w=majority".format(user,password, DatabaseName))
    return client