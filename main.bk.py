from  mood.mqueue import MessageQueue
import os
import sys
mq = MessageQueue("/myqueue",  os.O_CREAT)
mq = MessageQueue("/myqueue",  os.O_RDWR)

def run_producer():
    print("running as producer")
    print(mq.__dict__)

def run_consumer():
    print("running as consumer") 
    while True:
        print("receiving from queue ...")
        message = mq.receive()
        print("message received " + str(message))


if sys.argv[1] not in ["producer", "consumer"]:
    print("Please specify a flag")
    exit(-1)

if sys.argv[1] == "producer":
   run_producer()

if sys.argv[1] == "consumer":
   run_consumer()

