import os
import sys

from ipcqueue import posixmq
from time import sleep

mq = posixmq.Queue('/fila1')

print("Hallo")

def run_producer():
    print("running as producer")
    while True:
        mq.put([1, 'A'], priority=1)
        sys.stdout.flush()
        sleep(0.5)

def run_consumer():
    print("running as consumer") 
    while True:
        print("receiving from queue ...")
        sys.stdout.flush()
        message = mq.get()
        print("message received " + str(message))
        sys.stdout.flush()


if sys.argv[1] not in ["producer", "consumer"]:
    print("Please specify a flag")
    exit(-1)

if sys.argv[1] == "producer":
   run_producer()

if sys.argv[1] == "consumer":
   run_consumer()

