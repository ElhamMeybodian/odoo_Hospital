# from odoo import api, models, _
#
#
# class PatientCardReport(models.AbstractModel):
#     _name = 'report.om_hospital.report_patient'
#     _description = 'Patient card Report'
#
#     @api.model
#     def _get_report_values(self, docids, data=None):
#         model = self.env.context.get('active_model')
#         docs = self.env[model].browse(self.env.context.get('active_id'))
#                                                                             sort_selection, data)
#         return {
#             'doc_ids': docids,
#             'doc_model': model,
#             'data': data,
#             'docs': docs,
#             'get_employee' :self.get_employee,
#             'get_employee_detail':self.get_employee_detail,
#
#         }
