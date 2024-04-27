import MySQLdb
from faker import Faker
from datetime import datetime
from database.queries.database_utilities import DatabaseUtilities


class DocumentReserve:
  """
  Class DocumentReserve provides methods to reserve a document.
  """


  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.db_utilities = DatabaseUtilities(connection)
  

  def execute(self,
              rid: str,
              doc_id: str,
              copy_no: str,
              bid: str) -> dict:
    """
    Reserve a document.

    Args:
      rid (str): The reader ID.
      doc_id (str): The document ID.
      copy_no (str): The copy number.
      bid (str): The branch ID.
    
    Returns:
      dict: The reservation information.
    """

    query_to_check_if_reader_exists = f"""
    SELECT COUNT(*)
    FROM READER
    WHERE RID = '{rid}';
    """
    result_query_to_check_if_reader_exists = self.db_utilities.format_query_result(
      query=query_to_check_if_reader_exists,
      description="Check if reader exists"
    )
    if result_query_to_check_if_reader_exists['query_result'][0]['COUNT(*)'] == 0:
      result_query_to_check_if_reader_exists["descriptive_error"] = "Reader does not exist"
      return result_query_to_check_if_reader_exists
    
    query_to_check_if_branch_exists = f"""
    SELECT COUNT(*)
    FROM BRANCH
    WHERE BID = '{bid}';
    """
    result_query_to_check_if_branch_exists = self.db_utilities.format_query_result(
      query=query_to_check_if_branch_exists,
      description="Check if branch exists"
    )
    if result_query_to_check_if_branch_exists['query_result'][0]['COUNT(*)'] == 0:
      result_query_to_check_if_branch_exists["descriptive_error"] = "Branch does not exist"
      return result_query_to_check_if_branch_exists
    
    query_to_check_if_document_exists = f"""
    SELECT COUNT(*)
    FROM DOCUMENT
    WHERE DOCID = '{doc_id}';
    """
    result_query_to_check_if_document_exists = self.db_utilities.format_query_result(
      query=query_to_check_if_document_exists,
      description="Check if document exists"
    )
    if result_query_to_check_if_document_exists['query_result'][0]['COUNT(*)'] == 0:
      result_query_to_check_if_document_exists["descriptive_error"] = "Document does not exist"
      return result_query_to_check_if_document_exists
    
    query_to_check_if_document_copy_is_available = f"""
    SELECT COUNT(*)
    FROM COPY
    WHERE DOCID = '{doc_id}' AND COPYNO = '{copy_no}' AND BID = '{bid}';
    """
    result_query_to_check_if_document_copy_is_available = self.db_utilities.format_query_result(
      query=query_to_check_if_document_copy_is_available,
      description="Check if document copy is available"
    )
    if result_query_to_check_if_document_copy_is_available['query_result'][0]['COUNT(*)'] == 0:
      result_query_to_check_if_document_copy_is_available["descriptive_error"] = "Document copy is not available"
      return result_query_to_check_if_document_copy_is_available
    
    query_to_check_if_document_copy_is_reserved = f"""
    SELECT COUNT(*)
    FROM RESERVES
    WHERE DOCID = '{doc_id}' AND COPYNO = '{copy_no}' AND BID = '{bid}';
    """
    result_query_to_check_if_document_copy_is_reserved = self.db_utilities.format_query_result(
      query=query_to_check_if_document_copy_is_reserved,
      description="Check if document copy is reserved"
    )
    if result_query_to_check_if_document_copy_is_reserved['query_result'][0]['COUNT(*)'] > 0:
      result_query_to_check_if_document_copy_is_reserved["descriptive_error"] = "Document copy is already reserved"
      return result_query_to_check_if_document_copy_is_reserved
    
    fake_resno = "RES" + Faker().password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False) 
    dtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query_to_insert_in_reservation = f"""
    INSERT INTO RESERVATION
    VALUES ('{fake_resno}', '{dtime}');
    """
    result_query_to_insert_in_reservation = self.db_utilities.format_query_result(
      query=query_to_insert_in_reservation,
      description="Reserve a document"
    )
    print(result_query_to_insert_in_reservation)
    if result_query_to_insert_in_reservation['status'] == "error":
      result_query_to_insert_in_reservation["descriptive_error"] = "Error in reserving the document"
      return result_query_to_insert_in_reservation
    
    query_to_insert_in_reserves = f"""
    INSERT INTO RESERVES
    VALUES ('{rid}', '{fake_resno}', '{doc_id}', '{copy_no}', '{bid}');
    """
    result_query_to_insert_in_reserves = self.db_utilities.format_query_result(
      query=query_to_insert_in_reserves,
      description="Reserve a document"
    )
    if result_query_to_insert_in_reserves['status'] == "error":
      result_query_to_insert_in_reserves["descriptive_error"] = "Error in reserving the document"
      return result_query_to_insert_in_reserves
    
    query_to_check_insertion_in_reserves = f"""
    SELECT *
    FROM RESERVES
    WHERE RID = '{rid}' AND RESERVATION_NO = '{fake_resno}' AND DOCID = '{doc_id}' AND COPYNO = '{copy_no}' AND BID = '{bid}';
    """
    result_query_to_check_insertion_in_reserves = self.db_utilities.format_query_result(
      query=query_to_check_insertion_in_reserves,
      description="Check if the insertion in RESERVES was successful"
    )
    if result_query_to_check_insertion_in_reserves['status'] == "error":
      result_query_to_check_insertion_in_reserves["descriptive_error"] = "Error in reserving the document"
      return result_query_to_check_insertion_in_reserves
    
    self.db_utilities.connection.commit()
    return result_query_to_check_insertion_in_reserves