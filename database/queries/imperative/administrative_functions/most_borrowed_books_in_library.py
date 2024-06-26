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
    
    query_to_check_library_name = f"""
    SELECT COUNT(*)
    FROM BRANCH
    WHERE BRANCH.BNAME = '{library_name}';
    """
    result_of_query_to_check_library_name = self.database_utilities.format_query_result(
      query=query_to_check_library_name,
      description="Check if the library name exists."
    )
    if result_of_query_to_check_library_name["query_result"][0]["COUNT(*)"] == 0:
      result_of_query_to_check_library_name["descriptive_error"] = "Library name does not exist."
      return result_of_query_to_check_library_name
    
    query = f"""
    SELECT BO.DOCID, DOC.TITLE, COUNT(DISTINCT BO.DOCID) AS NO_OF_TIMES_BORROWED
    FROM BORROWS AS BOR, BOOK AS BO, DOCUMENT AS DOC
    WHERE BOR.DOCID = BO.DOCID AND BO.DOCID = DOC.DOCID AND BOR.BID IN (
      SELECT DISTINCT BID
        FROM BRANCH
        WHERE BNAME='{library_name}'
    )
    GROUP BY BO.DOCID
    ORDER BY COUNT(DISTINCT BO.DOCID) DESC
    LIMIT {limit};
    """
    description = "Get number N as input and print the N most borrowed books in the library."
    return self.database_utilities.format_query_result(query, description)