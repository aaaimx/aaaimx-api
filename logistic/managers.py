from django.db import models

class CertificateManager(models.Manager):

    def get_certs_by_type(self, type):
        queryset = self.get_queryset()
        return queryset.filter(type=type)