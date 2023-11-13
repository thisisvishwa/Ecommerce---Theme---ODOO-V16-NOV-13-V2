{
    "name": "ecommerce_theme_v2_nov_13",
    "version": "1.0",
    "category": "Theme/Ecommerce",
    "summary": "Advanced eCommerce theme for gaming products",
    "sequence": 1,
    "description": """
    This is a fully-featured, advanced eCommerce website theme in Odoo Version 16 Community Edition, targeting businesses selling gaming PCs, laptops, PC components, gaming consoles, and similar products.
    """,
    "depends": ["base", "website_sale", "website_blog"],
    "data": [
        "views/templates.xml",
        "views/product_template_views.xml",
        "views/product_category_views.xml",
        "views/res_users_views.xml",
        "views/error_pages.xml",
        "data/demo_data.xml"
    ],
    "demo": ["data/demo_data.xml"],
    "application": False,
    "installable": True,
    "auto_install": False,
    "external_dependencies": {
        "python": [],
        "bin": []
    }
}