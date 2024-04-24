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
    
    query_to_check_if_branch_exists = f"""
    SELECT COUNT(*)
    FROM BRANCH
    WHERE BID='{branch_no}';
    """
    result_of_branch_check = self.database_utilities.format_query_result(
      query=query_to_check_if_branch_exists,
      description="Check if the branch exists"
    )
    if result_of_branch_check["query_result"][0]["COUNT(*)"] == 0:
      result_of_branch_check["descriptive_error"] = "Branch does not exist"
      return result_of_branch_check
    
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