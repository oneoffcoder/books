def normalize_name(first_name, last_name):
    """
    Build a normalized full name.

    Args:
        first_name: The first name to normalize.
        last_name: The last name to normalize.

    Returns:
        The normalized full name in title case.
    """
    return f'{first_name.strip().title()} {last_name.strip().title()}'


print(normalize_name('  jane', 'DOE  '))
