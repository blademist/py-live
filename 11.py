import requests

platform = {
    'name': '17直播吧',
    'id': '11',
    'img': 'http://appimg.hicloud.com/hwmarket/files/application/icon144/0534a32d29a54d569bc39f616492d729.png'
}


class Router(object):
    def __init__(self):
        self.url = "http://shangtv.cn:3003/recommand_list"
        self.params = {
            "uid": "194078"
        }

    def get_list(self) -> list:
        resp = requests.get(url=self.url, params=self.params)
        room_list = resp.json()['RoomList']
        ret = []
        for item in room_list:
            tmp = dict()
            tmp['pid'] = platform['id']
            tmp['name'] = item["nick_name"]
            tmp['rid'] = item['nick_name']
            tmp['title'] = item['room_name']
            tmp['avatar'] = item['image']
            tmp['url'] = item['flv_url']

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
