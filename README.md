# 直播爬虫

## 基本需求
1. 自动登录
2. 翻页爬
3. 只爬一个排序类型(优先级: 热门(推荐) > 时间, 如果`热门`(`推荐`)的数据量不等于`时间`的数据了, 则爬`时间`)

### 数据格式
```
# 直播平台的dict
{
	name: 平台名
	id: 平台id(第一个平台为11, 后面一直递增)
	img: 平台logo(官网找, 或者AppStore)
}

# 直播的dict
{
	pid: 平台id(第一个平台为11, 后面一直递增)
	name: 用户字
	rid: 房间id
	title: 房间标题或用户名
	avatar: 头像地址(完整链接)
	url: 直播链接(完整链接)
}
```

## Demo
```
import requests

platform = {
	'name' = '',
	'id' = '',
	'img' = ''
}

class Router:
	URL = `base url`
	List = '{}/`uri`'.format(URL)
	...
	
def get_list():
	return []

# maybe need
def get_address() -> str:
	...
	
def xxx_crawl():
	datas = get_list()  # 获取所有直播房间
	... # maybe need get_address
	
	# done

```