
SELECT MIN(CleMoisAnnee) AS CleMoisAnnee
    FROM [commun].[DimDate] WITH (NOLOCK)
    WHERE CleSemaineISOAnneeStatistique = {Periode};