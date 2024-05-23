{
    'name': 'Custom Alda pms_propertyes Regions Management',
    'version': '14.0.1.0.0',
    'category': 'HPMS/HR',
    'summary': 'Manage pms_property regions and assign job positions to properties.',
    'author': 'Irlui Ramirez,José Luis Algara,Odoo Community Association (OCA)',
    'depends': [
        'base',
        'hr',
        'pms',
    ],
    'data': [
        'views/region_views.xml',
        'views/pms_property_region_assignment_views.xml',
    ],
    'installable': True,
    'application': False,
}
