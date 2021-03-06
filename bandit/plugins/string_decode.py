import bandit
import re
import ast
from bandit.core import test_properties as test

@test.checks('Str')
@test.test_id('B502')
def string_decode(context):
    if isinstance(context.node._bandit_parent, ast.Attribute):
        if context.node._bandit_parent.attr == 'decode':
            return bandit.Issue(
            severity=bandit.MEDIUM,
            confidence=bandit.MEDIUM,
            text="string_decode"
        )
