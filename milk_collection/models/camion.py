from odoo import models, fields

class Camion(models.Model):
    _name="milk.camion"
    _description= "milk camion model"

    camion_id= fields.Many2one(
        "fleet.vehicle",required=True
    )
    license = fields.Char(
        related='camion_id.license_plate',
        store=True,
        readonly=False
    )
    kilometrage = fields.Float(related='camion_id.odometer',
                    store=True,
                    readonly=False)
    capacite = fields.Float(string="capacite (L)")
    
    _sql_constraints = [
        ('plate_unique','unique(license)','immatricule already exists')
    ]  
    def name_get(self):
        res = []
        for record in self:
            name = str(record.license)
            res.append((record.id, name))
        return res