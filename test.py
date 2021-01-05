a = {"单位": "1"}
print(a["单位"])
import platform
import os
environ_list = os.environ
print(environ_list)
for i in environ_list:
    print(i + ":" + environ_list[i])