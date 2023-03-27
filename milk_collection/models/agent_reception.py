from odoo import models, fields

class Milkagent(models.Model):
    _name = "milk.agent"
    _description = "milk collection agent model"


    
    partner_id = fields.Many2one(
    "res.partner",required=True)
    
    name = fields.Char(
        related="partner_id.name",
        string="Name",
        store=True,
        readonly=False,
    )
    phone = fields.Char(
         related="partner_id.phone",
        string="Phone",
        store=True,
        readonly=False
    )
    email = fields.Char(
         related="partner_id.email",
        string="email",
        store=True,
        readonly=False,
    )