def jazz_potato(thang):
    thang2 = []
    thang3 = thang.split()
    for jazz in thang3:
        if jazz in ['fuck','shit', 'fucking','balls','damn', 'fucked', 'shitted','bitch','ass']:
            thang2.append('potato')

        else:
            thang2.append(jazz)
    return ' '.join(thang2)


print(space_jam('i hate this fucking shit'))