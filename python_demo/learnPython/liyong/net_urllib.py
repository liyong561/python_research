import urllib.request
""" import模块不行。  """
f = urllib.request.urlopen('http://www.httpbin.org/')
"""只有read就不会解析html源文件"""
"""print(f.read().decode("utf-8"))"""

