import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class MostBorrowedBooksInBranch:
  """
  Get number N and branch number I as input and print the N most borrowed books in branch I
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
    self.database_utilities = DatabaseUtilities(connection)
  
  
  def execute(self,
              limit: int,
              branch_no: str) -> dict:
    """
    Get number N and branch number I as input and print the N most borrowed books in branch I
    
    Args:
      limit (int): The limit to get the most frequently borrowing users
      branch_no (str): The branch_no to get the most frequently borrowing users
    
    Returns:
      dict: A dictionary containing the metadata of the most frequently borrowing users
    """
    
    query_to_check_branch_no = f"""
    SELECT COUNT(*)
    FROM BRANCH
    WHERE BRANCH.BID = '{branch_no}';
    """
    result_of_query_to_check_branch_no = self.database_utilities.format_query_result(
      query=query_to_check_branch_no,
      description="Check if the branch number exists."
    )
    if result_of_query_to_check_branch_no["query_result"][0]["COUNT(*)"] == 0:
      result_of_query_to_check_branch_no["descriptive_error"] = "Branch number does not exist."
      return result_of_query_to_check_branch_no
    
    query = f"""
    SELECT DOC.DOCID, DOC.TITLE, COUNT(DISTINCT BO.DOCID) AS NO_OF_TIMES_BORROWED
    FROM BORROWS AS BOR, BOOK AS BO, DOCUMENT AS DOC
    WHERE BOR.DOCID = BO.DOCID AND BOR.BID='{branch_no}' AND BO.DOCID = DOC.DOCID
    GROUP BY BO.DOCID
    ORDER BY COUNT(DISTINCT BO.DOCID) DESC
    LIMIT {limit};
    """
    description = "Get number N and branch number I as input and print the N most borrowed books in branch I."
    return self.database_utilities.format_query_result(query, description)