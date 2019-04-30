import os
from bs4 import BeautifulSoup

print("HTML解析開始")

# HTMLファイル 保存先のディレクトリ
save_dir = os.path.dirname(os.path.abspath(__file__)) + "/html/"
# HTMLファイルパス
html_file = save_dir + "/chigusa.html"

# 保存先テキストファイル
save_file = os.path.dirname(os.path.abspath(__file__)) + "/save.txt"
if os.path.exists(save_file):
    os.remove(save_file)

with open(save_file, 'a', encoding='utf-8') as fw, open(html_file, encoding='utf-8') as f:

    bsoup = BeautifulSoup(f, "html5lib")

    # HTMLから該当の範囲を取得
    ele = bsoup.select_one("div.postList:nth-child(4)")

    if ele is None:
        print("見つかりませんでした")
    else:
        # h1タグのリストを取得
        allTitles = ele.find_all("h1")
        for h1 in allTitles:
            title = h1.select_one("a").string
            # h1の中のaタグの表示文字列を取得
            print(title)
            # テキストファイルに保存
            fw.write(title + "\n")

print("HTML解析終了")