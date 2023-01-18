# -*- coding: utf-8 -*-
# © 2020 - TODAY  Albin John
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

import logging

from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)

class LoginCredential(models.Model):
	_name = "login.credential"
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = "Login Credentials"
	_order = 'id desc'

	name = fields.Char('Name', required=True, tracking=True)
	login_url = fields.Char('Login URL', tracking=True)
	login_username = fields.Char('Login Username', copy=False, help="Used to log into the system", tracking=True)
	login_psw = fields.Char('Login Password', copy=False, tracking=True)
	psw_key = fields.Many2one('ir.attachment', string='Key file', copy=False, ondelete='cascade', domain=lambda self:[('id','=',self.psw_key.id)], tracking=True)
	# psw_key = fields.Binary(string='Key file', attachment=True, copy=False)
	note = fields.Text(string='Description', tracking=True)
	allowed_users = fields.Many2many('res.users', string='Allowed Users', copy=False, tracking=True)
	active = fields.Boolean(default=True, tracking=True)
	partner_id = fields.Many2one('res.partner', string='Partner', tracking=True)
	sequence = fields.Integer(string='Sequence', default=10, tracking=True)