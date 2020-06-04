import thread
import time


def print_time_thread(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (thread_name, time.ctime(time.time()))


if __name__ == '__main__':

    try:
        thread.start_new_thread(print_time_thread, ('Thread-1', 2))
        thread.start_new_thread(print_time_thread, ('Thread-2', 1))

    except:
        print "Error: unable to start thread"
    while 1:
        pass
