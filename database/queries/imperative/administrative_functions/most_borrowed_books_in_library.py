import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class MostBorrowedBooksInLibrary:
  """
  Get number N as input and print the N most borrowed books in the library
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
    self.database_utilities = DatabaseUtilities(connection)
  
  
  def execute(self,
              limit: int,
              library_name: str) -> dict:
    """
    Get number N as input and print the N most borrowed books in the library
    
    Args:
      limit (int): The limit to get the most borrowed books in the library
      library_name (str): The name of the library to get the most borrowed books in
    
    Returns:
      dict: A dictionary containing the metadata of the most borrowed books in the library
    """
    
    query = f"""
    SELECT BOR.DOCID, DOC.TITLE, BO.ISBN
    FROM BORROWS AS BOR, BOOK AS BO, DOCUMENT AS DOC
    WHERE BOR.BID IN (
      SELECT BID
        FROM BRANCH
        WHERE BNAME='{library_name}'
    ) AND BO.DOCID = BOR.DOCID AND DOC.DOCID = BOR.DOCID
    GROUP BY BOR.DOCID
    ORDER BY COUNT(DISTINCT BOR.RID) DESC
    LIMIT {limit};
    """
    description = "Get number N as input and print the N most borrowed books in the library."
    return self.database_utilities.format_query_result(query, description)