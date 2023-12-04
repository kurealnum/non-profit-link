from django.db import models


# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100, unique=False)
    want = models.BooleanField(default=True)
    # bit of a weird field, just sets the units for the UI: i.e.
    # {{ item.count }} {{ item.units_description }} of {{ item.item_name }}
    units_description = models.CharField(max_length=20, default="units")
    org = models.ForeignKey("apps.org", on_delete=models.CASCADE, blank=True)
    count = models.SmallIntegerField(unique=False, default=1)

    def __str__(self):
        return self.item_name

    class Meta:
        unique_together = "apps.org", "item_name"
        verbose_name = "Item"
        verbose_name_plural = "Items"
