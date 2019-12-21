# queue-systems
Design and Implementing of file backed queue sytem
$ pip install redis==3.2.1

queue.py creates new queues and tasks via the Queue and Task classes, respectively.
client.py enqueues new tasks.
worker.py dequeues and processes tasks.
server.py bring out worker processes.

To test, run server.py and client.py in separate terminal
