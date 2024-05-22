
SELECT
    DISTINCT(CleSemaineISOAnneeStatistique) AS SemaineISO
FROM
    [commun].[DimDate] WITH (NOLOCK)
WHERE
    [CleMoisAnnee] = '{CleMoisAnnee}';