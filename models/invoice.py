from odoo import models,fields

class Invoice(models.Model):
    _inherit = "account.move"

    country_name = fields.Char(string="country Name")




