from odoo import models, fields

class Cow(models.Model):
    _name = "milk.cow"
    _description = "cow"

    code = fields.Char(required=True)
    age = fields.Integer()
    milk_producer_id = fields.Many2one("milk.producer")

    def name_get(self):
        res = []
        for record in self:
            name = str(record.code)
            res.append((record.id, name))
        return res