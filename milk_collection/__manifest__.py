# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'milk_collection',
    'depends': [
        'base','fleet','stock'
    ],
    'application': True,
    'data':[
        'security/ir.model.access.csv',
        
        'views/milk_producer_views.xml',
        
        'views/milk_tournee_views.xml',
        'views/milk_reception_views.xml',
        'views/collect_center_views.xml',
        'views/milk_collect_views.xml',
        'views/milk_chauffeur_views.xml',
        'views/milk_collection_agent_views.xml',
        'views/milk_camion_views.xml',
        'views/milk_vache_views.xml',
        'views/milk_production_unite_views.xml',
        'views/milk_producer_menus.xml',
    ]
}