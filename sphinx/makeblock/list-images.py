import pathlib
from collections import defaultdict, namedtuple

Image = namedtuple('Image', 'alias path')

image_dir = './source/_static/images/mbot'
files = pathlib.Path(image_dir).glob('**/*.png')
d = defaultdict(list)

for f in files:
    parts = f.parts
    if parts[-1].startswith('main'):
        continue
    parts = parts[1:]
    section = parts[3]
    p = '/'.join(parts)
    a = parts[-1].replace('.png', '')
    s = f'.. |{a}| image:: {p}'
    t = Image(a, s)
    d[section].append(t)

d = [(section, figures) for section, figures in d.items()]
d = sorted(d, key=lambda tup: tup[0])

for section, figures in d:
    figs = sorted(figures, key=lambda image: image.path)
    s = section[3:len(section)]
    print(s.title())
    print('-'*len(s))
    print()
    
    for _, path in figs:
        print(path)

    print()
    print(f'.. csv-table:: {s.title()}')
    print('   :header: Block, Effect')
    print()
    
    for alias, _ in figs:
        print(f'   |{alias}|, ')


    print()
