import MySQLdb
from database.queries.database_utilities import DatabaseUtilities


class RetrieveBranchInformation:
  def __init__(self, mysqlconnection: MySQLdb.Connection) -> None:
    self.connection = mysqlconnection
    self.database_utilities = DatabaseUtilities(mysqlconnection)
  

  def execute(self,
              branch_id: str) -> dict:
    """
    Used to retrieve the branch information from the database

    Args:
      branch_id (str): The branch_id to retrieve the information for

    Returns:
      dict: A dictionary containing the branch information
    """

    check_if_branch_exists_query = f"""
    SELECT COUNT(*)
    FROM BRANCH
    WHERE BID = '{branch_id}';
    """
    branch_exists_result = self.database_utilities.format_query_result(
      query=check_if_branch_exists_query,
      description="Check if the branch exists"
    )
    if branch_exists_result["query_result"][0]["COUNT(*)"] == 0:
      return branch_exists_result
    else:
      retrieve_branch_information_query = f"""
      SELECT BNAME, BLOCATION
      FROM BRANCH
      WHERE BID = '{branch_id}';
      """
      retrieve_branch_information_result = self.database_utilities.format_query_result(
        query=retrieve_branch_information_query,
        description="Retrieve the branch information"
      )
      return retrieve_branch_information_result