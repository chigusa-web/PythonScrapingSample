import os
from bs4 import BeautifulSoup

print("HTML解析開始")

# HTMLファイル 保存先のディレクトリ
save_dir = os.path.dirname(os.path.abspath(__file__)) + "/html/"
# HTMLファイルパス
html_file = save_dir + "/chigusa.html"

with open(html_file, encoding='utf-8') as f:

    bsoup = BeautifulSoup(f, "html5lib")

    # HTMLから該当の文字を取得
    ele = bsoup.select_one(".entry-body > h2:nth-child(3)")

    if ele is None:
        print("見つかりませんでした")
    else:
        print("見つかりました：" + ele.string)

print("HTML解析終了")