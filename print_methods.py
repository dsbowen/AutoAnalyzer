import pandas as pd

df = pd.Series()
methods = dir(df)
for m in methods:
    l = '    def '+m+'(self, *args, **kwargs):\n'
    l += '        print("'+m+'")\n'
    l += "        return self._overload('"+m+"', *args, **kwargs)\n"
    print(l)