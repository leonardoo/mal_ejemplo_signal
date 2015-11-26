from django.apps import AppConfig


class AppUserConfig(AppConfig):
    """
        esta es la configuracion inicial de un modulo, sirve para muchas cosas que jamas he usado, excepto el ready
        este funcion se ejecuta cuando las configuraciones de su modulo estan cargadas

         en el ready deben cargarse los signals, dado que en este punto django ya a cargado todo lo necesario para
         ejecutar sin problemas su modulo
    """

    name = 'appuser'
    verbose_name = "App User"

    def ready(self):
        # me gusta importar relativamente las cosas :v
        # pero no es tan relevante
        from . import signals


# segir en __init__.py
