from django.db import models


class Postagem(models.Model):
    titulo = models.CharField(max_length=80)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    quantidade = models.CharField(max_length=200)
    valor = models.CharField(max_length=200)

    # a ideia era fazer uma lista de produtos com os 4 atributos....
    # eu consegui fazer a criação através do admin, mas a exibição do que foi feito não rodou