# -*- coding: utf-8 -*-

{
    'name': "Task manager",
    'version': '1.0',
    'depends': ['base','mail','contacts'],
    'author': "Ta So",
    'category': 'Managers',
    'summary': 'Custom module - Task manager',
    'description': """
    Task manager description
    """,
    # data files always loaded at installation
    'data': [
        'views/task_view.xml',
        'views/task_manager_view.xml',
        'security/ir.model.access.csv',
        'report/tasks_report_template.xml',
        'report/tasks_report.xml',
        'data/ir_cron_data.xml',
        'data/mail_template_data.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        #'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'autoinstall': False,
}
