# -*- coding: utf-8 -*-
"""
 Récupération dles dates de six mois d'historique pour une semaine iso donnée
"""

from datetime import datetime
from typing import TYPE_CHECKING
from typing import Tuple

from dateutil.relativedelta import relativedelta

from time_periodes.get_range_date import get_range_date

if TYPE_CHECKING:
    from logger import LOGGER
    from sql_operations import SQLOperations


def get_period_etude(sql_operations: 'SQLOperations', parameters: dict, logger: 'LOGGER' = None) -> Tuple[str, str]:
    """Définit une période de 6 mois à partir de la date de fin de l'étude

    :param sql_operations: variable de type SqlManagement
    :param parameters: paramètres de l'étude
    :param logger: gestion des logs
    :return: Tuple (date de début de la période, date de fin de la période)
    """
    try:
        query = """
                    SELECT MIN([CleMoisAnnee]) AS CleMoisAnnee 
                    FROM [commun].[DimDate] \
                    WHERE [CleSemaineISOAnneeStatistique] = {0}
                """.format(parameters['Periode'])

        cle_mois_annee = sql_operations.load_df(query)['CleMoisAnnee'].tolist()[0]
        date_time = datetime.strptime(str(cle_mois_annee), "%Y%m")

        end_period = date_time - relativedelta(months=1)
        end_year, end_month = end_period.year, end_period.month
        end_period = "{0}{1}".format(str(end_year), str(end_month).zfill(2))

        start_period = date_time - relativedelta(months=6)
        start_year, start_month = start_period.year, start_period.month
        start_period = "{0}{1}".format(str(start_year), str(start_month).zfill(2))

        query = """
                SELECT MIN(CleDate) AS MinCleDate, MAX(CleDate) AS MaxCleDate 
                FROM [commun].[DimDate] WITH (NOLOCK)
                WHERE CleMoisAnnee IN ({start_period}, {end_period})
                """.format(start_period=start_period, end_period=end_period)
        df = sql_operations.load_df(query)
        start_period = df["MinCleDate"].tolist()[0]

        _, end_period = get_range_date(sql_operations, parameters['Periodicite'], parameters['Periode'], logger=logger)

        return datetime.strftime(start_period, "%Y-%m-%d"), end_period
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    from sql_connexion import get_sql_operations
    sql_operations = get_sql_operations()
    parameters = dict(Periodicite='hebdo', Periode = 202133)

    date_debut, date_fin = get_period_etude(sql_operations, parameters, logger=None)

    print(date_debut, date_fin)