import pytz

from odoo import models, fields, api, _

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    def delete_lines(self):
        for rec in self:
            print("Time in UTC", rec.appointment_datetime)
            user_tz = pytz.timezone((self.env.context.get('tz') or self.env.user.tz))
            data_today = pytz.utc.localize(rec.appointment.datatime).astimezone(user_tz)
            print("Time in Local Timezone ..", data_today)
            print('rec', rec)
            rec.appointment_lines = [(5, 0, 0)]

    # برای تعریف Control States and Statusbar Using Buttons
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    # برای تعریف Control States and Statusbar Using Buttons
    def action_done(self):
        for rec in self:
            rec.state = 'done'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            # seq = self.env['ir.sequence']
            # vals['name_seq'] = seq.next_by_code['hospital.patient.sequence'] or _('New')
            # print('ppppppppppppppppppppp')
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    def _get_default_note(self):
        return "Subscribe our youtube channel"

    def _get_default_patient_id(self):
        return 3

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for rec in self:
            return {'domain': {'order': [('partner_id', '=', rec.partner_id.id)]}}

    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True, default=_get_default_patient_id)
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    notes = fields.Text(string='Registration Note', default=_get_default_note)
    appointment_date = fields.Date(string='Date')
    # appointment_date = fields.Date(string='Date', required=True)
    doctor_notes = fields.Text(string='Note')
    appointment_lines = fields.One2many('hospital.appointment.lines', 'appointment_id', string='Appointment Lines')
    pharmacy_notes = fields.Text(string='Note')

    # برای تعریف Control States and Statusbar Using Buttons
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done'), ('cancel', 'Cancel')],
                             string='status', readonly=True, default='draft')
    partner_id = fields.Many2one('res.partner', string="Customer")
    order_id = fields.Many2one('sale.order', string="Sale Order")


class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Appointment Lines'

    product_id = fields.Many2one('product.product', string='Medicine')
    product_qty = fields.Integer(string='Quantity')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment ID')
