from odoo import fields, models, api


class ProductionUnite(models.Model):
    _name = 'milk.unite'
    _description = 'Milk production unite'
    stock_location_id = fields.Many2one("stock.location")
    name = fields.Char()
    producer_id = fields.Many2one('milk.producer')
    bacalait_ids = fields.One2many('bac.lait','unite_production_id',string="bac a laits")
    latitude = fields.Float(       
    )
    longitude = fields.Float(
    )
    @api.model
    def create(self, vals):
        value = {
            'name' : vals['name'],
            'usage' : 'production',
        }
        
        stock_location = self.env['stock.location'].create(value)
        vals['stock_location_id'] = stock_location.id
        ret = super().create(vals)
        return ret