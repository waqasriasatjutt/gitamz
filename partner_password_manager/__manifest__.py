# -*- coding: utf-8 -*-

##############################################################################
#
#    Albin John.
#    Copyright (C) 2017-TODAY Albin John(<https://www.linkedin.com/in/albin-john/>).
#    Author: Albin John(<albin@vidts.in>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <https://www.gnu.org/licenses/>.
#
##############################################################################

{
	'name': 'Password Manager',
	'category': 'Extra Tools',
	'author': 'Albin John',
	'website':'https://www.linkedin.com/in/albin-john/',
	'version': '1.1',
	'depends': [
		'contacts',
	],

	'description': """
		Password managers offer greater security and convenience for the use of passwords to access online services.
	""",
	'data': [
		'security/password_security.xml',
		'security/ir.model.access.csv',
		'views/partner_view.xml',
		'views/password_manager_view.xml'
	],
	'qweb': [
        
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 20.00,
    'currency': 'EUR',
}
