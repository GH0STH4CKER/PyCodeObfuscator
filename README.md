### Obfuscate your python source code to hide it from everyone

Sample obfuscated file :
```
import gzip,zlib,marshal,base64
exec(marshal.loads(gzip.decompress(zlib.decompress(base64.b64decode(b'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')))))
```

If somebody try change exec to print, this is what prints
```

<code object <module> at 0x15034df59df0, file "Nice Try", line 1>
```

Star my Repo [🌟]
