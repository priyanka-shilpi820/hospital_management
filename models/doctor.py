from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Doctors"
    _rec_name = 'name'

    name = fields.Char(string='Name')
    experience = fields.Integer(string='Experience')
    is_doctor_in_hospital = fields.Boolean(string="Is Doctor in Hospital")
    doctor_id = fields.Many2one('res.partner', string="id_number")
    image_1920=fields.Binary(string='image')
