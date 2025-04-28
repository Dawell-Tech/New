{
    'name': 'Sum Calculator',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Simple Sum Calculator for Two Numbers',
    'description': """
        This module provides a simple calculator to add two numbers together.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/sum_calculator_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
