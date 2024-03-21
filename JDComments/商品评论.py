"""
采集京东商品评论, 并制作词云图 (爬虫 + 数据分析)

https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1698736264206&loginType=3&uuid=122270672.1675327822068798256204.1675327822.1698672561.1698736093.11&productId=100066896472&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1&bbtf=&shield=
"""
import requests
import csv

with open('jingdong.csv', mode='a', newline='', encoding='utf-8-sig') as f:
    csv.writer(f).writerow(['referenceName', 'referenceTime', 'productSize', 'productColor', 'content'])

headers = {
    'Cookie': '__jdu=1675327822068798256204; shshshfpa=a8c4d3ab-4de2-1594-07c6-96937703bc48-1675511732; shshshfpx=a8c4d3ab-4de2-1594-07c6-96937703bc48-1675511732; shshshfp=df23b3178a68c52485e728025047439d; _pst=jd_7449b8b770c1a; unick=u_y14qxm7bysay; pin=jd_7449b8b770c1a; _tp=vZPPhy6cqARc6L2%2B3nOzUq3kCs2OWuApKpEwLezV01A%3D; b_dw=1903; b_dh=962; b_dpr=1; b_webp=1; b_avif=1; autoOpenApp_downCloseDate_auto=1698495726388_1800000; unpl=JF8EAMhnNSttChlQBRNWTBBDQwgDW11aQkcKPGIFAw1cSAFVGlUSRhZ7XlVdXxRLFh9tZhRUVVNPUw4YAysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwUFEleUldeC0oQCmlvDFdZX0hVACsDKxUge21QV10LTxYzblcEZB8MF1YGHgoYFF1LWlJaXwtNHgBsZgJdW1BCVwEcARoXIEptVw; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_cc519ef3b9df41c8a8b41fa52da0f8e7|1698666995221; joyya=1698667578.1698667580.21.0xzc5bv; areaId=18; logintype=qq; npin=jd_7449b8b770c1a; jsavif=1; __jda=122270672.1675327822068798256204.1675327822.1698672561.1698736093.11; __jdc=122270672; 3AB9D23F7A4B3CSS=jdd03BFXLLB72GO2GWA4OW3JSYXJPOVRF3WAKAKETOTSMNISZ6VIJTLEVQKEHWUA6VLD7ORS2QYC55PWBVUZVPZTXPDCHZUAAAAMLQSH3OYIAAAAAD4RUN3GAWKCUHYX; mba_muid=1675327822068798256204; wlfstk_smdl=19mco020eodmiecb9ue3qff20j37jnzl; thor=459E9A0707CDD36020E74D14717A705AD6CEE67A8D55FEDAACBD33B9D31511E6B5CD49A1E4AE44646F96C758F129CA7A6E3B430314D35AFBABB127B37FD38BC585AAD5A247030DDEC70F8244A0301A9884FFA87CAEA8D000B10664FB3E8918296F528D39F39D8298EFD6B2BD2FCAC9FF4B8D691D7F84452637148FA58200FA7CBA6E7217B9C58CF5BACDDC307CE31F182DECBE5FC83F2FC49FE0126582183146; flash=2_NNQxFsqkWofS9naUTFtBfMwjYp5humv_wP8odmT2ndD_SE6ehmDsPQIIzIh4L76M-zL3SADByLnqzs0es3GwK_A5afPUrbau6ln7FGUTqWM*; pinId=f_SKjtPUQ3D1_NrwwoSZkrV9-x-f3wj7; 3AB9D23F7A4B3C9B=BFXLLB72GO2GWA4OW3JSYXJPOVRF3WAKAKETOTSMNISZ6VIJTLEVQKEHWUA6VLD7ORS2QYC55PWBVUZVPZTXPDCHZU; token=24bd9dde8ce17c6891c24d925759a9f1,3,943742; __tk=ArXuBUg0jrArBUhu4rhujugzAuW5ArawkUew4UkpkrgE4Ueyjuhrjg,3,943742; shshshsID=d5a4d986826b087b362780a6400c4f07_1_1698736114189; __jdb=122270672.5.1675327822068798256204|11.1698736093; shshshfpb=AAigKkISLEsTTq03iFZQHxpaTdwO8SBZ1URcyWwAAAAA; ipLoc-djd=18-1482-48942-49058',
    'Origin': 'https://item.jd.com',
    'Referer': 'https://item.jd.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
for page in range(10):
    url = f'https://api.m.jd.com/?appid=item-v3&functionId=pc_club_productPageComments&client=pc&clientVersion=1.0.0&t=1698736264206&loginType=3&uuid=122270672.1675327822068798256204.1675327822.1698672561.1698736093.11&productId=100066896472&score=0&sortType=5&page={page}&pageSize=20&isShadowSku=0&rid=0&fold=1&bbtf=&shield='
    print(url)
    response = requests.get(url=url, headers=headers)
    json_data = response.json()
    comments = json_data['comments']
    for comment in comments:
        content = comment['content']
        productColor = comment['productColor']
        referenceName = comment['referenceName']
        productSize = comment['productSize']
        referenceTime = comment['referenceTime']
        print(referenceName, referenceTime, productSize, productColor, content)
        with open('jingdong.csv', mode='a', newline='', encoding='utf-8-sig') as f:
            csv.writer(f).writerow([referenceName, referenceTime, productSize, productColor, content])