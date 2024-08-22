person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = set(person['skills'])
    if skills == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif skills >= {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif skills >= {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('unknown title')