from odoo import models, fields,api
from datetime import datetime
from odoo.exceptions import UserError, ValidationError
class MilkReception(models.Model):
    _name="milk.reception"
    _description= "milk reception model"

    quantite = fields.Float()
    pesage = fields.Float()
    date_reception = fields.Datetime(string="date de  reception", default=datetime.now())
    tournee_id = fields.Many2one("milk.tournee",required=True)
    destination = fields.Many2one("bac.interne")
    collection_ids = fields.Many2many('milk.collection',domain="[('is_received', '=',False)]")   
    Mg = fields.Float()
    Alc = fields.Float()
    Rdl = fields.Float()

    @api.model
    def create(self, vals):
        reception =  super().create(vals)
        if reception:
            if reception.destination.store(reception.quantite) == False:
                raise ValidationError("bac a lait est plein")
            for item in reception.collection_ids:
                print("hello123")
                item.receive()
        return reception