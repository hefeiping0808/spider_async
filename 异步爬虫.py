import requests, re, time, aiohttp, asyncio
from bs4 import BeautifulSoup
# https://222cce.com/
# https://222cce.com/xiaoshuo/list_120.html
# 拼接URL
def makeUrl(list):
    list1 = []
    for l in list:
        if 'xingaijiqiao' in l or 'huangsexiaohua' in l:
            pass
        else:
            list1.append('https://222cce.com/htm/' + l)
    return list1
def getStoryUrl(url):
            try:
                res = requests.get(url=url, timeout=(10, 15))
                res.encoding = 'utf-8'
                l = re.findall('href="/htm/(.*?)"', res.text, re.S)
                return l
            except Exception as e:
                # print(e)
                return []
            return []
async def getText(url):
    try:
        print('开始请求 '+url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as g:
                res = await g.text(encoding='utf-8')
                # await asyncio.sleep(1)
                soup = BeautifulSoup(res, 'lxml')
                title = soup.find('h1').text
                text = soup.find('div', class_='content').text
        with open('.\story\\'+title+'.txt', 'w', encoding='utf-8') as f:
            f.write(text)
            print('下载成功 '+title)
            f.close()
    except Exception as e:
        pass
        # print(e)
async def main(list):
    await asyncio.gather(*[getText(l) for l in list])
if __name__ == '__main__':
    page_url = []  # 每个翻页内的小说URL
    starttime = time.time()
    txt_list = getStoryUrl('https://222cce.com/xiaoshuo/index.html')
    print(f'获取URL用时 {time.time() - starttime}')
    print(len(txt_list), txt_list)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(makeUrl(txt_list)))
    loop.run_until_complete(asyncio.sleep(1))
    loop.close()
    print(f'总用时 {time.time()-starttime}')
