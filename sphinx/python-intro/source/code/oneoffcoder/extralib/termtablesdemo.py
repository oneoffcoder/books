import termtables as tt

header = ['first_name', 'last_name', 'age', 'height', 'is_cool']
data = [
    ['john', 'doe', 23, 5.5, True],
    ['jack', 'johnson', 34, 6.2, False]
]

tt.print(
    data,
    header=header,
    style=tt.styles.markdown,
    padding=(0, 1),
    alignment="lcrlc"
)