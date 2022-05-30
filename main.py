# url = 'https://dazi.kukuw.com/'
import time
import selenium.webdriver
from bs4 import BeautifulSoup

if __name__ == '__main__':
    text_answer = []
    name_all = []
    edg = selenium.webdriver.Edge(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')  # , options=op
    url = 'https://dazi.kukuw.com/'
    head = {
        'User-Agent': '9Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
    }
    edg.get(url)
    edg.find_element_by_id('radio_cn').click()   # 模拟点击中文文章按钮
    '''可以找到中文文章进行点击'''
    edg.find_element_by_name('start_button').click()
    html = edg.page_source
    soup = BeautifulSoup(html, 'html.parser')
    text_all = soup.find_all('div', class_="text")
    # 找到所有的text上方的div标签
    for text in text_all:
        txt = text.span.string
        text_answer.append(txt)
    name_html = soup.find_all('div', class_='typing typing_on')
    for name in name_html:
        name_all.append(name.input.next_sibling.get('name'))
    # 所有的答案已经拿到，只需要填入input标签即可
    for i in range(34):
        '''可以用列表循环但是i自增会写在循环内部，懒得改了'''
        edg.find_element_by_id('i_{}'.format(str(i))).find_element_by_name(name_all[0]).send_keys(
            text_answer[i])

    time.sleep(20)
    edg.quit()
'''只针对于英语文章，中文文章要多两个click'''
