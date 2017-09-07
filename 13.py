import requests


platform = {
    'name': '比艺直播',
    'id': '13',
    'img': 'http://1.pic.pc6.com/thumb/up/2017-4/20174178394129036233_160_160.png'
}


class Router(object):
    def __init__(self):
        self.url = "http://www.17biyi.cn/biyi-api/biyi/live/getHotRoomList"
        self.data = 'oauth_signature_method=HMAC-SHA1&oauth_consumer_key=d690ae490693370caa8b37dafb635a79&oauth_version=1.0&oauth_timestamp=1501830578&oauth_nonce=e00362bf9a361bd66f7d5966edc935ee&oauth_token=3026031_95fcbd992e22c6c4307e4e2e3cf1982b&oauth_signature=mKVtnxdJtY8nztZM%2BgsD1IuK3tA%3D'
        self.headers = {
            "Host": "www.17biyi.cn",
            "User-Agent": "okhttp/2.5.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }

    def get_list(self) -> list:
        """没有分页"""
        resp = requests.post(url=self.url,
                             data=self.data,
                             headers=self.headers)
        ret = []
        rooms = resp.json()['result']
        for room in rooms:
            tmp = dict()
            tmp['pid'] = platform['id']
            tmp['name'] = room["nickname"]
            tmp['rid'] = room['gid']
            tmp['title'] = room['levelTitle']
            tmp['avatar'] = room['face_url']
            tmp['url'] = room['streamAddr']

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
