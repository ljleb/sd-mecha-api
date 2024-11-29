class UserGroup:
    ADMIN = 'Admin'
    USER = 'User'


ALL_GROUPS = [group for key, group in UserGroup.__dict__.items() if isinstance(key, str) and not key.startswith('__')]
