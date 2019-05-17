import sys
if len(sys.argv)==2:
    with open(sys.argv[1]) as filename:
        i=0
        temp={}
        for baris in filename:
            if i!=0:
                element=baris.split(',')
                if len(element)==48:
                    e=element[47].split('\n')
                    if e[0] not in temp:
                        temp[e[0]]=1
                    else:
                        temp[e[0]]=temp[e[0]]+1
            i=i+1
    print(temp)
    filename.close()
else:
    print('please input a csv dataset filename as an argument')
