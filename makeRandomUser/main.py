import requests

def getRandomUser():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    if response.status_code != 200:
        return f"データ取得に失敗しました。コード:{response.status_code}"
    data = response.json()
    user = data['results'][0]

    return user

def main():
    while True:
        print('ランダムにユーザー情報を生成します。生成するには1を、止めるには2を入力してください。')
        userInput = input('>')
        if userInput == '2':
            break

        user = getRandomUser()
        print(f"名前: {user['name']['first']} {user['name']['last']}")
        print(f"メール: {user['email']}")
        print(f"国: {user['location']['country']}")
        print(f"画像URL: {user['picture']['large']}")

if __name__ == '__main__':
    main()
