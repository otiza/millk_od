from odoo import models, fields, api

class MilkProduce(models.Model):
    _name = "milk.producer"
    _description = "milk producer model"


    
    partner_id = fields.Many2one(
    "res.partner",required=True)
    unite_ids = fields.One2many('milk.unite','producer_id',string="unite de prodcution")
    bacalait_ids = fields.Many2many('bac.lait')
    name = fields.Char(
        related="partner_id.name",
        string="Name",
        store=True,
        readonly=False
        
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
        readonly=False
        
    )
    street = fields.Char(
         related="partner_id.street",
        string="street",
        store=True,
        readonly=False
        
    )
    street2 = fields.Char(
         related="partner_id.street2",
        string="email",
        store=True,
        readonly=False
        
    )
    zip = fields.Char(
         related="partner_id.zip",
        string="email",
        store=True,
        readonly=False
        
    )
    city = fields.Char(
         related="partner_id.city",
        string="email",
        store=True,
        readonly=False
        
    )
    latitude = fields.Float(
         related="partner_id.partner_latitude",
        string="email",
        store=True,
        readonly=False
    )

    
    longitude = fields.Float(
         related="partner_id.partner_longitude",
        string="email",
        store=True,
        readonly=False
    )
    
    is_company = fields.Boolean(string="company")
    cheptel_ids = fields.One2many("milk.cow", "milk_producer_id")
    


