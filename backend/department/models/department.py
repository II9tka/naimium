from django.db import models

from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    title = models.CharField(
        max_length=128, verbose_name=_('title')
    )
    director = models.OneToOneField(
        'Employee', related_name='_department',
        on_delete=models.DO_NOTHING, null=True, blank=True,
        verbose_name=_('director')
    )

    @cached_property
    def total_employees(self):
        return self.employees.count()

    @cached_property
    def total_salary_employees(self):
        return self.employees.aggregate(models.Sum('salary'))['salary__sum']

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
