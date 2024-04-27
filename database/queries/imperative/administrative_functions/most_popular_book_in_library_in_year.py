import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class MostPopularBookInLibraryInYear:
  """
  Get a year as input and print the 10 most popular books of that year in the library
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
    self.database_utilities = DatabaseUtilities(connection)
  
  
  def execute(self,
              year: int,
              library_name: str) -> dict:
    """
    Get a year as input and print the 10 most popular books of that year in the library
    
    Args:
      year (int): The year to get the most popular book in the library
      library_name (str): The name of the library to get the most popular book in the year
    
    Returns:
      dict: A dictionary containing the metadata of the most popular book in the library in a year
    """
    
    query = f"""
    SELECT BO.DOCID, DOC.TITLE, COUNT(DISTINCT REA.RID) AS NO_OF_TIMES_BORROWED 
    FROM BORROWS AS BOR, BOOK AS BO, READER AS REA, BORROWING AS BORW, DOCUMENT AS DOC
    WHERE BO.DOCID = BOR.DOCID AND BOR.BOR_NO = BORW.BOR_NO AND BOR.RID = REA.RID AND DOC.DOCID = BO.DOCID AND BORW.BDTIME LIKE '{year}%' AND BOR.BID IN (
      SELECT DISTINCT BID
      FROM BRANCH
      WHERE BNAME='{library_name}'
    )
    GROUP BY BO.DOCID
    ORDER BY COUNT(DISTINCT REA.RID) DESC
    LIMIT 10;
    """
    description = "Get a year as input and print the 10 most popular books of that year in the library."
    return self.database_utilities.format_query_result(query, description)