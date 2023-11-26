from django.db import models


def dynamic_fieldname_model_factory(fields_prefix):
    class AbstractModel(models.Model):

        class Meta:
            abstract = True

    AbstractModel.add_to_class(
        fields_prefix + '_title',
        models.CharField(max_length=255, blank=True, default=''),
    )
    return AbstractModel


class ModelOne(dynamic_fieldname_model_factory('someprefix1')):
    id = models.AutoField(primary_key=True)


class ModelTwo(dynamic_fieldname_model_factory('someprefix2')):
    id = models.AutoField(primary_key=True)
