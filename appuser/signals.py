from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

# implementacion para recibir un signal
# django envia antes de salvar un modelo uno
# y luego de salvarlo envia otro
# receiver es el metodo que escucha el signal y ejecuta la funcion
# recibe varios parametros, pero los mas importantes son el primero
# que le dice con que tipo de señal debe ejecutar dicha funcion
# el otro parametro importante es sender, que le indica que modelo
# envio la señal, si no designa un sender la funcion escuchara cualquier modelo
# mas info https://docs.djangoproject.com/en/1.8/topics/signals/#module-django.dispatch
# https://docs.djangoproject.com/en/1.8/topics/signals/#listening-to-signals

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, **kwargs):
    """
    desde el signal se puede hacer magia cuando el objecto ha sido salvado en la db
    o modificar dicho objecto antes de ser salvado, entre otras muchas cosas
    :param sender: es la clase del modelo que envio la señal
    :param kwargs: son los argumenots adicionales que enviar la señal
    entre esos si el modelo fue creado o modificado (created -> true si es creado, false si es modificado)
    instance, es la instancia del objecto enviado
    :return: None
    """

    created = kwargs.get("created", False)
    if created:
        user = kwargs.get("instance")
        Token.objects.create(user=user)


# para continuar leer apps