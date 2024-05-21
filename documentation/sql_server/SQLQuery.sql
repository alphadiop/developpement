
SELECT DB_NAME() AS [Current Database];  
GO 


SELECT DB_NAME(database_id) AS [Database], database_id  
FROM sys.databases;  




--L’exemple suivant retourne le nom et la valeur database_id de chaque base de données.
SELECT arrondissement,sum(price) as Prix
FROM Menage.dbo.house_data
GROUP BY arrondissement
ORDER BY arrondissement ASC;



USE Menage;
GO
SELECT arrondissement,sum(price) as Prix
FROM house_data
GROUP BY arrondissement
ORDER BY sum(price) DESC;
GO




SELECT *
FROM Menage.dbo.house_data
WHERE price > 2000;


USE SoinsSanté;
GO
BULK INSERT SoinsSanté.dbo.ebola
    FROM 'D:\data\ebola.txt'
    WITH
    (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',  --CSV field delimiter
    ROWTERMINATOR = '\n',   --Use to shift the control to next row
    ERRORFILE = '',
    TABLOCK
    );
GO

SELECT *
FROM SoinsSanté.dbo.ebola;




SELECT * FROM OPENROWSET(
   BULK 'D:\data\petrol_consumption.csv',
   SINGLE_CLOB) AS DATA;



SELECT * 
FROM "SOINS-SANTE".dbo.winequalitt

---------------Par table-------------------------------------------------
SELECT * 
FROM "SOINS-SANTE".dbo.winequalitt


--BEGIN TRANSACTION


SELECT * 
FROM "SOINS-SANTE".dbo.[python -note]



SELECT * 
FROM "SOINS-SANTE".dbo.sysdiagrams






sp_configure 'show advanced options', 1;
RECONFIGURE;
GO  --Added        
sp_configure 'Ad Hoc Distributed Queries', 1;
RECONFIGURE;


USE Menage;
GO
SELECT * INTO consommation_carburant
FROM OPENROWSET('Microsoft.ACE.OLEDB.12.0','Excel 12.0; Database=D:\data\petrol_consumption.csv', [Prestations$]);
GO


select top 10 *
from openrowset(
    bulk r'D:/data/petrol_consumption.csv',
    format = 'csv',
    parser_version = '3.0',
    firstrow = 2 ) as rows


SELECT * INTO Your_Table FROM OPENROWSET('Microsoft.ACE.OLEDB.12.0',
                        'Excel 12.0;Database=D:\data\soinsSante.xlsx',
                        'SELECT * FROM [Prestations$]')