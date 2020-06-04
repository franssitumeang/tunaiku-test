-- run on bigquery

DECLARE start_date TIMESTAMP DEFAULT '2020-03-02 13:02:00';
DECLARE start_hour TIMESTAMP DEFAULT
  IF (start_date >= TIMESTAMP_ADD(TIMESTAMP_TRUNC(start_date, hour), INTERVAL 30 MINUTE),
      TIMESTAMP_ADD(TIMESTAMP_TRUNC(start_date, hour), INTERVAL 30 MINUTE),
      TIMESTAMP_TRUNC(start_date, hour));
DECLARE end_date TIMESTAMP DEFAULT '2020-03-02 15:55:07';

CREATE TEMP FUNCTION
  GenerateMinuteTimestampArray(
    t0 TIMESTAMP,
    t1 TIMESTAMP,
    minutes INT64) AS ( ARRAY
    ( SELECT
        TIMESTAMP_ADD(t0, INTERVAL minutes * x MINUTE)
      FROM
        UNNEST(GENERATE_ARRAY(0, TIMESTAMP_DIFF(t1, t0, MINUTE))) AS x ));


SELECT
  CASE
    WHEN start_date > ts THEN start_date
    ELSE ts
  END AS A,
  CASE
    WHEN TIMESTAMP_ADD(ts, INTERVAL 30 MINUTE) > end_date THEN end_date
    ELSE TIMESTAMP_ADD(ts, INTERVAL 30 MINUTE)
  END AS B
FROM
  UNNEST(GenerateMinuteTimestampArray(start_hour, end_date, 30)) AS ts
WHERE
  ts <= end_date