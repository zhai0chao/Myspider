#coding:utf-8
import requests
import urllib2
import json
def spider():
    ssion = requests.session()
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
                "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,und;q=0.6",
                "cookie":"SINAGLOBAL=9257282730239.717.1555940566755; Ugrow-G0=589da022062e21d675f389ce54f2eae7; wvr=6; TC-V5-G0=4c4b51307dd4a2e262171871fe64f295; _s_tentry=www.sina.com.cn; UOR=,,www.sina.com.cn; Apache=5574777392328.656.1560391484234; wb_view_log_6704607176=1440*9002; ULV=1560391484251:2:1:1:5574777392328.656.1560391484234:1555940566785; cross_origin_proto=SSL; login_sid_t=66da5f5582519ddc3ccbcd4592823929; WBStorage=6b696629409558bc|undefined; wb_view_log=1440*9002; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFR8BKZyvJ_2enPijG42AOo5JpX5K2hUgL.FoqNehBcehMpS0q2dJLoIpXLxK.L1KzLBo-LxK.L1KzLBo-LxK.LBonLBK89-5tt; ALF=1591928321; SSOLoginState=1560392321; SCF=AvFikMv3Ok4JAtvI79FtIjZDv9GCne8UwAGc3NcVrdZJazuw5djHMAstHpBLNcscAmZibMlVtmcJbwnNQW8aV2g.; SUB=_2A25wBcLRDeRhGeBJ61YX8CnNzDqIHXVTcrMZrDV8PUNbmtAKLRTkkW9NRnUVeZLWdgQ7-wWwtXxtU-WGQZndXob3; SUHB=0Ela8Vo3yhZpgB; un=13241458088; TC-Page-G0=c4376343b8c98031e29230e0923842a5|1560392326|1560392326; webim_unReadCount=%7B%22time%22%3A1560392335760%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A7%2C%22msgbox%22%3A0%7D",

                }
    urls = 'https://weibo.com/6704607176/info'
    #mycookie = {"cookie":"SINAGLOBAL=9257282730239.717.1555940566755; Ugrow-G0=589da022062e21d675f389ce54f2eae7; wvr=6; TC-V5-G0=4c4b51307dd4a2e262171871fe64f295; _s_tentry=www.sina.com.cn; UOR=,,www.sina.com.cn; Apache=5574777392328.656.1560391484234; wb_view_log_6704607176=1440*9002; ULV=1560391484251:2:1:1:5574777392328.656.1560391484234:1555940566785; cross_origin_proto=SSL; login_sid_t=66da5f5582519ddc3ccbcd4592823929; WBStorage=6b696629409558bc|undefined; wb_view_log=1440*9002; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFR8BKZyvJ_2enPijG42AOo5JpX5K2hUgL.FoqNehBcehMpS0q2dJLoIpXLxK.L1KzLBo-LxK.L1KzLBo-LxK.LBonLBK89-5tt; ALF=1591928321; SSOLoginState=1560392321; SCF=AvFikMv3Ok4JAtvI79FtIjZDv9GCne8UwAGc3NcVrdZJazuw5djHMAstHpBLNcscAmZibMlVtmcJbwnNQW8aV2g.; SUB=_2A25wBcLRDeRhGeBJ61YX8CnNzDqIHXVTcrMZrDV8PUNbmtAKLRTkkW9NRnUVeZLWdgQ7-wWwtXxtU-WGQZndXob3; SUHB=0Ela8Vo3yhZpgB; un=13241458088; TC-Page-G0=c4376343b8c98031e29230e0923842a5|1560392326|1560392326; webim_unReadCount=%7B%22time%22%3A1560392335760%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A7%2C%22msgbox%22%3A0%7D"}
    #利用session登录
    response = ssion.get(url=urls,headers=headers)
    res = response.text
    print response.url
    print response.headers
    print response.cookies
    print response.encoding
    #print(requests.utils.add_dict_to_cookiejar(,cookie_dict=cookiejar))
    #print(res)



    #response = requests.get(url=urls,handers=handers)




if __name__ == '__main__':
    spider()