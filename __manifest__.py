# -*- coding: utf-8 -*-
{
    'name': "Generar reportes",

    'summary': """
        """,

    'description': """
        Generador de reportes personalizados.
    """,

    'author': "Quadit",
    'website': "https://www.quadit.mx/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Desarrollo',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/report_catalog.xml',
        'reports/report.xml',
        'views/assests.xml',
        #'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}