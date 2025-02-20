======================
Forbid Record Creation
======================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-akretion%2Fak--odoo--incubator-lightgray.png?logo=github
    :target: https://github.com/akretion/ak-odoo-incubator/tree/14.0/forbid_record_creation
    :alt: akretion/ak-odoo-incubator

|badge1| |badge2| |badge3| 

Forbide to create Odoo objects by raising an alert to the user.
This module is only useful before to reach 'production' step of ERP implementation project.

**Table of contents**

.. contents::
   :local:

Configuration
=============

Put this code in your custom module according to model
you want forbid creation.

.. code:: python

    class AccountMove(models.Model):
        _inherit = ["account.move", "forbidden.model"]
        _name = "account.move"


    class SaleOrder(models.Model):
        _inherit = ["sale.order", "forbidden.model"]
        _name = "sale.order"


    class PurchaseOrder(models.Model):
        _inherit = ["purchase.order", "forbidden.model"]
        _name = "purchase.order"

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/akretion/ak-odoo-incubator/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed
`feedback <https://github.com/akretion/ak-odoo-incubator/issues/new?body=module:%20forbid_record_creation%0Aversion:%2014.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Akretion

Contributors
~~~~~~~~~~~~

* David Beal <david.beal@akretion.com>

Maintainers
~~~~~~~~~~~

This module is part of the `akretion/ak-odoo-incubator <https://github.com/akretion/ak-odoo-incubator/tree/14.0/forbid_record_creation>`_ project on GitHub.

You are welcome to contribute.
