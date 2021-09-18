from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResPartners(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals_list):
        res = super(ResPartners, self).create(vals_list)
        print('yes working!!!')
        # do the custom coding here
        return res


# ایجاد یک فیلد جدید در ماژول sale
class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    patient_name = fields.Char(string='patient name')


class HospitalsPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    _rec_name = 'patient_name'

    @api.multi
    def name_get(self):
        res = []
        for field in self:
            res.append((field.id, '%s-%s' % (field.name_seq, field.patient_name)))
        return res

    @api.model
    def test_cron_job(self):
        print('Abcd')
        # code accordingly to execute the cron

    # @api.depends('patient_age')
    # def set_age_group(self):
    #     if self.patient_age:
    #         if self.patient_age < 10:
    #             self.age_group = 'minor'
    #         else:
    #             self.age_group = 'major'

    # چک کردن مقدار وارد شده فیلد و برگرداندن پیام در صورت اشتباه (برای ایجاد محدودیت)
    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5:
                raise ValidationError(_('The Age Must be Greater than 5'))

    # برای فیلد محاسباتی
    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if self.patient_age < 10:
                    self.age_group = 'minor'
                else:
                    self.age_group = 'major'

    @api.multi
    def open_patient_appointments(self):
        return {
            'name': _('Appointments'),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

    # print("Hello button click!!!")
    @api.onchange('doctor_id')
    def set_doctor_gender(self):
        for rec in self:
            if rec.doctor_id:
                rec.doctor_gender = rec.doctor_id.gender

    def action_send_card(self):
        print("sending email")
        template_id = self.env.ref('om_hospital.patient_card_email_template').id
        print("template id", template_id)
        template = self.env['mail.template'].browse(template_id)
        print('template', template)
        template.send_mail(self.id, force_send=True)
        # self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)

    patient_name = fields.Char(string='نام بیمار', required=True, track_visibility='always')
    patient_age = fields.Integer('سن', track_visibility='always')
    notes = fields.Text(string='noted')
    image = fields.Binary(string='عکس')
    name = fields.Char(string='Test')
    name_seq = fields.Char(string='Patient ID', required=True, copy=False, readonly=True, index=True,
                           default=lambda self: _('New'))
    gender = fields.Selection([('male', 'Male'), ('fe_male', 'Female')], default='male', string='Gender')
    age_group = fields.Selection([
        ('major', 'Major'),
        ('minor', 'Minor'),
    ], string='Age Group', compute='set_age_group')
    appointment_count = fields.Integer(string='Appointment', compute='get_appointment_count')
    active = fields.Boolean('Active', default=True)
    doctor = fields.Many2one('hospital.doctor', string='doctor')
    email = fields.Char(string='Email')
    user_id = fields.Many2one('res.users', string='PRO')
    contact_number = fields.Char(string='Contact Number', track_visibility='always')
    patient_name_upper = fields.Char(compute='_compute_upper_name', inverse='_inverse_upper_name')

    @api.depends('patient_name')
    def _compute_upper_name(self):
        for rec in self:
            rec.patient_name_upper = rec.patient_name.upper() if rec.patient_name else False

    def _inverse_upper_name(self):
        for rec in self:
            rec.patient_name = rec.patient_name.lower() if rec.patient_name_upper else False

    # وقتی یک ابجکت ایجاد میشود name_seq آن به جای new از ir.sequence استفاده میکند
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            # seq = self.env['ir.sequence']
            # vals['name_seq'] = seq.next_by_code['hospital.patient.sequence'] or _('New')
            # print('ppppppppppppppppppppp')
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalsPatient, self).create(vals)
        return result
