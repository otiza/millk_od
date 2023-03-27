from odoo import models, fields

class CollectionLine(models.Model):
    _name="collection.line"
    _description="milk collection line"

    bac_alait = fields.Many2one('bac.lait')
    quantity = fields.Float()
    milk_collection_id = fields.Many2one('milk.collection')
 