# -*- coding: utf-8 -*-
{
    'name': "cirus_inventory",

    'summary': """
        Control Center configurations.""",

    'description': """
        This module extends the functionality of inventory application by adding the linking with the Control Center.
    """,

    'author': "Glossa Systems",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}