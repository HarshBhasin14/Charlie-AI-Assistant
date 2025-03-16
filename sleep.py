import time
query= input("Enter")
a=10
if('wait' in query or 'go offline' in query):
    for i in range(a):
        time.sleep(a)
        a = 2*a
    while True:
        print('Offlne')
    
    if('resume' in query or 'wake up' in query):
        break


    