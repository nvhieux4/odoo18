# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Theme Xtream Fashion',
    'version': '18.0.1.0.0',
    'category': 'Theme/eCommerce',
    'description': 'Design eCommerce Website with Theme Xtream Fashion',
    'summary': 'Theme Xtream Fashion',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'website_sale_wishlist', 'website_mass_mailing'],
    'data': [
        'security/ir.model.access.csv',
        'views/xtream_testimonials_views.xml',
        'views/contact_us_templates.xml',
        'views/footer_templates.xml',
        'views/shop_templates.xml',
        'views/header_templates.xml',
        'views/snippets/snippets_templates.xml',
        'views/snippets/amazing.xml',
        'views/snippets/new_arrivals.xml',
        'views/snippets/discount.xml',
        'views/snippets/main_banner.xml',
        'views/snippets/main_product.xml',
        'views/snippets/testimonial.xml',
    ],
    'assets': {
      'web.assets_frontend': [
          '/theme_xtream/static/src/css/animate.min.css',
          '/theme_xtream/static/src/css/owl.carousel.min.css',
          '/theme_xtream/static/src/css/owl.theme.default.min.css',
          '/theme_xtream/static/src/css/style.css',
          '/theme_xtream/static/src/js/owl.carousel.js',
          '/theme_xtream/static/src/js/owl.carousel.min.js',
          '/theme_xtream/static/src/js/new_arrivals.js',
          '/theme_xtream/static/src/js/testimonials.js',
          '/theme_xtream/static/src/js/custom.js',
      ]
    },
    'images': [
        'static/description/banner.jpg',
        'static/description/theme_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
