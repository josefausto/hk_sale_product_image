# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Picking(models.Model):
    _inherit = "stock.picking"
    
    show_sequence_number = fields.Boolean(string='Show Sequence Number in Picking Report?', default=False)
    show_product_image = fields.Boolean(string='Show Product Image in Picking Report?', default=False)
    product_image_size = fields.Selection([
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
       	], string='Product Image Size', default="medium")