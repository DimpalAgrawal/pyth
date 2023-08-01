# The original list : ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
# List after removal of suffix elements : ['gfg', 'xit', 'is']

list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
suffix = 'x'

for i in list[:]:
    if i.endswith(suffix):
        list.remove(i)
print(str(list))