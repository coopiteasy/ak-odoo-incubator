{
    "name": "Purchase EDI file",
    "version": "14.0.1.0.0",
    "author": "Akretion, Odoo Community Association (OCA)",
    "website": "https://github.com/akretion/ak-odoo-incubator",
    "category": "Purchase",
    "depends": ["base_custom_export", "purchase", "attachment_synchronize"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_supplierinfo_view.xml",
        "views/res_partner_view.xml",
        "views/ir_exports_config.xml",
        "views/edi_transport_config.xml",
    ],
    "demo": [
        "demo/ir_exports_config.xml",
        "demo/edi_transport_config.xml",
        "demo/res_partner.xml",
        "demo/purchase_order.xml",
        "demo/product.xml",
    ],
    "maintainer": "florian-dacosta",
    "license": "AGPL-3",
    "installable": True,
}
