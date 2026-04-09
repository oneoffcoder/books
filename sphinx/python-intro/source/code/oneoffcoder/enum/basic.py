from enum import Enum


class Status(Enum):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    ARCHIVED = 'archived'


status = Status.DRAFT
print(status)
print(status.value)
