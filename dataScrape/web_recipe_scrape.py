import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp


url = 'https://www.skinnytaste.com'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

links = soup.select('article.post.teaser-post') #.odd + .even
article_imgs = soup.select('img.lazyload.attachment-teaser.size-teaser.wp-post-image')
article_title = soup.select('h2.title')
article_summary = soup.select('p.excerpt')
article_more_link = soup.select('a.more-link')
#article_meta_icons = soup.select('div.icons')
article_blue_points = soup.select('span.smart-points.blue')
article_green_points = soup.select('span.smart-points.green')
article_purple_points = soup.select('span.smart-points.purple')
article_cals = soup.select('span.icon-star')
# print(len(links))
# print(len(article_imgs))
# print(len(article_title))
# print(len(article_summary))
# print(len(article_blue_points))
# print(len(article_green_points))
# print(len(article_purple_points))
# print(len(article_cals))
# print(len(article_meta_icons))
# print(len(article_meta_icons[1].findAll('span', recursive=False))) #.find('img').get('alt'))

def skinny_content(links):
    st = []
    for idx, article in enumerate(links):
        meta = []
        #Not all articles have icons so get it here
        div_icon = article.find('div', {"class":"icons"})
        if div_icon:
            span_icons = div_icon.findAll('span', recursive=False)
            for j, mta in enumerate(span_icons):
                meta.append(mta.find('img').get('alt'))

        st.append([article_title[idx].text, article_imgs[idx].get('data-src'), article_summary[idx].text, 
                    article_more_link[idx].get('href'), article_blue_points[idx].text, article_green_points[idx].text,
                    article_purple_points[idx].text, article_cals[idx].text, article_imgs[idx].get('alt'), meta])

    return st

article_data = skinny_content(links)
print(article_data)
print(f'{len(article_data)} articles found......end!')
