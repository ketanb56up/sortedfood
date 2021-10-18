from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F,Sum
from django.utils.translation import ugettext_lazy as _

from ingredient.models import Ingredient

class ShoppingList(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    title = models.CharField(_("Title"), max_length=250)

    total_cost = models.PositiveIntegerField(
        _("Cost"), help_text=_("Cost in pence, e.g. £4.53 -> 453"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Shopping List")
        verbose_name_plural = _("Shopping Lists")


    def calculate_cost(self,queryset):
        # Calculate the total cost of the shopping list

        shopping_item = ShoppingListItem.objects.filter(shopping_list=queryset.id).annotate(progress=F('quantity') * F('ingredient__cost_per_unit')).aggregate(progress_sum=Sum('progress'))
        return shopping_item['progress_sum']


class ShoppingListItem(models.Model):

    shopping_list = models.ForeignKey(
        ShoppingList,
        verbose_name=_("Shopping List"),
        related_name="items",
        on_delete=models.CASCADE,
    )

    ingredient = models.ForeignKey(
        Ingredient, verbose_name=_("Ingredient"), on_delete=models.SET_NULL, null=True, limit_choices_to={'is_available':'True'}
    )

    quantity = models.FloatField(_("Quantity"))

    def __str__(self):
        return "{}: {}".format(self.shopping_list, self.ingredient)

    class Meta:
        verbose_name = _("Shopping List Item")
        verbose_name_plural = _("Shopping List Items")
