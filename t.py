
d = "dict_1"
name = 'John'
dob = 10152020


def add_to_dict(name, dob, variable_name):
    globals()[variable_name] = {name:dob}



add_to_dict(name, dob, d)
print(dict_1)

b = 1
a = [b, 'what']
a[b]