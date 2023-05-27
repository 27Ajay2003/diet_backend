import csv
from django.core.management.base import BaseCommand
from recommendation.models import Recipe

class Command(BaseCommand):
    help = 'Loads recipe data from CSV file into database'

    def handle(self, *args, **kwargs):
        if Recipe.objects.count() == 0:
            with open('./media/csv/recipe_data.csv') as csvfile:
                reader = csv.DictReader(csvfile)

                # Loop through the rows and create new Recipe objects
                for row in reader:
                    recipe = Recipe(
                        RecipeId=row['RecipeId'],
                        Name=row['Name'],
                        RecipeCategory=row['RecipeCategory'],
                        RecipeInstructions=row['RecipeInstructions'],
                        CookTime=row['CookTime'],
                        PrepTime=row['PrepTime'],
                        TotalTime=row['TotalTime'],
                        RecipeIngredientParts=row['RecipeIngredientParts'],
                        Calories=row['Calories'],
                        FatContent=row['FatContent'],
                        SaturatedFatContent=row['SaturatedFatContent'],
                        CholesterolContent=row['CholesterolContent'],
                        SodiumContent=row['SodiumContent'],
                        CarbohydrateContent=row['CarbohydrateContent'],
                        FiberContent=row['FiberContent'],
                        SugarContent=row['SugarContent'],
                        ProteinContent=row['ProteinContent']
                    )

                    # Save the object to the database
                    recipe.save()

            self.stdout.write(self.style.SUCCESS('Recipe data loaded successfully'))
        else:
            self.stdout.write(self.style.WARNING('Recipe data already exists, skipping data load'))
