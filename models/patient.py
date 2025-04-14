from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _rec_name = "patient_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one(comodel_name="res.partner", string="Name", domain=[("email", "!=", False)],
                                 tracking=True, required=True, stored=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender")
    is_patient_in_ward = fields.Boolean("is patient in ward")
    admit_date = fields.Date("Admit date")
    discharge_date = fields.Date("discharge Date")
    date_of_birth = fields.Date(string="DOB")
    patient_names = fields.Many2many(comodel_name="hospital.doctor", string="Doctors")
    patient_lines = fields.One2many("hospital.patient.line", "patient", "Order lines")
    email = fields.Char(string="email")  # related="patient_id.email"

    user_id = fields.Many2one("res.users", "user", compute="compute_user_company")
    company_id = fields.Many2one("res.company", "company", compute="compute_user_company")

    def compute_user_company(self):
        for rec in self:
            rec.user_id = self.env.user
            rec.company_id = self.env.user.company_id.id

    @api.onchange("patient_id")
    def onchange_patient_name(self):
        for rec in self:
            print(rec)
            rec.email = rec.patient_id.email

    # def compute_patient_id(self):
    #  for rec in self:
    #    print(rec)
    #  rec.email=rec.patient_id.email


class HospitalPatientLines(models.Model):
    _name = "hospital.patient.line"

    product_id = fields.Many2one("product.product", "product name")
    qty = fields.Integer("qty")
    unit_price = fields.Float("Unit price")
    patient = fields.Many2one("hospital.patient", "patient")
