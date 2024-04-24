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
    SELECT BO.DOCID, DOC.TITLE, BO.ISBN, COUNT(*) AS NO_OF_TIMES_BORROWED
    FROM BOOK AS BO, DOCUMENT AS DOC, COPY AS COP, BORROWS AS BOR
    WHERE BO.DOCID = DOC.DOCID AND DOC.DOCID = COP.DOCID AND COP.BID = '{branch_no}' AND COP.DOCID = BOR.DOCID AND COP.COPYNO = BOR.COPYNO AND COP.BID = BOR.BID
    GROUP BY BO.DOCID
    ORDER BY COUNT(*) DESC
    LIMIT {limit};
    """
    description = "Get number N and branch number I as input and print the N most borrowed books in branch I."
    return self.database_utilities.format_query_result(query, description)