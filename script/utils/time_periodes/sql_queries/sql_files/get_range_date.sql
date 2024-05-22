IF EXISTS (
SELECT
    MAX([CleDate]) AS DateFin,
    MIN([CleDate]) AS DateDebut
FROM
    [commun].[DimDate] WITH (NOLOCK)
WHERE
    {ClePeriode} = {Periode});
