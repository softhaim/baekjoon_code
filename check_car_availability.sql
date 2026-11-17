# 중복으로 CAR_ID의 여러 기록이 있기에 이를 gruping 함.
# 여기서 16일에 start 및 end 사이에 껴있다면 대여중, 아니면 대여 가능
# 결과 예시 (CAR_ID = 2인 경우)
# 첫 번째 기록 (10월 5일 ~ 10월 5일): 10월 16일이 포함되지 않으므로 0
# 두 번째 기록 (10월 15일 ~ 10월 17일): 10월 16일이 포함되므로 1
# 여기서 MAX 로 1인 경우가 있으면 대여중 표시

SELECT 
    CAR_ID,
    CASE 
        WHEN MAX('2022-10-16' BETWEEN START_DATE AND END_DATE) = 1 THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY 
    CAR_ID
ORDER BY 
    CAR_ID DESC;