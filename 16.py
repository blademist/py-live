import requests

platform = {
    'name': '维秀直播',
    'id': '16',
    'img': 'http://appimg.hicloud.com/hwmarket/files/application/icon144/1e7ab30e03514632863746fcb26d3175.png'
}


class Router(object):
    def __init__(self):
        self.url = "http://service-vshow.ttddsh.com/room!getRoomListForMobile"
        self.data = {
            "numStart": 0,
            "numOffset": 30
        }
        self.headers = {
            "Host": "service-vshow.ttddsh.com",
            "User-Agent": "okhttp/3.2.0"
        }

    def get_list(self) -> list:
        ret = []
        page = 0
        while True:
            self.data['numStart'] = page
            page += 1
            resp = requests.post(url=self.url, data=self.data, headers=self.headers)
            rooms = resp.json()['list']
            for room in rooms:
                # 第一次出现这个为空后，后面都是历史的了
                if room["liveUrl"] == "":
                    return ret
                tmp = dict()
                tmp['pid'] = platform['id']
                tmp['name'] = room["showerName"]
                tmp['rid'] = room['roomId']
                tmp['title'] = room['roomName']
                tmp['avatar'] = room['imgMin']
                tmp['url'] = self.get_address(room)
                ret.append(tmp)

    @staticmethod
    def get_address(item) -> str:
        return item['liveUrl'] + item['liveCode']

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