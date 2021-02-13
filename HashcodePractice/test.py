from collections import OrderedDict
a = {'1': (1,3), '2': (6,2),'3':(10,2)}
def sortindex(index):
    def key_func(item):
        key, value = item
        return (value[index], key)
    return key_func


sorted_list = sorted(a.items(), key=sortindex(0))
sorted_list.pop(0)
print(sorted_list)