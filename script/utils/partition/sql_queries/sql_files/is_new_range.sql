
IF EXISTS (SELECT
               *
           FROM
               [sys].[partition_range_values] AS r
           INNER JOIN
               [sys].[partition_functions] AS f
                   ON r.function_id = f.function_id
                   AND f.name = '{NameFunction}'
                   AND r.value = {Range})
BEGIN
    INSERT INTO {TableName} ({Columns}) VALUES ({Range});
END