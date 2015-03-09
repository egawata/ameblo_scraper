import urllib.request
import bs4
 
def get_entry_list(username, page=1):
    """Parse entries in entrylist of page and return its URL and title"""
   
    url = 'http://ameblo.jp/%s/entrylist-%d.html' % (username, page) 
    res = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(res.read())
   
    entries = soup.findAll(attrs={'class': 'contentTitle'})
    entry_list = [ {'title': entry.text, 'href': entry.attrs['href']} for entry in entries ]
    is_last = False if (soup.find(attrs={'class': 'pagingNext'})) else True
    return {'entry_list': entry_list, 'is_last': is_last}

         
    
            
