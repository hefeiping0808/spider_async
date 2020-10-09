**1. 项目简介：**

    单线程异步爬取某个网站的所有小说。
    
**2. 环境依赖：**

    python==3.8.5
    pycharm专业版==2019.3.3 
    bs4==0.0.1
    asyncio==
    aiohttp==
**3. 技术栈：**

    1.asyncio 创建事件循环
    2.re 的 findall 函数对返回文本进行数据筛选
    3.bs4 的 BeautifulSoup 类获取网页返回文本的小说题目和小说文本
    4.aiohttp 对所有小说 url 列表进行异步网路请求
    
**3. 结果展示：**

    获取URL用时 1.0683445930480957
    40 ['2020/10/10/miqingxiaoyuan/478712.html', '2020/10/10/miqingxiaoyuan/478711.html', '2020/10/10/miqingxiaoyuan/478710.html', '2020/10/10/miqingxiaoyuan/478709.html', '2020/10/10/doushijiqing/478708.html', '2020/10/10/doushijiqing/478707.html', '2020/10/10/doushijiqing/478706.html', '2020/10/10/doushijiqing/478705.html', '2020/10/10/jiatingluanlun/478704.html', '2020/10/10/jiatingluanlun/478703.html', '2020/10/10/lingleixiaoshuo/478702.html', '2020/10/10/lingleixiaoshuo/478701.html', '2020/10/10/lingleixiaoshuo/478700.html', '2020/10/10/lingleixiaoshuo/478699.html', '2020/10/10/huangsexiaohua/478698.html', '2020/10/10/huangsexiaohua/478697.html', '2020/10/10/huangsexiaohua/478696.html', '2020/10/10/huangsexiaohua/478695.html', '2020/10/10/xingaijiqiao/478694.html', '2020/10/10/xingaijiqiao/478693.html', '2020/10/10/xingaijiqiao/478692.html', '2020/10/10/xingaijiqiao/478691.html', '2020/10/10/doushijiqing/478690.html', '2020/10/10/renqinvyou/478689.html', '2020/10/10/doushijiqing/478688.html', '2020/10/10/doushijiqing/478687.html', '2020/10/10/doushijiqing/478686.html', '2020/10/10/miqingxiaoyuan/478685.html', '2020/10/10/jiatingluanlun/478684.html', '2020/10/10/jiatingluanlun/478683.html', '2020/10/10/jiatingluanlun/478682.html', '2020/10/10/wuxiagudian/478681.html', '2020/10/10/lingleixiaoshuo/478680.html', '2020/10/7/renqinvyou/478461.html', '2020/10/7/renqinvyou/478460.html', '2020/10/7/renqinvyou/478459.html', '2020/10/7/renqinvyou/478458.html', '2020/10/7/renqinvyou/478457.html', '2020/10/7/renqinvyou/478456.html', '2020/10/7/miqingxiaoyuan/478455.html']
    开始请求 https://222cce.com/htm/2020/10/10/miqingxiaoyuan/478712.html
    ......
    开始请求 https://222cce.com/htm/2020/10/7/miqingxiaoyuan/478455.html
    下载成功 *********
    ......
    下载成功 *********
    总用时 17.952542543411255

**4. 总结：**
    
    1）相比于python3里的多进程，异步请求效率明显比多进程的requests同步请求快很多；
    2）如果使用asyncio.run(main(makeUrl(txt_list)))函数，会抛出raise RuntimeError('Event loop is closed')异常，换成
       loop = asyncio.get_event_loop()
       loop.run_until_complete(main(makeUrl(txt_list)))
       则无异常；但是如果在后者加上一句 loop.close() 则又报上述异常，查看其源码，提示
        """Close the loop.
        The loop should not be running.
        This is idempotent and irreversible.
        No other methods should be called after this one.
        """
        也就是说，事件循环未结束。
        查了很多资料，官方有个文档 https://docs.aiohttp.org/en/latest/client_advanced.html#graceful-shutdown 给出的建议是：
        如果请求的 url 是 https ，则需要在 loop.close() 前面加一句 loop.run_until_complete(asyncio.sleep(time))，参数 time 设置越大则报错率越低，此程序设置成 time=1 时则不报错。