
import pickle 

with open('chat.pkl','wb') as f:
    pickle.dump({'name':'ravi','age':20},f)#pickling

with open('chat.pkl','rb') as f:
    print(pickle.load(f))#unpickling



import logging 
logging.basicConfig(filename="chat.log",level=logging.DEBUG,format="%(asctime)s---%(levelname)s---%(message)s--%(lineno)d")
logging.debug("I am enter into application")#1 
logging.info("you are login successfully")#2
logging.warning("there are 2items left")#3
logging.error("you ticket is not comfirmed due to payment failure")#4
logging.critical("too much traffic system crashed....")#5
logging.exception('yi code break ayindii')