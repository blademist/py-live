import requests
import json

platform = {
    'name': '七鼎直播',
    'id': '19',
    'img': "http://img3.anzhi.com/data3/icon/201707/28/tv.qiding.qidinglive_43652400_48.png"
}


class Router(object):
    def __init__(self):
        self.url = "http://nlb163.qiding.tv:9999/qiDingLive2.1/videoRoom/findConditionOnlineRoomList"

        self.data = {"currentPage": 1, "pageSize": 10}

        self.headers = {
            "Accept": "application/json",
            "Content-type": "application/json",
            "Host": "nlb163.qiding.tv:9999",
            "sign": "1501689849564_65982445757597005919247978179416",
        }
        self.cookies = {
            "JSESSIONID": "DC773B60266B4AD2E90217D43E43ED57",
            "JSESSIONID6": "72025669220"
        }

    def get_list(self) -> list:
        page = 1
        ret = []

        while True:
            self.data['currentPage'] = page
            page += 1
            resp = requests.get(url=self.url,
                                data=json.dumps(self.data),
                                headers=self.headers,
                                cookies=self.cookies)
            resp = resp.json()
            status = resp['Status']
            if status == 0:
                break

            rooms = resp['Data']
            for room in rooms:
                tmp = dict()
                tmp['pid'] = platform['id']
                tmp['name'] = room["zlrlTheCorenPetName"]
                tmp['rid'] = room['zlraRoomId']
                tmp['title'] = room['zlrlPetName']
                tmp['avatar'] = self.get_avatar(room['zlrlTheCorenHeadImg'])
                tmp['url'] = room['downVideoStreamRTMPApril']

                ret.append(tmp)

        return ret

    @staticmethod
    def get_avatar(zlrlTheCorenHeadImg):
        return "http://image.qiding.tv/{}".format(zlrlTheCorenHeadImg)

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
