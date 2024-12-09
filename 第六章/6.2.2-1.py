from threading import Thread
def task():
    print ('线程运行')
thread_one = Thread(target=task)
class MyThread(Thread):
    def __init__(self,num):
        super().__init__()
        self.name = '线程' + str(num)
    def run(self):
        message = self.name + '运行'
        print(message)
thread_two = MyThread(1)
if __name__ == '__main__':
    thread_two.start()