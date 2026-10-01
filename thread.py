import threading
import time
b=[1,2,3,4,5]
def cube(a):
    for i in a:
        print('cube is ',i**3)
        time.sleep(1)
        
def square(a):
    for i in a:
            print('square is ',i**2)
            time.sleep(2)
            
t1=threading.Thread(target=cube,args=(b,))  
t2=threading.Thread(target=square,args=(b,))   

t1.start()      
t2.start()
t1.join()
t2.join()

print("done") 
            
            
            
            
            
import threading
import time
def download():
    print("Download starts...")            
    time.sleep(5)
    
def countdown():
    for i in range(5,0,-1):
        print("countdown:",i)
        time.sleep(1)
        
t1=threading.Thread(target=download)
t1=threading.Thread(target=countdown)

t1.start()  
time.sleep(0.2)    
t2.start()
t1.join()
t2.join()                        
print("All task completed")