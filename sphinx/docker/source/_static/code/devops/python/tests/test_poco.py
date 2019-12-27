from nose import with_setup

from pydemo.poco import Human

def setup():
    """
    Setup.
    :return: None.
    """
    pass


def teardown():
    """
    Teardown.
    :return: None.
    """
    pass

@with_setup(setup, teardown)
def test_dict():
    """
    Tests conversion to dictionary.
    :return: None.
    """

    human = Human('John', 'Doe', 28, 'M')
    d = human.as_dict()

    assert 'first_name' in d
    assert 'last_name' in d
    assert 'age' in d
    assert 'gender' in d
    
    assert d['first_name'] == 'John'
    assert d['last_name'] == 'Doe'
    assert d['age'] == 28
    assert d['gender'] == 'M'
