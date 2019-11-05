from odoo import models, fields, api


class SessionModel(models.Model):
    _name = 'test_app.session_model'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help='Duration in days')
    seats = fields.Integer(string='Number of seats')

    # model_id = fields.Many2one('test_app.first_model', ondelete='casecade', string='FirstModel', required=True)