DROP TABLE SEQUENCES;
CREATE TABLE SEQUENCES(
    NAME VARCHAR (32),
    CUR_VAL TEXT
)
COMMENT '로스트아크 거래소 배치 시퀀스';

/* 스퀀스 생성 프로시저(YYYYMMDD####) */
DROP PROCEDURE SP_CREATE_SEQUENCES;
CREATE PROCEDURE SP_CREATE_SEQUENCES(IN SEQUENCE_NAME MEDIUMTEXT)
    MODIFIES SQL DATA
    DETERMINISTIC
BEGIN
    DELETE
    FROM SEQUENCES
    WHERE NAME = SEQUENCE_NAME;

    INSERT INTO SEQUENCES (NAME,
                           CUR_VAL)
    VALUES (SEQUENCE_NAME,
            CONCAT(DATE_FORMAT(NOW(), '%Y%m%d'), '0001'));
END;

/* 시퀀스 NEXT_VAL(YYYYMMDD####) */
DROP FUNCTION FN_NEXT_VAL;
CREATE FUNCTION FN_NEXT_VAL (SEQUENCE_NAME MEDIUMTEXT)
    RETURNS BIGINT UNSIGNED
    MODIFIES SQL DATA
    DETERMINISTIC
    BEGIN

        DECLARE RET_VAL VARCHAR(12); -- 반환 시퀀스 값
        DECLARE CUR_DATE VARCHAR(8); -- 시퀀스 날짜
        DECLARE CUR_CNT VARCHAR(4); -- 시퀀스 순번

        -- 현재 시퀀스 날짜, 시퀀스 순번 가져오기
        SELECT SUBSTR(CUR_VAL, 1, 8) AS CUR_DATE,
               SUBSTR(CUR_VAL, 9) AS CUR_CNT
        INTO CUR_DATE,
             CUR_CNT
        FROM SEQUENCES
        WHERE NAME = SEQUENCE_NAME
          AND SUBSTR(CUR_VAL, 1, 8) = SUBSTR(DATE_FORMAT(NOW(), '%Y%m%d'), 1, 8);

        -- 새로운 날짜의 시퀀스 채번
        IF CUR_DATE IS NULL THEN
            SELECT SUBSTR(DATE_FORMAT(NOW(), '%Y%m%d'), 1, 8) AS CUR_DATE,
                   '0001' AS CUR_CNT
            INTO CUR_DATE,
                 CUR_CNT
            FROM DUAL;
        -- 같은 날짜의 다음 시퀀스 채번
        ELSE
            SELECT CUR_DATE AS CUR_DATE,
                   LPAD(CUR_CNT + 1, 4, 0) AS CUR_CNT
            INTO CUR_DATE,
                 CUR_CNT
            FROM DUAL;
        END IF;

        -- 현재 시퀀스값 UPDATE
        UPDATE SEQUENCES
        SET CUR_VAL = CONCAT(CUR_DATE, CUR_CNT)
        WHERE NAME = SEQUENCE_NAME;

        -- 반환 시퀀스값 SELECT
        SELECT CUR_VAL
        INTO RET_VAL
        FROM SEQUENCES
        WHERE NAME = SEQUENCE_NAME
        LIMIT 1;

        RETURN RET_VAL;
    END;