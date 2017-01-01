def cheeseshop(kind, *arguments, **keywords):
    print(kind)
    print(arguments) #arguments before there's a keyword argument
    print(keywords)

"""
hi
('every', 'one', 'how', 'are', 'you')
{}
"""
cheeseshop('hi', 'every', 'one', 'how', 'are', 'you')


"""
hi
('all', 'how')
{'param1': 'every', 'param2': 'one', 'param3': 'how', 'param5': 'you', 'param4': 'are'}
"""
cheeseshop('hi', 'all', 'how', param1='every', param2='one', param3='how', param4='are', param5='you')