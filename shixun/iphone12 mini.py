import requests
import time
import re
import json
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shixun.settings")
#os.environ.setdefault设置环境变量,这里的online_judge就是你的项目名称
django.setup()
from shixunapp.models import *

for k in range(101):
    url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100016034424&score=0&sortType=5&page='+str(k)+'&pageSize=10&isShadowSku=0&rid=0&fold=1'
    headers={
        'Cookie':'__jda=122270672.16045645684111321421374.1604564568.1610328806.1610334097.9; unpl=V2_ZzNtbUMAQEZzD0BTeExZDWIHQlhKBENGcQhOUChKVVI3VBQIclRCFnUUR1RnGVwUZgsZWUdcQhVFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHseXQBjBBdZRV5GFXUIRFd7HF8FZQUXbXJQcyVFD0dQfhxeNWYzE20AAx8XfQ1EVXJUXAJmBhZaR1NEHHAIRlR5GlwAZAMQW0dnQiV2; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_0f2b76762d4945a49b1b5195bb8faf7d|1610330040439; __jdu=160456456…15; ipLoc-djd=15-1213-3038-59931; shshshfp=289b54b00baf200ac9fb65759665948e; shshshfpa=0cfa2d8c-01bc-0b41-8322-25ae15a8543d-1609813883; shshshfpb=zx38YWB2EDRZ8M6e4lb5L7w%3D%3D; jwotest_product=99; PCSYCityID=CN_330000_0_0; 3AB9D23F7A4B3C9B=5Y54BWANBVLTNMDDGG6P5MZBO4SAB4OBADRQLJ3QNAPU6JO6NPV4V57ZWNTKVQSTAZQ4WRKJHY37VL544S5GVKVJYI; shshshsID=3f24543ba598a43dca9102f18917fe9e_5_1610334182681; __jdb=122270672.6.16045645684111321421374|9.1610334097; __jdc=122270672; JSESSIONID=FC3BC5059CEDA3862E2FE9ABCB693EE5.s1',
    'Referer': 'https://item.jd.com/100016034424.html',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
            }
    req =requests.get(url=url,headers=headers)
    kw=req.text

    a=kw.replace("fetchJSON_comment98(", "")
    b=a.replace(");","")
    jsonData = json.loads(b)
    for data in jsonData["comments"]:
         shujuku = JingdongTaobao(yonghu=data["nickname"],
                         xinghao=(str(data["productColor"])) + '   ' + (str(data["productSize"])),
                         pinglun=data["content"], shijian=data["creationTime"])
         shujuku.save()
         time.sleep(1)
