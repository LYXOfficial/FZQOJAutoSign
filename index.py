import time,re,warnings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
chrome_options = Options()
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
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
    global bs
    browser.get("https://qoj.fzoi.top/login")
    browser.refresh()
    print("Logining")
    if acc in browser.execute_script("return document.body.innerHTML"):
        browser.execute_script("""document.querySelectorAll(".nav-link")[document.querySelectorAll(".nav-link").length-1].click()""")
    rp=20
    while(1):
        if not rp:
            print("Time out")
            raise Exception
        if not browser.execute_script("""return document.querySelector("[name='username']")==null"""):
            break
        time.sleep(0.5)
        rp-=1
    browser.execute_script("""document.querySelector("[name='username']").value="%s";document.querySelector("[name='password']").value="%s";document.querySelector("#button-submit").click()"""%(acc,pwd))
    print("Waiting For Login")
    rp=20
    while(1):
        if not rp:
            print("Time out")
            raise Exception
        try:
            if "签到" in browser.execute_script("""return document.querySelectorAll(".card-body")[7].innerText"""):
                break
        except: pass
        try:
            if "错误" in browser.execute_script("""return document.body.innerText"""):
                print("%s: Invaild Password\n------------------------------------------"%acc)
                return
        except: pass
        time.sleep(0.5)
        rp-=1
    try:
        b=browser.execute_script("""return document.querySelectorAll(".card-body")[7].innerText""")
        if "你已经连续签到" in b:
            print("%s Already Signed\n%s\n------------------------------------------"%(acc,b))
            bs.append(b)
            return
    except:
        pass
    print("Try to Click")
    browser.execute_script("""document.querySelector(\'.btn.btn-primary.btn-lg\').click()""")
    time.sleep(2)
    b=browser.execute_script("""return document.querySelectorAll(".card-body")[7].innerText""")
    print("%s OK\n%s\n------------------------------------------"%(acc,b))
    bs.append(b)
browser = webdriver.Chrome(options=chrome_options,executable_path='./chromedriver')
print("FZQOJ Auto Sign System By Ariasaka v3.2.0\n------------------------------------------\nStart Processing")
for acc,pwd in accounts.items():
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
            browser.delete_all_cookies()
    browser.delete_all_cookies()
    k+=1
day,rp=0,0
for string in bs:
    r=re.findall("你已经连续签到 (.*?) 天，今日获得 (.*?) RP值和 1 硬币",string)
    day+=int(r[0][0])
    rp+=int(r[0][1])
print("Arrage Days: %.2f && Today RP: %.2f"%(day/ok,rp/ok))
