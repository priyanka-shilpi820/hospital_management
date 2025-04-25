from odoo import models, fields, api
class PatientAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one("res.partner", "Name", domain=[
        ("email", "!=", False),
    ])
    email = fields.Char(related="patient_id.email", string="email")
    patient_age = fields.Integer("Age")
    date = fields.Date("Date")
    appointment_date = fields.Datetime("appointment date and time")
    company_id = fields.Many2one("res.company", string="Company")
    user_id = fields.Many2one("res.users")
    status = fields.Selection([("draft", "Draft"), ("confirm", "Confirmed")], "status", default="draft")
   # appointment_line_id = fields.One2many("patient.appointments.line", "appointment_id", "appointment fee")



