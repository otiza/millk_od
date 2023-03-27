from odoo import models,fields, api

class Tournee(models.Model):
    _name="milk.tournee"
    _description="milk tournee model"

    number = fields.Integer(required=True)
    chauffeur_id = fields.Many2one("milk.chauffeur")
    agent_id = fields.Many2one("milk.agent")
    camion_id= fields.Many2one("milk.camion")
    trajet_ids = fields.Many2many("milk.unite")
    
    _sql_constraints = [
        ('number_unique','unique(number)','number already exists')
    ]  
    


    def name_get(self):
        res = []
        for record in self:
            name = str(record.number)
            res.append((record.id, name))
        return res