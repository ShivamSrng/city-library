import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class MostFrequentlyBorrowers:
  """
  Get number N and branch number I as input and print the top N most frequent borrowers (Rid and name) in branch I and the number of books each has borrowed
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
    self.database_utilities = DatabaseUtilities(connection)
  
  
  def execute(self,
              limit: int,
              branch_no: str) -> dict:
    """
    Get number N and branch number I as input and print the top N most frequent borrowers (Rid and name) in branch I and the number of books each has borrowed
    
    Args:
      limit (int): The limit to get the most frequently borrowing users
      branch_no (str): The branch_no to get the most frequently borrowing users
    
    Returns:
      dict: A dictionary containing the metadata of the most frequently borrowing users
    """
    
    query = f"""
    SELECT REA.RID, REA.RNAME, COUNT(DISTINCT COP.COPYNO, COP.DOCID) AS NO_OF_BOOKS_BORROWED
    FROM COPY AS COP, BORROWS AS BOR, READER AS REA
    WHERE COP.BID='{branch_no}' AND COP.BID = BOR.BID AND COP.COPYNO = BOR.COPYNO AND COP.DOCID = BOR.DOCID AND BOR.RID = REA.RID
    GROUP BY RID
    ORDER BY COUNT(DISTINCT COP.COPYNO, COP.DOCID) DESC
    LIMIT {limit};
    """
    description = "Get number N and branch number I as input and print the top N most frequent borrowers (Rid and name) in branch I and the number of books each has borrowed."
    return self.database_utilities.format_query_result(query, description)