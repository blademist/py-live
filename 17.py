import requests

platform = {
    'name': '暖暖直播',
    'id': '17',
    'img': 'http://appimg.hicloud.com/hwmarket/files/application/icon144/0a900f6e6c4c4b3a9e0b719885c39ae1.png'
}


class Router(object):
    def __init__(self):
        self.url = "http://www.nuannuanzhibo.com//call.do?cmd=live.newList"
        self.data = 'eZlN79acnZdnb3ff8A4FYsOghSh5hDTk9Q8j27EGkBoBK2mofShsPP2NrumEKq44u/SZsCG/z8M7864sRPPoUweoTv5Iq6jjcF4KwiiMzQqQyUjaEVfWn5ah5dbvqH0XNpmEThzC+kSI0yW2CbHkkQ=='
        self.headers = {
            "Charset": "UTF-8",
            "Content-Type": "application/json",
            "Host": "www.nuannuanzhibo.com",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi Note 3 MIUI/6.11.3)",
            "headKey": "eZlN79acnZdnb3ff8A4FYsOghSh5hDTk9Q8j27EGkBqhbK5dhXVlIZi3iaPrBP5DYV9HQAmDfEn5l/ui9KbM5MchpkE4nVPwndpu2lLWerbed2Z7M1SNWTHGRgDpbWi6uXVGlC070m6E0cc8WHaJHAMdH38btA5QmBPseA1WJ8YWABt+vrC07/VY3QJTIkxosHMbXQUdHyo0glry7/xbWzBJYMUU/TdbM1dp5FnxgzGM/H8w0+LCVbSWPoYxf28wCI/WGexaqoYptb/1VHSdnmy3Oxg5FAd2c6qTbGyNgqi0VP2xyJSdK48gb3GcPqko76J6JxyUoAqph2Pp3Nf0sFjiokB75E5K3nDNwEOr+FYsPZcIOe6vGWiVbS3oAHqDyc/BbYjMKrP2mprakDjSGmLwcTFgekiHZYq9OGRFwUGcgjnQMskJdk971p5kHomtQb0l41w60QfUP5WasFUn3RjAsHSA9GJuk8Hu8OCCWvJOUYYk63fnMvfOUb/zDOYLLMtH4w3UtC64++8nnskSxjk8uMfUaAkyVAqVIRYYFEMRsu4kSvMtRt0wQ7mx53hl6OURzMEO/zLtBSOEHNPlM2abzWUzln0a"
        }

    def get_list(self) -> list:
        ret = []
        resp = requests.post(url=self.url,
                             data=self.data,
                             headers={
                                 "Charset": "UTF-8",
                                 "Content-Type": "application/json",
                                 "Host": "www.nuannuanzhibo.com",
                                 "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi Note 3 MIUI/6.11.3)",
                                 "headKey": "eZlN79acnZdnb3ff8A4FYsOghSh5hDTk9Q8j27EGkBqhbK5dhXVlIZi3iaPrBP5DYV9HQAmDfEn5l/ui9KbM5MchpkE4nVPwndpu2lLWerbed2Z7M1SNWTHGRgDpbWi6uXVGlC070m6E0cc8WHaJHAMdH38btA5QmBPseA1WJ8YWABt+vrC07/VY3QJTIkxosHMbXQUdHyo0glry7/xbWzBJYMUU/TdbM1dp5FnxgzGM/H8w0+LCVbSWPoYxf28wCI/WGexaqoYptb/1VHSdnmy3Oxg5FAd2c6qTbGyNgqi0VP2xyJSdK48gb3GcPqko76J6JxyUoAqph2Pp3Nf0sFjiokB75E5K3nDNwEOr+FYsPZcIOe6vGWiVbS3oAHqDyc/BbYjMKrP2mprakDjSGmLwcTFgekiHZYq9OGRFwUGcgjnQMskJdk971p5kHomtQb0l41w60QfUP5WasFUn3RjAsHSA9GJuk8Hu8OCCWvJOUYYk63fnMvfOUb/zDOYLLMtH4w3UtC64++8nnskSxjk8uMfUaAkyVAqVIRYYFEMRsu4kSvMtRt0wQ7mx53hl6OURzMEO/zLtBSOEHNPlM2abzWUzln0a"
                             })
        rooms = resp.json()['list']
        for room in rooms:
            tmp = dict()

            tmp['pid'] = platform['id']
            tmp['name'] = room["name"]
            tmp['rid'] = room['id']
            tmp['title'] = room['name']
            tmp['avatar'] = room['head']
            tmp['url'] = room['url']

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
