from collections.abc import Mapping
import textwrap
import inspect

class MailingLabel(Mapping):
    def __init__(self, **kwargs):
        self.data = kwargs

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        s = f"""
        {self.data['fname']} {self.data['lname']}
        {self.data['street']}
        {self.data['city']}, {self.data['state']} {self.data['zip']}
        """
        s = inspect.cleandoc(s)
        return s

label = MailingLabel(**{
    'fname': 'One-Off',
    'lname': 'Coder',
    'street': '7526 Old Linton Hall Road',
    'city': 'Gainesville',
    'state': 'VA',
    'zip': '20155'
})

print(label)
print('-'*5)
for k, v in label.items():
    print(f'{k}: {v}')