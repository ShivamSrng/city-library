import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class MostFrequentBorrowersOfLibrary:
  """
  Get number N as input and print the top N most frequent borrowers (Rid and name) in the library and the number of books each has borrowed.
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
    self.database_utilities = DatabaseUtilities(connection)
  
  
  def execute(self,
              limit: int,
              library_name: str) -> dict:
    """
    Get number N as input and print the top N most frequent borrowers (Rid and name) in the library and the number of books each has borrowed.
    
    Args:
      limit (int): The limit to get the most frequent borrowers of the library
      library_name (str): The library name to get the most frequent borrowers of the library
    
    Returns:
      dict: A dictionary containing the metadata of the most frequent borrowers of the library
    """
    
    query = f"""
    SELECT REA.RID, REA.RNAME, COUNT(DISTINCT BOR.DOCID) AS BOOKS_BORROWED
    FROM READER AS REA, BORROWS AS BOR
    WHERE REA.RID = BOR.RID AND BOR.BID IN (
      SELECT BID
        FROM BRANCH
        WHERE BNAME='{library_name}'
    )
    GROUP BY REA.RID
    ORDER BY COUNT(DISTINCT BOR.DOCID) DESC
    LIMIT {limit};
    """
    description = "Get number N as input and print the top N most frequent borrowers (Rid and name) in the library and the number of books each has borrowed."
    return self.database_utilities.format_query_result(query, description)