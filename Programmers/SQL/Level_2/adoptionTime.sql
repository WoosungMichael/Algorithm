SELECT HOUR(DATETIME) "HOUR", COUNT(HOUR(DATETIME)) "COUNT" FROM ANIMAL_OUTS WHERE 9 <= HOUR(DATETIME) and HOUR(DATETIME) <= 19 GROUP BY HOUR(DATETIME) ORDER BY HOUR(DATETIME)