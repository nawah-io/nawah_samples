from nawah.base_module import BaseModule
from nawah.classes import ATTR, PERM

class Blog(BaseModule):
    collection = 'blogs'
    attrs = {
        'title': ATTR.LOCALE(),
        'content': ATTR.LOCALE(),
        'create_time': ATTR.DATETIME(),
    }
    methods = {
        'read': {
            'permissions': [PERM(privilege='*')],
        },
        'create': {
            'permissions': [PERM(privilege='create')],
        },
        'update': {
            'permissions': [PERM(privilege='update')],
        },
        'delete': {
            'permissions': [PERM(privilege='delete')],
        },
    }