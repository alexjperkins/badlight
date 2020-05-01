# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_get_user_query 1'] = {
    'data': {
        'user': {
            'email': 'test',
            'name': 'test test'
        }
    }
}

snapshots['test_get_user_query_bad_query 1'] = {
    'data': {
        'user': None
    }
}

snapshots['test_get_user_query_user_not_found 1'] = {
    'data': {
        'user': None
    }
}

snapshots['test_create_user_mutation 1'] = {
    'data': {
        'createUser': {
            'email': 'test.test@email.com',
            'name': 'test test'
        }
    }
}
