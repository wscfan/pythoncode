import re

def test_re_img():
    # 1、读取 html
    with open('./data/img.html', encoding='utf-8') as f:
        html = f.read()
        # print(html)
        # 2、准备正则
        p = re.compile(r'<img.+?src=\"(.+?)\".+?>')
        list_img = p.findall(html)
        print(len(list_img))
        with open('./data/img.txt', 'w', encoding='utf-8') as w:
            for img in list_img:
                img_url = img.replace('&amp;', '&')
                w.write(img_url + "\n\n")


if __name__ == '__main__':
    test_re_img()