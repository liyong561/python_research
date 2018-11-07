import requests

res = requests.get("https://www.baidu.com/")
print(res.status_code)  # 200，说明可以访问到豆瓣首页
# print(res.text)  返回网页代码

res1 = requests.get("https://www.bouban.com/search", params={'q': 'python', 'cat': '1001'})
res2 = requests.post("https://www.bouban.com/search", params={'q': 'python', 'cat': '1001'})

print(res2.content)
