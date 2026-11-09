import time
import threading

tickets_available = 1
mutex = threading.Lock()

def buy_ticket(user_id: int):
    global tickets_available
    print(f"User {user_id} is attempting purchase...")

    with mutex:
        if tickets_available > 0:
            time.sleep(0.1)
            tickets_available -= 1
            print(f"...User {user_id} purchase successful!")
        else:
            print(f"...User {user_id} failed. Sold out.")

if __name__ == "__main__":
    threads = [threading.Thread(target=buy_ticket, args=(i,))
               for i in range(1, 4)]
    for t in threads: t.start()
    for t in threads: t.join()
