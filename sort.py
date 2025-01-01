my_dict={'b': 2,'a': 1,'d': 4,'e': 3}
asc_dict = dict(sorted(my_dict.items()))
des_dict = dict(sorted(my_dict.items(),reverse=True))
print("original Dictionary:", my_dict)
print("Ascending order:", asc_dict)
print("Descending order:", des_dict)

