from django.db import models
from django.utils.translation import gettext_lazy as _

from ..utils import upload_to


class Employee(models.Model):
    first_name = models.CharField(
        max_length=64, verbose_name=_('first_name')
    )
    middle_name = models.CharField(
        max_length=64, verbose_name=_('middle_name')
    )
    last_name = models.CharField(
        max_length=64, db_index=True, verbose_name=_('first_name')
    )
    position = models.CharField(
        max_length=128, help_text=_(
            'Employee post.'
        ), verbose_name=_('position')
    )
    salary = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name=_('salary')
    )
    photo = models.ImageField(
        upload_to=upload_to, verbose_name=_('photo')
    )
    age = models.IntegerField(
        verbose_name=_('age')
    )
    department = models.ForeignKey(
        'Department', related_name='employees',
        on_delete=models.DO_NOTHING, blank=True, null=True,
        verbose_name=_('department')
    )

    @property
    def full_name(self):
        return ' '.join((self.first_name, self.middle_name, self.last_name))

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ('id',)
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
