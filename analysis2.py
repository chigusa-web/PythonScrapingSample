import os
from bs4 import BeautifulSoup

print("HTML解析開始")

# HTMLファイル 保存先のディレクトリ
save_dir = os.path.dirname(os.path.abspath(__file__)) + "/html/"
# HTMLファイルパス
html_file = save_dir + "/chigusa.html"

with open(html_file, encoding='utf-8') as f:

    bsoup = BeautifulSoup(f, "html5lib")

    # HTMLから該当の範囲を取得
    ele = bsoup.select_one("div.postList:nth-child(4)")

    if ele is None:
        print("見つかりませんでした")
    else:
        # h1タグのリストを取得
        allTitles = ele.find_all("h1")
        for h1 in allTitles:
            # h1の中のaタグの表示文字列を取得
            print(h1.select_one("a").string)

print("HTML解析終了")