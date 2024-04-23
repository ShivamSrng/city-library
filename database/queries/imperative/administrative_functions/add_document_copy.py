import MySQLdb
from faker import Faker
from database.queries.database_utilities import DatabaseUtilities


class AddDocumentCopy:
  def __init__(self, mysqlconnection: MySQLdb.Connection) -> None:
    self.connection = mysqlconnection
    self.database_utilities = DatabaseUtilities(mysqlconnection)


  def execute(self,
              document_id: str,
              branch_id: str) -> dict:
    """
    Used to add a copy of a document to a branch

    Args:
      document_id (str): The document_id to add a copy to
      branch_id (str): The branch_id to add the copy to

    Returns:
      dict: A dictionary containing the add copy details
    """

    check_if_document_exists_query = f"""
    SELECT COUNT(*)
    FROM DOCUMENT
    WHERE DOCID = '{document_id}';
    """ 
    document_exists_result = self.database_utilities.format_query_result(
      query=check_if_document_exists_query,
      description="Check if the document exists"
    )
    if document_exists_result["query_result"] is None:
      return document_exists_result
    else:
      check_if_branch_exists_query = f"""
      SELECT COUNT(*)
      FROM BRANCH
      WHERE BID = '{branch_id}';
      """
      branch_exists_result = self.database_utilities.format_query_result(
        query=check_if_branch_exists_query,
        description="Check if the branch exists"
      )
      if branch_exists_result["query_result"] is None:
        return branch_exists_result
      else:
        fake_copyno = "COP" + Faker().password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
        fake_position = Faker().password(length=3, special_chars=False, digits=True, upper_case=False, lower_case=False) + Faker().password(length=3, special_chars=False, digits=True, upper_case=True, lower_case=False)
        add_copy_query = f"""
        INSERT INTO COPY (DOCID, COPYNO, BID, POSITION)
        VALUES ('{document_id}', '{fake_copyno}', '{branch_id}', '{fake_position}');
        """
        add_copy_result = self.database_utilities.format_query_result(
          query=add_copy_query,
          description="Add a copy of the document to the branch by automatically generating the appropriate copy number and position"
        )
        add_copy_result["new_copy_details"] = {
          "DOCID": document_id,
          "COPYNO": fake_copyno,
          "BID": branch_id,
          "POSITION": fake_position
        }
        return add_copy_result


