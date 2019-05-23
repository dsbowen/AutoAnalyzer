import pandas as pd

df = pd.DataFrame()
methods = dir(df)
methods = [m for m in methods if m[0:2]=='__']
for m in methods:
    l = '    def '+m+'(self, *args, **kwargs):\n'
    l += '        print("'+m+'")\n'
    l += "        return self._overload('"+m+"', *args, **kwargs)\n"
    print(l)