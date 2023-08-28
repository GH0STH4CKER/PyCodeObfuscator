# Coded by GH0STH4CKER
# If this is useful, please Star 🌟 my repo https://github.com/GH0STH4CKER/PyCodeObfuscator/

import gzip,zlib,marshal,base64

pyfile = input('Python file [C:/User/file.py]: ')

with open(pyfile,'r') as file:
    pycode = file.read()

Cmp = base64.b64encode(zlib.compress(gzip.compress(marshal.dumps(compile(pycode, "Nice Try", "exec"))), level=zlib.Z_BEST_COMPRESSION))

f_cont = f"""import gzip,zlib,marshal,base64
exec(marshal.loads(gzip.decompress(zlib.decompress(base64.b64decode({Cmp})))))"""

with open(pyfile.split('/')[-1][:-3]+'obfuscated'+'.py','w') as file:
    file.write(f_cont)
