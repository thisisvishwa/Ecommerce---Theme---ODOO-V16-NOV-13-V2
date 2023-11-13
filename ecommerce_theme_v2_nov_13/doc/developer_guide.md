# Developer Guide for ecommerce_theme_v2_nov_13

## Setup

1. Clone the repository to your local machine.
2. Navigate to the Odoo addons directory.
3. Create a symbolic link to the `ecommerce_theme_v2_nov_13` directory.

## Custom Module Creation

1. Create a new directory for the module in the Odoo addons directory.
2. Create the necessary files: `__init__.py`, `__manifest__.py`, and directories for controllers, models, views, and data.
3. Define the module's metadata in `__manifest__.py`.
4. Define the module's data models in the models directory.
5. Define the module's controllers in the controllers directory.
6. Define the module's views in the views directory.
7. Define the module's demo data in the data directory.

## Theme Customization

1. Define the theme's styles in `custom.scss` in the static/src/css directory.
2. Define the theme's JavaScript functions in `custom.js` in the static/src/js directory.
3. Define the theme's images in the static/src/img directory.
4. Define the theme's templates in the views directory.

## Deployment Instructions

1. Start the Odoo server.
2. Navigate to the Apps menu in the Odoo web interface.
3. Update the Apps list.
4. Search for `ecommerce_theme_v2_nov_13`.
5. Click on Install to install the module.

For more detailed instructions, refer to the `api_documentation.md` file.