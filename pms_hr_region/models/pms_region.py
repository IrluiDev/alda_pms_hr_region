from odoo import models, fields, api

class Region(models.Model):
    _name = 'pms.property.region'
    _description = 'PMS Property Region'

    cod_region = fields.Char(string='Region Code', compute='_compute_region_code', store=True)
    #employee_id = fields.Many2one('hr.employee', string='Regional Manager', domain="[('job_id', '=', position1_id)]")
    employee_id = fields.Many2one('hr.employee', string='Regional Manager', store=True)
    #company_ids = fields.Many2many('res.company', string='Companies')
    property_region_ids = fields.One2many('pms.property.region.assignment', 'region_id', string='Properties', store=True)

    @api.depends('employee_id')
    def _compute_region_code(self):
        for region in self:
            # Base del código de región
            base_code = 'ALDA-RGM'
            
            # Obtener el número total de regiones para calcular el valor incremental
            total_regions = self.env['pms.property.region'].search_count([])
            incremental_value = total_regions
            
            # Obtener el ID del empleado y el ID de la primera propiedad (si existen)
            employee_id = region.employee_id.id or ''
            
            # Concatenar los IDs y formatear el código de región
            region.cod_region = '{}-{:02d}-{}'.format(base_code, incremental_value, employee_id,)

