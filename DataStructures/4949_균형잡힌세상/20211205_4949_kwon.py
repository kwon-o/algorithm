while True:
    l=input()
    if'.'==l:
        break
    t=''
    for i in l:
        if i in['(',')','[',']']:
            t+=i
    while 1:
        s = t.replace('()','').replace('[]','')
        if s and s == t:
            print('no');break
        elif not s:
            print('yes');break
        else:
            t=s