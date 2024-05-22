
SELECT
    DISTINCT t.name
FROM
    [STAT].[sys].[partitions] AS p
INNER JOIN
    [STAT].[sys].[tables] AS t
        ON p.object_id = t.object_id
WHERE
    p.partition_number <> 1
    AND t.name = '{NameTable}' ;