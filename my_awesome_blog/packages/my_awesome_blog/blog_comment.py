from nawah.base_module import BaseModule
from nawah.classes import ATTR, PERM


class BlogComment(BaseModule):
    collection = 'blogs_comments'
    attrs = {
        'blog': ATTR.ID(),
        'name': ATTR.STR(),
        'email': ATTR.EMAIL(),
        'content': ATTR.STR(),
        'status': ATTR.LITERAL(literal=['pending', 'approved', 'deleted']),
        'status_note': ATTR.STR(),
        'create_time': ATTR.DATETIME(),
    }
    methods = {
        'read': {
            'permissions': [PERM(privilege='read'), PERM(privilege='*', query_mod={'status':'approved'})],
            'query_args':[
                {'blog': ATTR.ID()},
                {'status': ATTR.LITERAL(literal=['pending', 'deleted'])}
            ]
        },
        'create': {
            'permissions': [PERM(privilege='create'), PERM(privilege='*', doc_mod={'status':'pending', 'status_note':''})],
        },
        'update': {
            'permissions': [PERM(privilege='update')],
        },
        'delete': {
            'permissions': [PERM(privilege='delete')],
        },
    }
