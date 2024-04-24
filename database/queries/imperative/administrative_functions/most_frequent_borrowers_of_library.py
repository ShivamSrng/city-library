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
    
    query_to_check_if_library_exists = f"""
    SELECT COUNT(*)
    FROM BRANCH
    WHERE BNAME='{library_name}';
    """

    result_of_library_check = self.database_utilities.format_query_result(
      query=query_to_check_if_library_exists,
      description="Check if the library exists"
    )
    if result_of_library_check["query_result"][0]["COUNT(*)"] == 0:
      result_of_library_check["descriptive_error"] = "Library does not exist"
      return result_of_library_check
    
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