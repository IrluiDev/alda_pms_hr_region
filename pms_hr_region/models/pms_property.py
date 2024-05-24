# Copyright 2024 OsoTranquilo
# Copyright 2024 Irlui Ramírez
# From Consultores Hoteleros Integrales (ALDA Hotels) - 2024
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PmsPropertyRegional(models.Model):
    _inherit = "pms.property"

    region_id = fields.Many2one(
        comodel_name="pms.property.region.assignment",
        string="Region",
        help="The region associated with this property",
    )