import requests

platform = {
    'name': '9513直播',
    'id': '14',
    'img': 'http://appimg.hicloud.com/hwmarket/files/application/icon144/b3f13b01c03f4d4c806c60106c6903fc.png'
}


class Router(object):
    def __init__(self):
        self.url = "http://api.9513.com/phone/getroomlistnew.ashx"
        self.params = {
            "p": "index",
            "device": 1
        }
        self.headers = {
            "Host": "api.9513.com",
            "User-Agent": "okhttp/3.3.1"
        }

    def get_list(self) -> list:
        resp = requests.get(url=self.url,
                            params=self.params,
                            headers=self.headers)
        ret = []
        data_list = resp.json()['dataList']

        for data in data_list:
            rooms = data['list']
            for room in rooms:
                tmp = dict()
                tmp['pid'] = platform['id']
                tmp['name'] = room["nick"]
                tmp['rid'] = room['idx']
                tmp['title'] = room['nick']
                tmp['avatar'] = room['hb']
                tmp['url'] = room['stream']

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


if __name__ == '__main__':
    main()
