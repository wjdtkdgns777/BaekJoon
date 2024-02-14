-- 대여 기록과 차량 정보, 할인 계획을 결합하여 대여 금액을 계산
SELECT
    h.HISTORY_ID, -- 대여 기록 ID
    -- 대여 금액 계산: 일일 대여 요금 * 대여 일수 * (1 - 할인율/100)
    ROUND(
        c.DAILY_FEE * (DATEDIFF(h.END_DATE, h.START_DATE) + 1) * 
        (1 - IFNULL(d.DISCOUNT_RATE, 0) / 100.0)
    ) AS FEE
FROM
    CAR_RENTAL_COMPANY_CAR c
JOIN
    CAR_RENTAL_COMPANY_RENTAL_HISTORY h ON c.CAR_ID = h.CAR_ID
-- 차량 정보와 대여 기록을 차량 ID를 기준으로 결합
LEFT JOIN
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN d ON c.CAR_TYPE = d.CAR_TYPE AND
    -- 대여 기간에 따른 할인 계획을 찾기 위한 조건
    CASE
        WHEN DATEDIFF(h.END_DATE, h.START_DATE) + 1 >= 90 THEN '90일 이상'
        WHEN DATEDIFF(h.END_DATE, h.START_DATE) + 1 >= 30 THEN '30일 이상'
        WHEN DATEDIFF(h.END_DATE, h.START_DATE) + 1 >= 7 THEN '7일 이상'
        -- 대여 기간을 계산하여 해당하는 할인율 적용
    END = d.DURATION_TYPE
WHERE
    c.CAR_TYPE = '트럭' -- 차종이 '트럭'인 차량만 대상으로 함
ORDER BY
    FEE DESC, -- 계산된 대여 금액으로 내림차순 정렬
    h.HISTORY_ID DESC; -- 동일 금액일 경우 대여 기록 ID로 내림차순 정렬
