import pandas as pd

methods = dir(pd.DataFrame())

for m in methods:
    if m in ['__setattr__', '__getattr__', '__getattribute__', '__init__', '__new__']:
        break
    l = '    def '+m+'(self, *args, **kwargs):\n'
    l += '        # print("'+m+'")\n'
    l += "        return self._overload('"+m+"', *args, **kwargs)\n"
    print(l)