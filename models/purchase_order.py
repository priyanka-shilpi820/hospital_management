from odoo import models,fields

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    customer_name=fields.Char(string="Customer Name")