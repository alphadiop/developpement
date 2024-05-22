
SELECT
		CAST(prv.value AS INT) AS BoundaryValue
FROM sys.partition_schemes AS ps
INNER JOIN sys.partition_functions AS pf
        ON ps.function_id = pf.function_id
INNER JOIN sys.destination_data_spaces AS dds
        ON ps.data_space_id = dds.partition_scheme_id
INNER JOIN sys.filegroups AS fg
        ON dds.data_space_id = fg.data_space_id
LEFT OUTER JOIN sys.partition_range_values AS prv
        ON dds.destination_id = (convert(int, pf.boundary_value_on_right) + prv.boundary_id)
       AND prv.function_id = pf.function_id
WHERE ps.name = '{SchemeName}' AND prv.value IS NOT NULL