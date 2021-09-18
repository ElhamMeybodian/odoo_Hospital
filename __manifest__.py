{
    'name': "Hospital Management",
    'version': '1.0',
    # 'category': 'Extra Tools',
    'depends': ['base', 'mail', 'sale'],
    'summary': 'Module for manging the Hospitals',
    'author': "sample",
    # 'category': 'Extra Tools',
    'sequence': '10',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizards/create_appointment.xml',
        'data/sequence.xml',
        'data/cron.xml',
        'data/mail_template.xml',
        'views/patient.xml',
        'views/lab.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'data/data.xml',

        # insert file report
        'reports/report.xml',
        'reports/patient_card.xml',
        'reports/sale_report_inherit.xml',
        # 'views/mymodule_view.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
