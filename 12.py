import requests

platform = {
    'name': '人气直播',
    'id': '12',
    'img': 'http://appimg.hicloud.com/hwmarket/files/application/icon144/6f9b402cef714f29b3223f7938b361f8.png'
}


class Router(object):
    def __init__(self):
        self.url = "http://123.207.176.15/room/getRooms"
        self.params = {
            "page": 7,
            "status": 1,
            "platform": "android",
            "packageId": 4,
            "channel": "and-huawei-4",
            "deviceName": "Motorola+Nexus+6"
        }
        self.cookie = {
            "PHPSESSID": "25ua2fsf952it34al61q91uqh7",
            "__DAYU_PP": "zybvQvJYmVAefi2nAzYiffffffff87770da1ba07",
            "uid": "10171253"
        }
        self.headers = {
            "Content-Type": "multipart/form-data; boundary=c4h624jCl1dan5Kr7sSaQkqAAhTdGdig",
            "Cookie2": "$Version=1",
            "Host": "123.207.176.15",
            "User-Agent": "mobile"
        }

    def get_list(self) -> list:
        page = 0
        ret = []
        while True:
            self.params['page'] = page
            page += 1
            resp = requests.get(url=self.url,
                                params=self.params,
                                headers=self.headers,
                                cookies=self.cookie)
            room_list = resp.json()['data']
            # empty
            if not len(room_list):
                break

            for item in room_list:
                tmp = dict()
                tmp['pid'] = platform['id']
                tmp['name'] = item["nickname"]
                tmp['rid'] = item['rid']
                tmp['title'] = item['announcement']
                tmp['avatar'] = item['headPic']
                tmp['url'] = item['videoPlayUrl']
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
