
ALTER DATABASE {Base}
SET RECOVERY BULK_LOGGED;
GO
INSERT INTO {DstTable}
      ({Columns})
SELECT {Columns}
      FROM {SrcTable};
GO
ALTER DATABASE {Base}
SET RECOVERY FULL;
GO