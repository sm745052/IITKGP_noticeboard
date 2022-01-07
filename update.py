import requests
import os
import copy

def check(ls):
    ctr=0
    l = len(ls)
    for i in ls:
        if(i[1]==b''):
            ctr+=1      #increases ctr by one whenever an empty element is found
    return ctr!=l       #returns false if some nonempty element is present


def notices(ls):
    filtered = copy.copy(ls)
    for i in ls:
        if(i[-4:]!='.pdf'):
            filtered.pop(filtered.index(i))
    for ind, i in enumerate(filtered):
        filtered[ind] = int(i[:-4])
    return filtered

last = -1

while(True):
    present = os.listdir('./')
    present = notices(present)
    present = sorted(present)[::-1]
    present_latest = present[0]+1
    span = 10
    contents = []
    for i in range(present_latest, present_latest+span):
        contents.append([i, requests.get('https://erp.iitkgp.ac.in/InfoCellDetails/resources/external/groupemailfile?file_id={}'.format(i)).content])
        if(contents[-1][1]!=b''):
            print('{}.pdf accessed'.format(i))
    if(check(contents)==False):
        print("**updated**")
        if(last==-1):
            print('No new notices found')
            break
        print("latest updated notice: {}.pdf".format(last))
        break
    else:
        for i in contents:
            if(i[1]!=b''):
                with open('{}.pdf'.format(i[0]), 'wb') as f:
                    f.write(i[1])
                    last = i[0]