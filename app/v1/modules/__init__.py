"""
Modules
=======

Modules habilita uma separação logica dos recursos.

Você pode controlar os modulos habilitados modificando a variavel de configuração ``ENABLED_MODULES``.
"""


def init_app(app, **kwargs):
    from importlib import import_module

    for module_name in app.config['EnablED_MODULES']:
        import_module('.%s' % module_name, package=__name__).init_app(app, **kwargs)
