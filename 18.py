import requests

platform = {
    'name': '超级直播秀场',
    'id': '18',
    'img': 'http://img5.anzhi.com/data3/icon/201703/02/com.chaomoshow.live_94803500_48.png'
}


class Router(object):
    def __init__(self):
        self.base_url = "http://app.live.sinashow.com/hot"
        self.query = "?page={page}&qid=29006&reg_mac=11674927b4464a6acccb3213e3ca67a9" \
                     "&token=55fc51bf427f130217ac1443ee179307&user_id=881599953&version=1.8.8&hot_type=1"
        self.headers = {
            "Cookie2": "$Version=1",
            "Host": "app.live.sinashow.com",
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi Note 3 Build/MMB29M) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
        }
        self.cookies = {
            "PHPSESSID": "jh1tg9vgujkfv918v7fiu3tcg6"
        }

    def get_list(self) -> list:
        ret = []
        page = 1

        while True:
            query = self.query.format(page=page)
            url = self.base_url + query
            resp = requests.get(url=url,
                                headers=self.headers,
                                cookies=self.cookies)
            page += 1
            resp = resp.json()
            code = resp['code']
            if code == 0:
                break

            rooms = resp['info']

            for room in rooms:
                tmp = dict()
                tmp['pid'] = platform['id']
                tmp['name'] = room["name"]
                tmp['rid'] = room['phid']
                tmp['title'] = room['title']
                tmp['avatar'] = self.get_avatar(room)
                tmp['url'] = room['url']

                ret.append(tmp)
        return ret

    @staticmethod
    def get_avatar(room):
        id = room['id']
        phid = room['phid']
        return "http://img.live.sinashow.com/pic/avatar/{id}_{phid}_200*200.jpg".format(id=id, phid=phid)

    @staticmethod
    def get_address(rid) -> str:
        pass

    def xx_crawl(self):
        pass


def main():
    router = Router()
    ls = router.get_list()
    print(ls)
    print(len(ls))


if __name__ == '__main__':
    main()
