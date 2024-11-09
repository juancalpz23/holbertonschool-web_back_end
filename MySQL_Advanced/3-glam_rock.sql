-- Script to list Glam rock bands ranked by longevity

SELECT band_name, (split - formed) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;