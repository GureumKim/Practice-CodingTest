WITH AvailableCars AS (
    SELECT 
        c.CAR_ID,
        c.CAR_TYPE,
        c.DAILY_FEE,
        dp.DISCOUNT_RATE,
        c.DAILY_FEE * 30 * (1 - dp.DISCOUNT_RATE / 100.0) AS FEE
    FROM 
        CAR_RENTAL_COMPANY_CAR c
        JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN dp
            ON c.CAR_TYPE = dp.CAR_TYPE AND dp.DURATION_TYPE = '30일 이상'
    WHERE 
        c.CAR_TYPE IN ('세단', 'SUV')
        AND c.CAR_ID NOT IN (
            SELECT DISTINCT r.CAR_ID
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY r
            WHERE r.START_DATE <= '2022-11-30' AND r.END_DATE >= '2022-11-01'
        )
),
FilteredCars AS (
    SELECT 
        CAR_ID,
        CAR_TYPE,
        FEE
    FROM 
        AvailableCars
    WHERE 
        FEE >= 500000 AND FEE < 2000000
)
SELECT 
    CAR_ID,
    CAR_TYPE,
    FLOOR(FEE) AS FEE
FROM 
    FilteredCars
ORDER BY 
    FEE DESC,
    CAR_TYPE ASC,
    CAR_ID DESC;