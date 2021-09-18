from odoo import models


class PatientCardXLS(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        # print('lines', lines, data)
        # format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
        # format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter', })
        # sheet = workbook.add_worksheet('Patient Card')
        workbook.add_worksheet('Patient Card')
        # sheet.write(2, 2, 'Name', format1)
        # sheet.write(2, 3, lines.patient_name, format2)
        # sheet = workbook.add_worksheet(report_name[:31])
        # bold = workbook.add_format({'bold': True})
        # sheet.write(0, 0, obj.name, bold)
