from multiprocessing.dummy import Pool as ThreadPool
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
start_page=2
end_page=3

def getpageurl(i):
   
    url="http://d1.ef7d6a2b557.rocks/pw/thread.php?fid=14&page="+str(i)#wei
    url="http://d1.ef7d6a2b557.rocks/pw/thread.php?fid=15&page="+str(i)#zi
    titlepage=requests.get(url,timeout=30)#打开标题页面
    titlepage_soup=BeautifulSoup(titlepage.content,'lxml')#解析标题页面
    bs0=titlepage_soup.find_all('a')
    t3= []
    k=0
    for t in bs0:
        t1=t.get('href')
        try:
            t2= re.findall("html\_data(.+)html",t1)
            if t2!=[]:
                t3.append(t2)  #获得重复的二级页面代码
        except:
            continue
            print('out')
    a=len(t3)
    for m in range(int(a/2)):
        t3[m]=t3[k]
        k=k+2
    del t3[int((a/2)):int(a)] 
    return(t3)   #去除重复的元素并返回代号列表
    print(t3)
def spider(surl):
   # http://p8.urlpic.club/pic20190701/upload/image/20200203/20300088902.gif
    a=surl
    print(surl)
    pic=requests.get(a)
    path="D:/s13/%s%%s.jpg"%k%surl[-15:-4]
    try:   
        with open(path,'wb') as f:
            f.write(pic.content)
            f.close()
        #print(pic.status_code,pic.url)
            
    except:
        pass     
    

def getpicurl(x):
    for q in x:
        purl= []
        q=str(q)
        #print(q)
        #http://d1.ef7d6a2b557.rocks/pw/html_data/14/2002/4589477.html
        url2='http://d1.ef7d6a2b557.rocks/pw/html_data'+q+'html'
        print(url2)
        r=requests.get(url2)
        r.encoding="utf-8"
        d=r.text
        soup0=BeautifulSoup(d,'lxml')
        lis=soup0.find('div',attrs={'class':'tpc_content'})
        lis0=soup0.find('h1',attrs={'class':'b'})
        t0=lis0.find_all('span')
        c=t0[0].string
        k=c[0:-5]
        li=lis.find_all('img')
        for q in li:
            la=q.get('src')
            purl.append(la)
        return(k,purl)
        #print(purl)
            


for i in range(start_page,end_page+1):
    print('第'+str(i)+'页')
    #print(getpageurl(i))
    x=getpageurl(i)
    print(x)
    for y in x:
        print(y)
        k,purl=getpicurl(y)
        
            
        pool=ThreadPool(4)
        #print(k)
        #print(purl)
        pool.map(spider,purl)
        pool.close()
        pool.join()
                       






