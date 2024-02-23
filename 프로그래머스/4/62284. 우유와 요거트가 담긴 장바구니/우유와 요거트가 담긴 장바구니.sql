SELECT P1.CART_ID
FROM CART_PRODUCTS P1
JOIN CART_PRODUCTS P2 ON P1.CART_ID = P2.CART_ID
WHERE P1.NAME = 'Milk' AND P2.NAME = 'Yogurt'
ORDER BY P1.CART_ID
