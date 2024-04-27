import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class ComputeFineCollectedByBranch:
  """
  Used to compute the fine collected by each branch
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
    self.database_utilities = DatabaseUtilities(connection)
  
  
  def execute(self,
              startdatetime: str,
              enddatetime: str) -> dict:
    """
    Used to compute the fine collected by each branch
    
    Args:
      startdatetime (str): The startdatetime to compute the fine collected by each branch
      enddatetime (str): The enddatetime to compute the fine collected by each branch
    
    Returns:
      dict: A dictionary containing the metadata of the fine collected by each branch
    """
    
    query = f"""
    SELECT BRAN.BID, BRAN.BNAME, SUM(GREATEST(DATEDIFF(BORW.RDTIME, BORW.BDTIME) - 20, 0) * 0.2) / COUNT(*) AS TOTAL_FINE_COLLECTED
    FROM BRANCH AS BRAN, BORROWS AS BOR, BORROWING AS BORW
    WHERE BRAN.BID = BOR.BID AND BOR.BOR_NO = BORW.BOR_NO AND BORW.BDTIME >= '{startdatetime}' AND BORW.RDTIME <= '{enddatetime}'
    GROUP BY BRAN.BID
    ORDER BY SUM(GREATEST(DATEDIFF(BORW.RDTIME, BORW.BDTIME) - 20, 0)) / COUNT(*) DESC;
    """
    description = "Get a start date S and an end date E as input and print, for each branch, the branch Id and name and the average fine paid by the borrowers for documents borrowed from this branch during the corresponding period of time."
    return self.database_utilities.format_query_result(query, description)