from django.db import models


class Tea(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)


class Brew(models.Model):
    def __str__(self):
        if self.beverage == "hotwater":
            desc = "{}: Hot Water".format(self.name)
        else:
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
    milkiness = models.ForeignKey(Tea, blank=True, null=True)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def milk_level(self):
        if self.milk == 0:
            return "black"
        elif self.milk == 1:
            return "white"
        else:
            return "white{}".format("+" * (self.milk-1))
