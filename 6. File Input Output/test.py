member = {
   'person':{
        'musa':'feni',
        'abrar':'laskmipur',
        'sorif':'laskmipur',
        'kamrul':'bogura',
    },
   'meal':{
        'musa':5,
        'abrar':3,
        'sorif':2,
        'kamrul':10,
    },
   'cost':{
        'musa':500,
        'abrar':300,
        'sorif':200,
        'kamrul':1000,
    }
}

sorted_dic = {}

for each in member:
    # print(member[each].keys())
    # print(sorted(member[each].keys()))
    # print(member[each])
    # print(member[each].items())
    # print(sorted(member[each].items()))
    sorted_dic[each]=dict(sorted(member[each].items()))

print(dict(sorted(member.items())))