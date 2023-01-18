# -*- coding: utf-8 -*-
# © 2020 - TODAY  Albin John
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

import logging

from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
	_inherit = 'res.partner'

	login_credentials = fields.One2many('login.credential', 'partner_id', string="Login Credentials", copy=False, domain=lambda self:['|',('create_uid', '=', self.env.uid),('allowed_users','in',self.env.uid)])