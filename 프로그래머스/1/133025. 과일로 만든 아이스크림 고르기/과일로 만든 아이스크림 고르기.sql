/**
일반적으로 속도와 메모리 사용량 측면에서도 첫 번째 쿼리가 더 효율적일 가능성이 높습니다. 그 이유는 다음과 같습니다:

	1.	명시적 조인의 최적화: 데이터베이스 엔진은 명시적 JOIN 구문을 사용한 쿼리를 더 잘 최적화할 수 있습니다. 내부적으로 최적화된 조인 전략을 사용하여 필요한 데이터만 읽고 처리할 수 있습니다.
	2.	쿼리 계획: 대부분의 현대적인 데이터베이스 엔진은 명시적 조인을 포함한 쿼리의 실행 계획을 더 효과적으로 생성하고 최적화할 수 있습니다. 이는 메모리 사용량과 처리 시간을 줄이는 데 도움이 됩니다.
	3.	필터링의 효율성: 첫 번째 쿼리는 WHERE 절을 통해 조인 후에 필터링을 적용합니다. 이는 필요한 데이터만 조인하고 필터링하는 데 도움이 되므로, 불필요한 데이터 처리를 줄일 수 있습니다.
	4.	구식 조인의 한계: 구식 조인 구문을 사용한 두 번째 쿼리는 조인 조건과 필터 조건이 혼합되어 있을 수 있으며, 이는 데이터베이스 엔진이 최적화하는 데 어려움을 줄 수 있습니다. 특히 복잡한 쿼리의 경우 이러한 차이가 더 두드러질 수 있습니다.
*/

# 첫 번째
SELECT FH.FLAVOR
FROM FIRST_HALF fh
JOIN ICECREAM_INFO ii ON fh.FLAVOR = ii.FLAVOR
WHERE fh.TOTAL_ORDER > 3000
    AND ii.INGREDIENT_TYPE = 'fruit_based'
ORDER BY fh.TOTAL_ORDER DESC;


# 두 번째 ... 별로

# SELECT H.FLAVOR
# FROM FIRST_HALF H, ICECREAM_INFO I
# WHERE H.FLAVOR = I.FLAVOR AND H.TOTAL_ORDER > 3000 AND I.INGREDIENT_TYPE = 'fruit_based'
# ORDER BY TOTAL_ORDER DESC