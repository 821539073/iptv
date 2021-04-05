import requests
import json
url = "https://raw.githubusercontent.com/iptv-org/iptv/master/channels/cn.m3u"
req = requests.get(url)
resultlist = req.text.split("#EXTINF:-1 tvg-id=")
ruturnlist=[]
for itme in resultlist:
    if "group-title=" in itme:
        tempiptvinfo = itme.split("\",")[1]
        iptvinfo = tempiptvinfo.replace("\n","")
        allinfostr = tempiptvinfo.replace("\n","")
        allinfolist = allinfostr.replace("http","\nhttp").split("\n")
        if(len(allinfolist)) != 1:
            print("频道名称:"+allinfolist[0]+"频道URL:"+allinfolist[1])
            ruturndic = {'iptvname':allinfolist[0],'iptvurl':allinfolist[1]}
            ruturnlist.append(ruturndic)
            print(ruturndic)
        else:
            print('error')
        
    else:
        print("errortype")

diclist = {'iptvlist':ruturnlist}
#print(json.dumps(diclist,ensure_ascii=False))
f1 = open("iptv.json", "w")
f1.seek(0)
f1.truncate()  # 清空
f1.write(json.dumps(diclist,ensure_ascii=False))
f1.close()
