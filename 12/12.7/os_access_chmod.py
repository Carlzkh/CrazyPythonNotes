import os
import stat

# 判断当前目录的权限
ret = os.access('.', os.F_OK | os.R_OK | os.W_OK | os.X_OK)
print("os.F_OK|os.R_OK|os.W_OK|os.X_OK - 返回值:", ret)
# 判断os.access_test.py文件的权限
ret = os.access('os_access_chmod.py', os.F_OK | os.R_OK | os.W_OK)
print("os.F_OK|os.R_OK|os.W_OK - 返回值:", ret)


# 将os.chmod_test.py文件改为只读
os.chmod('os_access_chmod.py', stat.S_IREAD)
# 判断是否可写
ret = os.access('os_access_chmod.py', os.W_OK)
print("os.W_OK - 返回值:", ret)
