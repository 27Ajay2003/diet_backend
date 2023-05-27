from django.db import models

# Create your models here.
class Recipe(models.Model):
    RecipeId = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    RecipeCategory = models.CharField(max_length=255)
    RecipeInstructions = models.TextField()
    CookTime = models.IntegerField()
    PrepTime = models.IntegerField()
    TotalTime = models.IntegerField()
    RecipeIngredientParts = models.TextField()
    Calories = models.FloatField()
    FatContent = models.FloatField()
    SaturatedFatContent = models.FloatField()
    CholesterolContent = models.FloatField()
    SodiumContent = models.FloatField()
    CarbohydrateContent = models.FloatField()
    FiberContent = models.FloatField()
    SugarContent = models.FloatField()
    ProteinContent = models.FloatField()

    def __str__(self):
        return self.Name