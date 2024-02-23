SELECT 
    F.CATEGORY, 
    F.PRICE AS MAX_PRICE, 
    F.PRODUCT_NAME
FROM 
    FOOD_PRODUCT F
    INNER JOIN (
        SELECT 
            CATEGORY, 
            MAX(PRICE) AS MAX_PRICE
        FROM 
            FOOD_PRODUCT
        WHERE 
            CATEGORY IN ('과자', '국', '김치', '식용유')
        GROUP BY 
            CATEGORY
    ) AS MaxPrices ON F.CATEGORY = MaxPrices.CATEGORY AND F.PRICE = MaxPrices.MAX_PRICE
ORDER BY 
    F.PRICE DESC;