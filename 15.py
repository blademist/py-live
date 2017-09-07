import requests
platform = {
    'name': 'VV直播',
    'id': '15',
    'img': 'http://appimg.hicloud.com/hwmarket/files/application/icon144/13234c2011e54dbe83a423b9120f94fd.png'
}


class Router(object):
    def __init__(self):
        self.url = "http://live.51vv.com/api/live/ghotlivepage.htm"
        self.params = {
            "province": "",
            "gender": "",
            "topic": "",
            "curPage": 1,
            "viewNumber": 200
        }

        self.headers = {
            "Host": "live.51vv.com",
            "User-Agent": "okhttp/2.7.5",
            "X-CHANNEL": "2004",
            "X-CID": "d08a8bf1dab80556b41cf159e73c2ba1",
            "X-MODEL": "RedmiNote3",
            "X-OS": "6.0.1",
            "X-PLATFORM": "Android",
            "X-PRODUCT": "vvlive",
            "X-PUSHCID": "f4eb5aafbdb5cf12802576b5177320a9",
            "X-TOKEN": "d5dab07cd5454cb491649fef05abc127",
            "X-VER": "3.5.2.4"
        }

    def get_list(self) -> list:

        ret = []
        page = 1
        while True:
            self.params['curPage'] = page
            page += 1
            resp = requests.get(url=self.url,
                                params=self.params,
                                headers=self.headers)

            room_list = resp.json()['lives']
            if len(room_list) == 0:
                break

            for item in room_list:
                tmp = dict()
                tmp['pid'] = platform['id']
                tmp['name'] = item["nickName"]
                tmp['rid'] = item['liveID']
                tmp['title'] = item['description']
                tmp['avatar'] = item['userImg']
                tmp['url'] = item['streamUrl']

                ret.append(tmp)
        return ret

    def get_address(self) -> str:
        pass

    def xx_crawl(self):
        data = self.get_list()
        print(data)


def main():
    router = Router()
    ls = router.get_list()
    print(ls)
    print(len(ls))


if __name__ == '__main__':
    main()
