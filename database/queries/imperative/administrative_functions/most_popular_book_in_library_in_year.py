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
    SELECT DOC.DOCID, DOC.TITLE, COUNT(DISTINCT RID) AS NO_OF_TIMES_BORROWED 
    FROM DOCUMENT AS DOC, BOOK AS BO, BORROWS AS BOR, BRANCH AS BR, COPY AS CO, BORROWING AS BORRO 
    WHERE BORRO.BOR_NO = BOR.BOR_NO AND BORRO.RDTIME LIKE '{year}%' AND DOC.DOCID = BO.DOCID AND BOR.DOCID = BO.DOCID AND DOC.DOCID = CO.DOCID AND BR.BNAME='{library_name}' AND CO.BID = BR.BID 
    GROUP BY DOC.DOCID 
    ORDER BY COUNT(DISTINCT RID) 
    DESC LIMIT 10
    """
    description = "Get a year as input and print the 10 most popular books of that year in the library."
    return self.database_utilities.format_query_result(query, description)