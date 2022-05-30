import list

l = list.UnorderedList()
l.seeFullList()

l.add(13)
l.seeFullList()

l.add(17)
l.seeFullList()

l.add(15)
l.seeFullList()

print(l.size())
print(l.index(15))
print(l.search(15))

print("-" * 20)

l.insert(0,499)
l.seeFullList()

l.insert(1, 500)
l.add(500)
l.seeFullList()

l.insert(3, 600)
l.add(600)
l.seeFullList()

l.insert(5,800)
l.add(501)
l.seeFullList()

print(l.size())
print(l.index(13))
print(l.search(13))
