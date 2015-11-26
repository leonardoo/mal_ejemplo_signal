"""
My app
"""

# aca registra su app, si no aparece la cadena
# default_app_config con su respectiva AppConfig
# django jamas reconocera su signal
# antes el init se usaba para registrar los signal
# no es muy recomendado
default_app_config = 'appuser.apps.AppUserConfig'