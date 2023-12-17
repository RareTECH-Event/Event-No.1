import requests

def post_code():
    zipcode = input("郵便番号を入力：> ")
    # 郵便番号検索APIのURLを定数化する
    URL = 'https://zipcloud.ibsnet.co.jp/api/search'
    # paramsで検索したい郵便番号を渡す
    res = requests.get(URL, params={'zipcode': zipcode})
    print(res.json())

