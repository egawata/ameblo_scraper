import ameblo.page
import ameblo.entrylist
import os.path

basedir = 'entries'
username = 'egawata'

page = 1
last_page = False
while last_page is False:
    entry_list = ameblo.entrylist.get_entry_list(username, page)
    print("\n[Page %d] -------------\n" % page)
    count = 1
    for entry in entry_list['entry_list']:
        content = ameblo.page.get_text_content(entry['href'])
        if content is None: 
            continue
        f = open(os.path.join(basedir, "entry-%d-%d.txt" % (page, count)), "w")
        f.write(content['title'] + ' : ' + content['content'])
        f.close()
        count += 1

    page += 1
    last_page = entry_list['is_last']

print("Done.")

