name = {'first_name': 'John', 'last_name': 'Doe'}
address = {
    'address': '123 Main Street',
    'city': 'Washington',
    'state': 'DC',
    'zip': 20050
}

person = {**name, **address}
