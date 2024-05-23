from odoo import models, fields

class Region(models.Model):
    _name = 'pms.property.region'
    _description = 'PMS Property Region'

    name = fields.Char(string='Region Name', required=True)
    pms_property_ids = fields.One2many('pms.property.region.assignment', 'region_id', string='Properties')
