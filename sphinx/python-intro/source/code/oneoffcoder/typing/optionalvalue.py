def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return 'Jane'
    return None


print(find_user(1))
print(find_user(2))
