import sys
import requests

print(sys.version)
print(sys.executable)


i = 2
print('This is i: {0:06d} or {0:06.2f}'.format(i))

r = requests.get("http://xaknak.hrasko.com")
print(r.status_code)
