import pathlib
from collections import defaultdict, namedtuple

Image = namedtuple('Image', 'alias path')

image_dir = './source/_static/images/codey'
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

for section, figures in d.items():
    figs = sorted(figures, key=lambda image: image.path)
    print(section.title())
    print('-'*len(section))
    print()
    
    for _, path in figs:
        print(path)

    print()
    print(f'.. csv-table:: {section.title()}')
    print('   :header: Block, Effect')
    print()
    
    for alias, _ in figs:
        print(f'   |{alias}|, ')


    print()
