{
    'name': 'Production Planning',
    'version': '1.0',
    'depends': ['mrp', 'base', 'web','mail'],
    'author': 'Your Name',
    'category': 'Manufacturing',
    'description': 'Adds Production Planning under Planning with PDF report',
    'data': [
        'security/ir.model.access.csv',
        'views/production_planning_views.xml',
        'data/production_planning_sequence.xml',
        'reports/planning_report.xml',
        'reports/planning_template.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
}
