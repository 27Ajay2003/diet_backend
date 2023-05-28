import json
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
import pandas as pd
from diet_backend import helper
import itertools
from sklearn.neighbors import NearestNeighbors
import numpy as np


from recommendation.models import Recipe

class RecipeAPIView(APIView):
    
    def get(self,request):
        
        weight=45
        height=170
        age=20
        gender="male"
        objective="gain weight faster"
        activity_level="sedentary"
        bmi=helper.calculate_bmi(weight, height)
        print(bmi)
        calories=helper.calculate_calorie_requirements(age, gender, weight, height, activity_level, objective)
        print(calories)
        meal_calories = helper.divide_calories(calories)
        print(meal_calories)
        breakfast=meal_calories[0]
        breads=meal_calories[1]
        lunch=meal_calories[2]
        dessert=meal_calories[3]
        dinner=meal_calories[4]
        min_limit=helper.calculate_min_limits(age, weight, gender)
        max_limit = helper.calculate_max_limits(age, weight, gender)
        avg_limit=helper.calculate_average_limits(max_limit,min_limit)
        average_nutritional_requirements=avg_limit
        average_nutritional_requirements["Calories"]=calories
        print(average_nutritional_requirements)
        
        print("ehy")
        
        
        
        
        recipes = Recipe.objects.all()
        print("hhy")

        # Convert queryset to DataFrame
        df = pd.DataFrame.from_records(recipes.values())
        print(df.keys())
        df_breakfast=df[df["RecipeCategory"]=="Breakfast"]
        df_breads=df[df["RecipeCategory"]=="Breads"]
        df_lunch=df[df["RecipeCategory"]=="Lunch"]
        df_dessert=df[df["RecipeCategory"]=="Dessert"]
        df_dinner=df[df["RecipeCategory"]=="Dinner"]
        
        
        return Response({'hello': 'success'})
    def post(self, request):
        try:
            weight= request.data["weight"]
            height= request.data["height"]
            age=request.data["age"]
            gender=request.data["gender"]
            preference=request.data["preference"]
            activity_level=request.data["activity_level"]
            objective=request.data["objective"]
            
        except KeyError:
            return Response({'error': 'Improper fields'}, status=status.HTTP_400_BAD_REQUEST)
        bmi=helper.calculate_bmi(weight, height)
        print(bmi)
        calories=helper.calculate_calorie_requirements(age, gender, weight, height, activity_level, objective)
        print(calories)
        meal_calories = helper.divide_calories(calories)
        print(meal_calories)
        breakfast=meal_calories[0]
        breads=meal_calories[1]
        lunch=meal_calories[2]
        dessert=meal_calories[3]
        dinner=meal_calories[4]
        min_limit=helper.calculate_min_limits(age, weight, gender)
        max_limit = helper.calculate_max_limits(age, weight, gender)
        avg_limit=helper.calculate_average_limits(max_limit,min_limit)
        average_nutritional_requirements=avg_limit
        average_nutritional_requirements["Calories"]=calories
        print(average_nutritional_requirements)
        
        print("ehy")
        
        
        
        
        recipes = Recipe.objects.all()
        print("hhy")

        # Convert queryset to DataFrame
        df = pd.DataFrame.from_records(recipes.values())
        print(df.keys())
        #print(df["RecipeCategory"].unique())
        df_breakfast=df[df["RecipeCategory"]=="Breakfast"]
        df_breads=df[df["RecipeCategory"]=="Breads"]
        df_lunch=df[df["RecipeCategory"]=="Lunch"]
        df_dessert=df[df["RecipeCategory"]=="Dessert"]
        df_dinner=df[df["RecipeCategory"]=="Dinner"]
        df_breakfast['CalorieDifference'] = abs(df_breakfast['Calories'] - breakfast)
        df_breads['CalorieDifference'] = abs(df_breads['Calories'] - breads)
        df_lunch['CalorieDifference'] = abs(df_lunch['Calories'] - lunch)
        df_dessert['CalorieDifference'] = abs(df_dessert['Calories'] - dessert)
        df_dinner['CalorieDifference'] = abs(df_dinner['Calories'] - dinner)
        
        print("hello")
        
        df_breakfast_sorted = df_breakfast.sort_values('CalorieDifference')
        df_breads_sorted = df_breads.sort_values('CalorieDifference')
        df_lunch_sorted = df_lunch.sort_values('CalorieDifference')
        df_dessert_sorted = df_dessert.sort_values('CalorieDifference')
        df_dinner_sorted = df_dinner.sort_values('CalorieDifference')
        top_100_breakfast = df_breakfast_sorted.head(15)
        top_100_breads = df_breads_sorted.head(15)
        top_100_lunch = df_lunch_sorted.head(15)
        top_100_dessert = df_dessert_sorted.head(15)
        top_100_dinner = df_dinner_sorted.head(15)
        
        
        print(top_100_breads)
        
        a=top_100_breakfast["Calories"]
        b=top_100_breads["Calories"]
        c=top_100_lunch["Calories"]
        d=top_100_dessert["Calories"]
        e=top_100_dinner["Calories"]
        top_100_meals = [a,b,c,d,e]
        combinations_Calories = list(itertools.product(*top_100_meals))
        sums_Calories = [sum(combination) for combination in combinations_Calories]





        a=top_100_breakfast["FatContent"]
        b=top_100_breads["FatContent"]
        c=top_100_lunch["FatContent"]
        d=top_100_dessert["FatContent"]
        e=top_100_dinner["FatContent"]
        top_100_meals = [a,b,c,d,e]
        combinations_FatContent = list(itertools.product(*top_100_meals))
        sums_FatContent = [sum(combination) for combination in combinations_FatContent]





        a=top_100_breakfast["SaturatedFatContent"]
        b=top_100_breads["SaturatedFatContent"]
        c=top_100_lunch["SaturatedFatContent"]
        d=top_100_dessert["SaturatedFatContent"]
        e=top_100_dinner["SaturatedFatContent"]
        top_100_meals = [a,b,c,d,e]
        combinations_SaturatedFatContent = list(itertools.product(*top_100_meals))
        sums_SaturatedFatContent = [sum(combination) for combination in combinations_SaturatedFatContent]





        a=top_100_breakfast["CholesterolContent"]
        b=top_100_breads["CholesterolContent"]
        c=top_100_lunch["CholesterolContent"]
        d=top_100_dessert["CholesterolContent"]
        e=top_100_dinner["CholesterolContent"]
        top_100_meals = [a,b,c,d,e]
        combinations_CholesterolContent = list(itertools.product(*top_100_meals))
        sums_CholesterolContent = [sum(combination) for combination in combinations_CholesterolContent]





        a=top_100_breakfast["SodiumContent"]
        b=top_100_breads["SodiumContent"]
        c=top_100_lunch["SodiumContent"]
        d=top_100_dessert["SodiumContent"]
        e=top_100_dinner["SodiumContent"]
        top_100_meals = [a,b,c,d,e]
        combinations_SodiumContent = list(itertools.product(*top_100_meals))
        sums_SodiumContent = [sum(combination) for combination in combinations_SodiumContent]





        a=top_100_breakfast["CarbohydrateContent"]
        b=top_100_breads["CarbohydrateContent"]
        c=top_100_lunch["CarbohydrateContent"]
        d=top_100_dessert["CarbohydrateContent"]
        e=top_100_dinner["CarbohydrateContent"]
        top_100_meals = [a,b,c,d,e]
        combinations_CarbohydrateContent = list(itertools.product(*top_100_meals))
        sums_CarbohydrateContent = [sum(combination) for combination in combinations_CarbohydrateContent]





        a=top_100_breakfast["FiberContent"]
        b=top_100_breads["FiberContent"]
        c=top_100_lunch["FiberContent"]
        d=top_100_dessert["FiberContent"]
        e=top_100_dinner["FiberContent"]
        top_100_meals = [a,b,c,d,e]
        combinations_FiberContent = list(itertools.product(*top_100_meals))
        sums_FiberContent = [sum(combination) for combination in combinations_FiberContent]





        a=top_100_breakfast["SugarContent"]
        b=top_100_breads["SugarContent"]
        c=top_100_lunch["SugarContent"]
        d=top_100_dessert["SugarContent"]
        e=top_100_dinner["SugarContent"]
        top_100_meals = [a,b,c,d,e]
        combinations_SugarContent = list(itertools.product(*top_100_meals))
        sums_SugarContent = [sum(combination) for combination in combinations_SugarContent]





        a=top_100_breakfast["ProteinContent"]
        b=top_100_breads["ProteinContent"]
        c=top_100_lunch["ProteinContent"]
        d=top_100_dessert["ProteinContent"]
        e=top_100_dinner["ProteinContent"]
        top_100_meals = [a,b,c,d,e]
        combinations_ProteinContent = list(itertools.product(*top_100_meals))
        sums_ProteinContent = [sum(combination) for combination in combinations_ProteinContent]





        a=top_100_breakfast["RecipeId"]
        b=top_100_breads["RecipeId"]
        c=top_100_lunch["RecipeId"]
        d=top_100_dessert["RecipeId"]
        e=top_100_dinner["RecipeId"]
        top_100_meals = [a,b,c,d,e]
        combinations_RecipeId = list(itertools.product(*top_100_meals))
        
        dict_temp={
            "Recipe ids":combinations_RecipeId,
            "FatContent":sums_FatContent,
            "SaturatedFatContent":sums_SaturatedFatContent,
            "CholesterolContent":sums_CholesterolContent,
            "SodiumContent":sums_SodiumContent,
            "CarbohydrateContent":sums_CarbohydrateContent,
            "FiberContent":sums_FiberContent,
            "SugarContent":sums_SugarContent,
            "ProteinContent":sums_ProteinContent,
            "Calories":sums_Calories,
        }
        dfx=pd.DataFrame(dict_temp)
        dfx=dfx[dfx["FatContent"]<=max_limit["FatContent"]]
        dfx=dfx[dfx["SaturatedFatContent"]<=max_limit["SaturatedFatContent"]]
        dfx=dfx[dfx["SodiumContent"]<=max_limit["SodiumContent"]]
        
        sample = np.array(list(average_nutritional_requirements.values()))

        # Initialize the KNN model
        knn = NearestNeighbors(n_neighbors=5)
        knn.fit(dfx.iloc[:, 1:])  # Exclude the first column ("Recipe ids") from the features

        # Find the indices of the most similar samples
        distances, indices = knn.kneighbors([sample])

        # Get the most similar samples
        similar_samples = dfx.iloc[indices[0]]

        # Display the most similar samples
        print(similar_samples)
        
        #similar_samples["Recipe ids"]
        
        appended_df = pd.DataFrame()

# Filter the original DataFrame based on the desired column value
        for i in range(len(similar_samples)):
            for j in similar_samples["Recipe ids"].iloc[i]:
                filtered_rows = df.loc[df['RecipeId'] == j]

            # Append the filtered rows to the new DataFrame
                appended_df = appended_df.append(filtered_rows, ignore_index=True)
        
        
        
        #print(df.head(10))
        print(appended_df)
        data = appended_df.to_dict(orient='records')

    # Convert list of dictionaries to JSON
        json_data = json.dumps(data)

        # Create JSON response
        response = JsonResponse(json_data, safe=False)

        # Set content type
        response["Content-Type"] = "application/json"

        return response
