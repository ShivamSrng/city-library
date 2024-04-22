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
              year: int) -> dict:
    """
    Get a year as input and print the 10 most popular books of that year in the library
    
    Args:
      year (int): The year to get the most popular book in the library
    
    Returns:
      dict: A dictionary containing the metadata of the most popular book in the library in a year
    """
    
    query = f"""
    SELECT DOC.DOCID, COUNT(DISTINCT RID) AS NO_OF_TIMES_BOUGHT
    FROM DOCUMENT AS DOC, BOOK AS BO, BORROWS AS BOR
    WHERE DOC.PDATE LIKE '{year}%' AND DOC.DOCID = BO.DOCID AND BOR.DOCID = BO.DOCID
    GROUP BY DOC.DOCID
    ORDER BY COUNT(DISTINCT RID) DESC
    LIMIT 10
    """
    description = "Get a year as input and print the 10 most popular books of that year in the library."
    return self.database_utilities.format_query_result(query, description)