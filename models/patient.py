from email.policy import default

from odoo import models, fields, api
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _rec_name = "patient_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    patient_id = fields.Many2one(comodel_name="res.partner", string="Name", domain=[("email", "!=", False)],
                                 tracking=True, required=True, stored=True)
    # name = fields.Char(string='Patient ID', required=True, copy=False, readonly=True, default='New')

    seq=fields.Char(string='Patient Sequence' , default='new')
    age = fields.Integer(string="Age")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender")

    is_patient_in_ward = fields.Boolean("is patient in ward")
    admit_date = fields.Date("Admit date")
    discharge_date = fields.Date("discharge Date")
    date_of_birth = fields.Date(string="DOB")
    patient_names = fields.Many2many(comodel_name="hospital.doctor", string="Doctors")
    patient_lines = fields.One2many("hospital.patient.line", "patient", "Order lines")
    image = fields.Image(string="Profile Image")
    email = fields.Char(string="email")  # related="patient_id.email"
    address=fields.Char(string="address")
    project=fields.Char(string="project")
    contact=fields.Char(string="contact")
    status = fields.Selection([("admit", "Admitted"), ("discharge", "Discharged")], "status", default="admit",
                              compute="status_date")





    user_id = fields.Many2one("res.users", "user", compute="compute_user_company")
    company_id = fields.Many2one("res.company", "company", compute="compute_user_company")

    def create(self, vals):
        vals["seq"] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    def compute_user_company(self):
        for rec in self:
            rec.user_id = self.env.user
            rec.company_id = self.env.user.company_id.id

    @api.onchange("patient_id")
    def onchange_patient_name(self):
        for rec in self:
            print(rec)
            rec.email = rec.patient_id.email

    def status_date(self):
        today = date.today()
        for i in self:
            if i.discharge_date and today > i.discharge_date:
                i.status = "discharge"
            else:
                i.status = "admit"

    # def compute_patient_id(self):
    #  for rec in self:
    #    print(rec)
    #  rec.email=rec.patient_id.email

    def send_email(self):
        for rec in self:
            template = self.env.ref("hospital_management.mail_template_patient_confirm")
            template.send_mail(rec.id, force_send=True)

    def view_patient_lines(self):
        self.ensure_one()
        for rec in self:
            return {
                'name': "view patient invoices",
                'view_mode': 'list',
                'res_model': 'hospital.patient.line',
                'domain': [('patient', '=', rec.id)],
                'type': 'ir.actions.act_window',
            }


class HospitalPatientLines(models.Model):
    _name = "hospital.patient.line"

    product_id = fields.Many2one("product.product", "product name")
    qty = fields.Integer("qty")
    unit_price = fields.Float("Unit price")
    patient = fields.Many2one("hospital.patient", "patient")
    subtotal = fields.Float("subtotal", compute="compute_subtotal")
    patient_id = fields.Many2one('hospital.patient', string="Patient")

    def compute_subtotal(self):
        for i in self:
            i.subtotal = i.qty * i.unit_price
