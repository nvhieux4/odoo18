{
    'name': 'Onex Bot Script',
    'version': '1.0',
    'category': 'Tools',
    'description': 'Module to execute scripts with API key.',
    'author': 'Your Company',
    'depends': ['base', 'website'],
    'data': [
        'views/bot_script_config_views.xml',
        'views/bot_script_template.xml',
        'data/ir.model.access.csv',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
