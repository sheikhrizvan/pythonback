lst = list()
while True:
        
    msg = input('Say Something: ')
    if msg == '/end':
        break
    else:
        if msg.startswith(("how","what","why")):
            lst.append(msg.title()+"?")
        else:
            lst.append(msg.title()+'.')
    
for i in lst:
    print(i)
