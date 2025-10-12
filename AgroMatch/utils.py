def recommend_crop(soil, rainfall, land_size):
    # Normalize inputs
    soil = soil.lower()
    rainfall = rainfall.lower()

    # Base recommendation logic
    if soil == 'sandy' and rainfall == 'low':
        crop = 'Millet'
        practice = 'Use drought-resistant seeds and mulch to retain moisture.'
    elif soil == 'sandy' and rainfall == 'moderate':
        crop = 'Cowpeas'
        practice = 'Use early-maturing varieties and conserve soil moisture.'
    elif soil == 'clay' and rainfall == 'high':
        crop = 'Rice'
        practice = 'Ensure proper drainage and consider raised beds.'
    elif soil == 'clay' and rainfall == 'moderate':
        crop = 'Sweet Potatoes'
        practice = 'Loosen soil before planting and avoid waterlogging.'
    elif soil == 'loamy' and rainfall == 'moderate':
        crop = 'Maize'
        practice = 'Apply compost and rotate crops to maintain fertility.'
    elif soil == 'loamy' and rainfall == 'high':
        crop = 'Bananas'
        practice = 'Use organic mulch and maintain spacing for airflow.'
    elif soil == 'rocky':
        crop = 'Cassava'
        practice = 'Use raised mounds and minimal tillage.'
    elif soil == 'silty' and rainfall == 'moderate':
        crop = 'Beans'
        practice = 'Use organic compost and monitor for fungal diseases.'
    elif soil == 'silty' and rainfall == 'high':
        crop = 'Arrowroot'
        practice = 'Ensure consistent moisture and partial shade.'
    elif soil == 'peaty':
        crop = 'Cabbage'
        practice = 'Add lime to reduce acidity and use raised beds.'
    elif soil == 'chalky':
        crop = 'Barley'
        practice = 'Add organic matter and monitor for nutrient deficiencies.'
    else:
        crop = 'Sorghum'
        practice = 'Use organic matter and monitor for pests.'

    # Land size adjustments
    if land_size < 2:
        practice += " Consider intercropping or vertical farming to maximize space."
    elif 2 <= land_size <= 5:
        practice += " You can diversify with legumes or short-cycle vegetables."
    elif land_size > 5:
        practice += " Explore cooperative labor or mechanized tools for scale."

    return crop, practice
