from odoo import models, fields, api

class CollecteCenter(models.Model):
    _name = "collect.center"
    _description = "milk collection center"

    stock_id = fields.Many2one("stock.location")
    name = fields.Char()
    bac_alait_ids = fields.One2many("bac.interne","centre_id")
    @api.model
    def create(self, vals):
        print("h",vals['name'])
        value = {
            'name' :vals['name'],
            'usage': 'transit' 
        }
        stock_id = self.env['stock.location'].create(value)
        vals['stock_id'] = stock_id.id
        return super().create(vals)