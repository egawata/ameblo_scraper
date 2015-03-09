import bs4
import re
import urllib.request

def get_text_content(url):
    """Scrape Ameblo page specified by url, and return its title and content"""

    res = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(res.read())
    title = soup.find(attrs={'class': 'skinArticleTitle'})
    article_text = soup.find(attrs={'class': 'articleText'})
    texts = [ 
        elem 
        for elem in article_text.contents 
        if (isinstance(elem, bs4.element.NavigableString)  
            and elem.find('google_ad_section_') == -1
        )
    ]

    if title:
        title_text = title.contents[0].strip()

    content = ' '.join([ t.strip() for t in texts ]).strip()

    return { 'title': title_text, 'content': content }

# get_text_content('http://ameblo.jp/egawata/entry-11590345027.html')


