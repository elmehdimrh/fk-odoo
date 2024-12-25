{
    'name': 'Fokal External Layout',
    'version': '1.0',
    'category': 'Reports',
    'author': 'Mehdi MARHOUM',
    'depends': ['base'],  # 'report' is needed for reports
    'data': [
        'views/fk_external_layout.xml',  # The custom external layout XML file
        'data/report_layout.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'fk_custom_layout/static/src/scss/layout_fokal.scss',
        ]
    },
    'installable': True,
}
