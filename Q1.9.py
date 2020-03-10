d = [  # a list of dictionaries
    {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
]
for dic in d:
    phone = dic.get('phone')
    if(phone[len(phone)-1] == '8'):
        print(dic)
for dic in d:
    email = dic.get('email')
    if(email == ''):
        print(dic)
