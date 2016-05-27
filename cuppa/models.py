from django.db import models

# Create your models here.
class Brew(models.Model):
    def __str__(self):
        desc = "{}: {} {}".format(
            self.name,
            self.milk_level(),
            self.beverage
        )

        if self.sugars > 0:
            if self.sugars == 1:
                desc += " ({} sugar)".format(self.sugars)
            else:
                desc += " ({} sugars)".format(self.sugars)

        return desc

    name = models.CharField(max_length=50)
    beverage = models.CharField(max_length=10)
    sugars = models.IntegerField(default=0)
    milk = models.IntegerField(default=0)
    notes = models.TextField()

    def milk_level(self):
        if self.milk == 0:
            return "black"
        elif self.milk == 1:
            return "white"
        else:
            return "white{}".format("+" * (self.milk-1))