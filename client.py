### This module will create a new instance of Redis and the SimpleQueue class and enqueue 40 tasks.



import redis

from queue import Queue
from tasks import get_word_counts


NUMBER_OF_TASKS = 10


if __name__ == '__main__':
    r = redis.Redis()
    queue = Queue(r, 'sample')
    count = 0
    for num in range(NUMBER_OF_TASKS):
        queue.enqueue(get_word_counts, 'file1.txt')
        queue.enqueue(get_word_counts, 'file2.txt')
        queue.enqueue(get_word_counts, 'file3.txt')
        queue.enqueue(get_word_counts, 'file4.txt')
        count += 4
    print(f'Enqueued {count} tasks!')