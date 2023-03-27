from odoo import models, fields, api

class BacInterne(models.Model):
    _name ="bac.interne"
    _description = "milk bac a lait interne"

    ref = fields.Char()
    stock_id = fields.Many2one("stock.location")
    capacite = fields.Float()
    usage = fields.Float()
    available = fields.Float(compute="_compute_avail")
    centre_id = fields.Many2one("collect.center")

    @api.model
    def create(self, vals_list):
        value = {
            'name' : vals_list['ref'],
            'usage' : 'internal'
        }
        stock_id = self.env['stock.location'].create(value)
        vals_list['stock_id'] = stock_id.id
        return super().create(vals_list)
    @api.depends("usage","capacite")
    def _compute_avail(self):
        for rec in self:
            rec.available = rec.capacite - rec.usage
    
    def name_get(self):
        res = []
        for record in self:
            name = str(record.ref)
            res.append((record.id, name))
        return res
    
    def store(self, quantity):
        if self.available >= quantity:
            self.usage += quantity
            return True
        else:
            return False
    def unload(self, quantiy):
        if self.usage >= quantiy:
            self.usage -= quantiy
            return True
        else:
            return False