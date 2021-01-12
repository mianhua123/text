import requests
import re
import json
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shixun.settings")
#os.environ.setdefault设置环境变量,这里的online_judge就是你的项目名称
django.setup()
from shixunapp.models import *
for k in range(1,4):
    url='https://rate.taobao.com/feedRateList.htm?auctionNumId=630068045150&userNumId=24699231&currentPageNum='+str(k)+'&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=&hasSku=false&folded=0&ua=098#E1hvrQvRvp9vUvCkvvvvvjiWPLsUQjiPR2LygjljPmPhtjE8nLzwsjtRRsqZzjrPRvhvChCvvvvVvpvfcr147rYg0kuUu+RMy6hmv9UkFU0C4wEkO98bRvhvChCvvvmvvpvWzCQAOnsNznswPZr439hvChCCvvvvvpvVph9vvvvvkvhvCyn2mvpwVu9Cvv3vpvLXGqTUWd9CvmkMpv25MMYvKZCvVvvvvhHzphvOvvvvpAnvpC9vvvC2J6CvV29vvhWHmvhvLhEyRQmFejwu4Qtr1EeKfvxYoRLZV3O07oDn9Wm/Se9wfvRGACI/wHDqVwex+bxqVmHoDOvXVjifEDRtFLu6b6HIjbmYDb6sBmDaF4hRvpvhvv2MMs9CvvBvpvvvi9hvChCvCCo+vpvEph8WVCGvphO4&_ksTS=1610201806432_2401&callback=jsonp_tbcrate_reviews_list'
    headers = {
        'Cookie': 'miid=2048909418277097228; tfstk=c_lVB_68nIdq1WPLiSNNCzGdNeAAZQqgA_zUnAOVYydv1R2liZSTriWazPW96-f..; cna=+wDzFw9OgEMCAd9o9kWtT3h/; isg=BDU16XGPhgh_e-KxDeCYO0lsR7HvsunEogGiu7da56zujlSAfwC1lWNI2NK41QF8; l=eB_FfMSnOvFYSTzhBOfZlurza77tQIObYuPzaNbMiOCP_R5JYLeVWZ8dDnLvCn1VnsBJR3rKssQJBqY_ay4EhEGfIqlBs2JZndLh.; _m_h5_tk=a12342932e7354d5ac85de6ccf5b4523_1610379936287; _m_h5_tk_enc=0add1fde785d290b64cff6a275335c7e; UM_distinctid=176e556c9912ca-078a0242ea8237-4c3f207e-144000-176e556c994279; hng=CN%7Czh-CN%7CCNY%7C156; …zbAkPf6PlCER1L%2B; tracknick=t_1478410737526_0; _cc_=U%2BGCWk%2F7og%3D%3D; mt=ci=-1_0; enc=PqDHTJg6d%2FiKBSlA14LoXV1naWjA9w8pmtbj9LfTNH46Ee1IBUJK7lJokUhutniB3zg6jdQzP%2FHZAUeuw9kLZQ%3D%3D; xlly_s=1; lLtC1_=1; cookie2=169ed7d89727e49b638f032857f5b14e; uc1=cookie14=Uoe1gqsHpFRzCQ%3D%3D; t=db5714b953bf3653ede73810f2fc0517; _tb_token_=e138115bb3be5; v=0; x5sec=7b22726174656d616e616765723b32223a226531656165323239346239386366643630633465356438646361373038373337434c713438663846454c4c516f396d7a774a7a464f413d3d227d',
        'Referer': 'https://item.taobao.com/item.htm?id=630068045150&ali_refid=a3_430673_1006:1102466130:N:IEFpic726ynfbEx5JZZ3Xv7tthcrkQ91:b642ef54eac64913cac01c83ca2cc5ad&ali_trackid=1_b642ef54eac64913cac01c83ca2cc5ad&spm=a2e0b.20350158.31919782.1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    req =requests.get(url=url,headers=headers)
    kw=req.text
    a = kw.replace("(", "")
    b = a.replace(")", "")
    jsonData = json.loads(b)
    for data in jsonData["comments"]:
        shujuku=JingdongTaobao(yonghu=data["user"]["nick"],xinghao=re.sub('&nbsp', "", data["auction"]["sku"]),pinglun=data["content"],shijian=data["date"])
        shujuku.save()