import time

def countdown(time):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    print('{:02d}:{:02d}:{:02d}'.format(h, m, s))

while True:
    try:
        hh, mm, ss = map(int, input("Insert time to count down (h:m:s) ").split(":"))
        if mm > 59 or ss > 59:
            raise Exception
        start = 3600 * hh + 60 * mm + ss
        timing = start
        st = time.time()
        while start > 0:
            countdown(start)
            time.sleep(0.998732)
            start  = start - 1
        print("Your time has run out\nBOOM!!!")
        break
    except:
        print("Please type correct time format")

print("", f"Timer working real time:  {time.time() - st} secs", sep = "\n")
print(f"Virtual timer calculated: {timing} secs")
