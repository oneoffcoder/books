import os

image_dir = 'sensing'
files = os.listdir(f'./source/_static/images/{image_dir}')
for f in files:
    s = f'.. figure:: _static/images/{image_dir}/{f}'
    print(s)