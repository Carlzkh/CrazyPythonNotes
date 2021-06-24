from urllib.parse import *
# 解析 URL 字符串
result = urlparse('http://www.crazyit.org:80/index.php;yeeku?name=fkit&id=1#frag')
print(result)
# 通过属性名和索引来获取 URL 的各部分
print('scheme :', result.scheme, result[0])
print('主机和端口:', result.netloc, result[1])
print('主机 ：', result.hostname)
print('端口 ：', result.port)
print('资源路径 ：', result.path, result[2])
print('参数 ：', result.params, result[3])
print('查询字符串 ：', result.query, result[4])
print('fragment ：', result.fragment, result[5])
print(result .geturl())

# 解析查询字符串 返回 dict
result = parse_qs('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
# 解析查询字符串 返回 list
result = parse_qsl('name=fkit&name=%E7%96%AF%E7%8B%82java&age=12')
print(result)
# 将列表形式的请求参数恢复成字符审
print(urlencode(result))

# 被拼接的 URL 以斜线开头
result = urljoin('http://www.crazyit.org/users/login.html', 'help.html')
print(result)
result = urljoin('http://www.crazyit.org/users/login.html', 'book/list.html')
print(result)
# 被拼接的 URL 以斜线（代表根路径 path ）开头
result = urljoin('http://www.crazyit.org/users/login.html',  '/help.html')
print(result)
# 被拼接的 UR 以双斜线（ 表绝对路径 path ）开头
result = urljoin('http://www.crazyit.org/users/login.html',  '//help.html')
print(result)
