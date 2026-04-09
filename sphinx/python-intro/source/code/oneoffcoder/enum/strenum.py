from enum import StrEnum


class Role(StrEnum):
    ADMIN = 'admin'
    EDITOR = 'editor'
    VIEWER = 'viewer'


role = Role.ADMIN
print(role)
print(role == 'admin')
