# -*- coding: utf-8 -*-
{
    'name': 'Sequence Number & Product Images on Sale Order, Delivery Order & Invoice Report',
    'version': '1.0',
    'category': 'Sales',
    'summary': '''
            Show Product Images and Sequence Number in Sale Order, Delivery Order and Invoice Report.
        ''',
    'author': 'HK',
    'license': "OPL-1",
    'support': 'prince.odoo.up@gmail.com',
    'depends': [
        'sale_stock',
    ],
    'data': [
        'views/sale_views.xml',
        'views/account_invoice_view.xml',
        'views/stock_picking_views.xml',
        'report/sale_report_templates.xml',
        'report/report_invoice.xml',
        'report/report_stockpicking_operations.xml',
        'report/report_deliveryslip.xml'
    ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'auto_install': False,
    'installable': True,
    'application': True
}