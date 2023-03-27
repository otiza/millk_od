from odoo import fields, models

class BacaLait(models.Model):
    _name = "bac.lait"
    _description = 'bac a lait'

    reference = fields.Char()
    capacite = fields.Float()
    unite_production_id = fields.Many2one('milk.unite')
    producer_id = fields.Many2one('milk.producer',related='unite_production_id.producer_id')

    def name_get(self):
        res = []
        for record in self:
            name = str(record.reference)
            res.append((record.id, name))
        return res