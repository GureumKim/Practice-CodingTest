SELECT ins.NAME, ins.DATETIME
FROM ANIMAL_INS ins LEFT OUTER JOIN ANIMAL_OUTS outs
    ON ins.ANIMAL_ID = outs.ANIMAL_ID
WHERE outs.DATETIME is NULL
ORDER BY ins.DATETIME limit 3;