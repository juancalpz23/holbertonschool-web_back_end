-- Script to list Glam rock bands ranked by longevity

SELECT band_name, COALESCE(split, 2020) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%' ;