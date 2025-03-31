import ee

# Authenticate GEE
ee.Authenticate()
# Initialize Earth Engine
ee.Initialize()

# Define Rangwe Contituency Boundary(from GEE Kenya Administrative Dataset)
rangwe_aoi = ee.FeatureCollection('FAO/GAUL_SIMPLIFIED_500m').filter(ee.Filter.eq('ADM2_NAME', 'Rangwe'))

# Check if the region is correctly filtered
print(rangwe_aoi.getInfo())
