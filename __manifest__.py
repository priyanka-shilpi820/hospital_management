{
    "name": "hospital management system",
    "author": "priyanka",
    "version": "18.0",
    "license": "LGPL-3",
    "depends": ["sale_management", "mail", "report_xlsx", ],
    "data":
        [
            "security/ir.model.access.csv",
            "views/view_patient.xml",
            "views/view_doctor.xml",
            "views/view_sale_order.xml",
            "views/view_purchase_order.xml",
            "data/patient_confirm_mail.xml",
            "views/view_patient_lines.xml",
            "report/report_patient_template.xml",
            "report/report.xml",
            "wizard/patient_wizard_invoices.xml",
            "views/report_wizard_view.xml",
            "views/menu.xml", ],
}
