import time,re,warnings,requests
from pyquery import PyQuery as pq
warnings.filterwarnings("ignore")
bs,ok,accounts,k=[],0,{},0
with open("data.conf") as f:
    for s in f.readlines():
        try:
            accounts[s.split()[0]]=s.split()[1]
        except:
            pass
# ------------------------------------------------------------------------
def run(acc,pwd):
    global bs,st
    print("Logining")
    headers={"content-type":"application/x-www-form-urlencoded; charset=UTF-8","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82"}
    data={"_token": "Lep0EHXPsInDznO201QMeY14AX8c9VQtXY76AkvmGqJD7mxVk7TAI1bdVj5N",
    "username": acc,
    "password": pwd,"login":"","ip":""}
    re=requests.post("https://qoj.fzoi.top/login",headers=headers,data=data)
    if(re.text=="账号或密码错误"):
        print("%s: Invaild password or username."%acc)
        return
    elif re.text=="banned":
        print("%s: Banned."%acc)
        return
    elif re.text!="ok":
        print("%s: Unknown Error"%acc)
        return
    print("Try to sign")
    headers["cookie"]=re.headers["Set-Cookie"]
    req=requests.get("https://qoj.fzoi.top/punch",headers=headers)
    if req.status_code==200:
        doc=pq(requests.get("https://qoj.fzoi.top",headers=headers).text)
        b=list(doc(".card-body").items())[7].text()
        print("%s OK, Time:%.2fs\n%s\n------------------------------------------"%(acc,time.time()-st,b))
    elif req.status_code==403:
        doc=pq(requests.get("https://qoj.fzoi.top",headers=headers).text)
        b=list(doc(".card-body").items())[7].text()
        print("%s Already Signed, Time: %.2fs\n%s\n------------------------------------------"%(acc,time.time()-st,b))
    else: raise Exception("Unknown Error")
    bs.append(b)
print("FZQOJ Auto Sign System By Ariasaka v4.0.0\n------------------------------------------\nStart Processing")
stt=time.time()
for acc,pwd in accounts.items():
    st=time.time()
    try:
        print("Task #%d\nRunning %s"%(k,acc))
        run(acc,pwd)
        ok+=1
    except Exception as e:
        print("%s Failed\n%s\n------------------------------------------"%(acc,e))
        for i in range(1,3):
            try:
                print("Running %s (Retrying #%d)"%(acc,i))
                run(acc,pwd)
                ok+=1
            except:
                print("%s #%d Still Failed\n%s\n------------------------------------------"%(acc,i,e))
    k+=1
day,rp=0,0
for string in bs:
    r=re.findall("你已经连续签到 (.*?) 天，今日获得 (.*?) RP值和 1 硬币",string)
    day+=int(r[0][0])
    rp+=int(r[0][1])
print("Arrage Days: %.2f && Today RP: %.2f && Total Time: %.2fs"%(day/ok,rp/ok,time.time()-stt))
