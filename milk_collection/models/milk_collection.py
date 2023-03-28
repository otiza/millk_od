from odoo import models, fields,  api
from datetime import datetime
class MilkCollection(models.Model):
    _name = 'milk.collection'
    _description = 'Milk Collection'

    producer_id = fields.Many2one('milk.producer', string='Producer')
    quantity = fields.Float(string='Quantity', compute="_compute_quantity")
    tournee_id = fields.Many2one('milk.tournee', string='Tournee')
    product_id = fields.Many2one(
        'product.product', 'Product',
        required=True)
    
    unite_id = fields.Many2one(
        'milk.unite', 'Source Location',
        domain="[('producer_id', '=', producer_id)]")
    location_id = fields.Many2one('stock.location',related="unite_id.stock_location_id")  
    centre_id = fields.Many2one("collect.center",'Destination Location')
    location_dest_id = fields.Many2one(
        'stock.location', related='centre_id.stock_id')
    date_collection = fields.Datetime(string="date de  collection", default=datetime.now(),readonly=True)
    is_received = fields.Boolean(default= False)
    collect_line_ids = fields.One2many('collection.line','milk_collection_id')
    @api.depends("collect_line_ids")
    def _compute_quantity(self):
          for rec in self:
                total = 0
                for line in rec.collect_line_ids:
                      total = total + line.quantity
                rec.quantity = total
    @api.model
    def create(self, vals):
           
            collection = super(MilkCollection, self).create(vals)
            
            
            if collection:
                name = 'Milk Collection'
                value = {
                    'name': 'test',
                    'product_id': vals['product_id'],
                    'product_uom_qty': collection.quantity,
                    'location_id': collection.location_id.id,
                    'location_dest_id':collection.location_dest_id.id,
                    'state': 'draft',
                    'picking_type_id': self.env.ref('stock.picking_type_in').id,
                    'product_uom': 	11
                }
                
                stock_move = self.env['stock.move'].create(value)
                stock_move._action_confirm()
                stock_move._action_assign()
                stock_move._action_done()

                
            
           
                
            return collection
    
    def receive(self):
          print("hey143")
          self.is_received = True