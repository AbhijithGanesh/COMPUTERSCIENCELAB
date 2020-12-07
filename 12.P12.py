# phishing mail


def find_email(data):
    for i in data:
        i.split()
    data.sort() 

    empty_dict = {}
    for i in data:
        empty_dict[str(i)] = data.count(i)
    
    _keys = list(empty_dict.keys())
    _values = list(empty_dict.values())
    _copy = _values.copy()
    _values.sort(reverse=True)
    
    mostoccuringwords = []

    for i in range(5):
        mostoccuringwords.append(_keys[_copy.index(_values[i])])
    
    print(mostoccuringwords)










'''f = open(file)
    _list = f.readlines()
    phishing_words = ['Suspicious', 'Help Us']
    for i in _list:
        if phishing_words in i:
            print("THIS MAIL LOOKS FISHY AND PLEASE DELETE THIS MAIL AND BLOCK THE ACCOUNT")'''

    