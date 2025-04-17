from odoo import models


class PatientReportXlsx(models.AbstractModel):
    _name = 'report.hospital_management.patient_report_xlsx_report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data,patients):
        sheet = workbook.add_worksheet("Patients")
        bold = workbook.add_format({'bold': True})
        date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})

        # Headers
        #sheet.write('A1', 'Patient Name', bold)
       # sheet.write('B1', 'Gender', bold)
        #sheet.write('C1', 'Age', bold)
        format1 = workbook.add_format({'font_size': 8, 'align': "vcenter", 'bold': True})
        format2 = workbook.add_format({'font_size': 6, 'align': "vcenter"})

        row = 0
        for patient in patients:
            sheet.write(row + 0, 0, 'Patient Name', format1)
            sheet.write(row + 0, 1, str(patient.patient_id.name) or '', format2)

            sheet.write(row + 1, 0, 'Age', format1)
            sheet.write(row + 1, 1, patient.age or '', format2)

            sheet.write(row + 2, 0, 'Admit Date', format1)
            sheet.write(row + 2, 1, str(patient.admit_date) or '', format2)

            sheet.write(row + 3, 0, 'Discharge Date', format1)
            sheet.write(row + 3, 1, str(patient.discharge_date) or '', format2)

            sheet.write(row + 4, 0, 'Gender' , format1)
            sheet.write(row + 4, 1, patient.gender or '', format2)
