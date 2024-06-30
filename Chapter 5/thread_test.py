import time
import threading


def long_task():
    for i in range(5):
        time.sleep(1)
        print("working: %s\n" % i)

print("Start")

threads = []
for i in range(5):
    # long_task()
    t = threading.Thread(target = long_task) # 스레드 생성
    threads.append(t)

for i in threads:
    t.start() # 스레드 실행, RuntimeError: threads can only be started once 발생

for i in threads:
    t.join() # join으로 thread가 종료될 때까지 대기해야 End가 출력되는 것을 확인 가능하다. BUT 원하는대로 출력 안됨

    
print("End")