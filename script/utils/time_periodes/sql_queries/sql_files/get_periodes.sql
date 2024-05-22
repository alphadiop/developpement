
SELECT
    DISTINCT {ClePeriode}
FROM
    [commun].[DimDate]
WHERE
    {ClePeriode} BETWEEN {StartPeriode} and {EndPeriode};