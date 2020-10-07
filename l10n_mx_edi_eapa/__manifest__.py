# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'EDI Complements to Plastic Arts & Antiques and Payment in kind',
    'version': '12.0.1.0.0',
    "author": "Vauxoo",
    "license": "LGPL-3",
    'category': 'Hidden',
    'summary': 'Mexican Localization for EDI documents',
    'depends': [
        'l10n_mx_edi',
    ],
    'data': [
        "data/plastic_arts_antiques.xml",
        "data/payment_in_kind.xml",
        "views/product_view.xml",
    ],
    'installable': True,
    'auto_install': False,
}
