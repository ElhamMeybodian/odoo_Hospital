from odoo import models, fields, api, _


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_date = fields.Date(string="Appointment Date")

    def delete_patient(self):
        for rec in self:
            rec.patient_id.unlink()
            # print("Test", rec)

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
            'notes': 'Create From The Wizard/Code'
        }
        # adding  a message to the chatter from code
        self.patient_id.message_post(body="Appointment Create Successfully", subject="Appointment Creation")
        # creating appointment from the code
        self.env['hospital.appointment'].create(vals)

    def get_data(self):
        # fetching data from the database table
        # print('Get Data Function')
        # appointments = self.env['hospital.appointment'].search_count([])
        # print('appointments', appointments)
        appointments = self.env['hospital.appointment'].search([])
        for rec in appointments:
            print('Appointment Name', rec.name)
        return {
            "type": "ir.actions.do_nothing"
        }
