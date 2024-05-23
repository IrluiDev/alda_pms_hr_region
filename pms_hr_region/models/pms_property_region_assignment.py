from odoo import models, fields

class PMSPropertyRegionAssignment(models.Model):
    _name = 'pms.property.region.assignment'
    _description = 'PMS Property Region Assignment'

    region_id = fields.Many2one('pms.property.region', string='Region', required=True)
    pms_property_id = fields.Many2one('pms.property', string='Property', required=True)
    
    position1_id = fields.Many2one('hr.job', string='Position 1')
    employee1_id = fields.Many2one('hr.employee', string='Employee 1', domain="[('job_id', '=', position1_id)]")

    position2_id = fields.Many2one('hr.job', string='Position 2')
    employee2_id = fields.Many2one('hr.employee', string='Employee 2', domain="[('job_id', '=', position2_id)]")

    position3_id = fields.Many2one('hr.job', string='Position 3')
    employee3_id = fields.Many2one('hr.employee', string='Employee 3', domain="[('job_id', '=', position3_id)]")

    position4_id = fields.Many2one('hr.job', string='Position 4')
    employee4_id = fields.Many2one('hr.employee', string='Employee 4', domain="[('job_id', '=', position4_id)]")

    position5_id = fields.Many2one('hr.job', string='Position 5')
    employee5_id = fields.Many2one('hr.employee', string='Employee 5', domain="[('job_id', '=', position5_id)]")
