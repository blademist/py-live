import requests
import json
import hashlib

platform = {
    'name': '由于直播',
    'id': '20',
    'img': "http://www.anzhi.com/icon.php?u=ZGF0YTN8aWNvbnwyMDE3MDR8MTh8b2Qxc0MzQjFIMTJGdE4xNFdoTXM0WDYvNWQyYWE5VlZoUWl5NzYyejlXTT0="
}


class Router(object):
    def __init__(self):
        self.search_url = 'http://api.youyulive.com/api/livelist/hot/search'
        self.room_info_url = 'http://api.youyulive.com/api/livelist/roominfo'
        self.search_params = {
            "province": "",
            "gender": 2,
            "pnum": 1,
            "pamount": 200
        }
        self.room_info_params = {
            "roomid": 68815,
            "userid": ""
        }
        self.headers = {
            "Host": "api.youyulive.com",
            "User-Agent": "okhttp/3.4.2",
            "appversion": "1.2.8",
            "channelid": "1",
            "os": "android",
            "subchannelid": "20"
        }

    def get_list(self) -> list:
        page = 1
        ret = []

        while True:
            self.search_params['pnum'] = page
            page += 1
            sign = self.sign_params(self.search_params)
            params = self.search_params.copy()
            params['signature'] = sign
            resp = requests.get(url=self.search_url,
                                params=params,
                                headers=self.headers)
            resp = resp.json()
            rooms = resp['data']
            if len(rooms) == 0:
                break

            for room in rooms:
                tmp = dict()
                tmp['pid'] = platform['id']
                tmp['name'] = room["anchor_nick"]
                tmp['rid'] = room['room_id']
                tmp['title'] = room['channel_name']
                tmp['avatar'] = room['headimg']
                tmp['url'] = self.get_address(room['room_id'])

                ret.append(tmp)

        return ret

    @staticmethod
    def get_avatar():
        pass

    def get_address(self, rid) -> str:
        sign = self.sign_params(self.room_info_params)
        params = self.room_info_params.copy()
        params['roomid'] = rid
        params['signature'] = sign
        resp = requests.get(url=self.room_info_url,
                            params=params,
                            headers=self.headers)
        return resp.json()['data']['roominfo']['v_pull_url']

    @staticmethod
    def sign_params(params):
        items = params.items()
        items = sorted(items)
        key = ""
        for (_key, _val) in items:
            key += str(_val)
        key += "ZGkoRZ9DxFwsAnXvuLappDMQL4XnPSKY"
        key = key.lower()
        m = hashlib.md5()
        m.update(key.encode("utf8"))
        return m.hexdigest()

    def xx_crawl(self):
        pass


def main():
    router = Router()
    ls = router.get_list()
    print(ls)
    print(len(ls))


if __name__ == '__main__':
    main()
