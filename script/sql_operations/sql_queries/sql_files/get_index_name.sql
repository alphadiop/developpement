
SELECT
     DISTINCT
     TableName = t.name,
     IndexName = ind.name
FROM
     sys.indexes ind
INNER JOIN
     sys.index_columns ic ON  ind.object_id = ic.object_id and ind.index_id = ic.index_id
INNER JOIN
     sys.columns col ON ic.object_id = col.object_id and ic.column_id = col.column_id
INNER JOIN
     sys.tables t ON ind.object_id = t.object_id
WHERE
     ind.is_primary_key = 0
     AND ind.is_unique = 0
     AND ind.is_unique_constraint = 0
     AND t.is_ms_shipped = 0
	 AND t.name = '{TableName}'
;