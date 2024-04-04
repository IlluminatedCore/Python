dict = {'name':'manideep', 'town':'miryalaguda' }

dict.update({'living':'USA'})

dict.update({'likes':'Janasena'})


#dict.pop('living')

print(list(dict.items()))

dict['name'] = 'madhuri'

print(list(dict.items()))


set = {1, 2, 3, 4, 5, 6}

set1 = {5, 6, 7, 8, 9}

newset = set.union(set1)

print(newset)

newset = set.intersection(set1)

print(newset)