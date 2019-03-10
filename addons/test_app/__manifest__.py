# -*- coding: utf-8 -*-
{
    'name': "Test Module",

    'summary': """測試建立一個odoo module""",

    'description': """
        Test module for managing models:
            - under construction
    """,

    'author': "Charlie Lee",
    'website': "https://example.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': [
        'base'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates/first.xml',
        'views/menu.xml',
        # 'views/first_view.xml',
        'views/session_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo.xml',
    ],
    'application': True,
}