from odoo import models, fields

class PatientReportWizard(models.TransientModel):
    _name = 'patient.report.wizard'
    _description = 'Patient Report Wizard'

    date_from = fields.Date("From Date")
    date_to = fields.Date("To Date")

    def print_xlsx_report(self):
        return {
            'type': 'ir.actions.report',
            'report_type': 'xlsx',
            'data': {
                'model': 'patient.report.wizard',
                'options': {
                    'date_from': self.date_from.isoformat(),
                    'date_to': self.date_to.isoformat(),
                },
                'output_format': 'xlsx',
                'report_name': 'patient_report',
            },
            'report_name': 'hospital_management.patient_report_xlsx',
        }