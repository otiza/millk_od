from odoo import models,fields

class  ProductTemplate(models.Model):
    _inherit = "product.template"

    is_collectable = fields.Boolean(default=False)