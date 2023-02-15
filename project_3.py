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
        
        while start > 0:
            countdown(start)
            time.sleep(1)
            start  = start - 1
        print("your time has run out\nBOOM!!!")
        break
    except:
        print("Please type correct time format")
