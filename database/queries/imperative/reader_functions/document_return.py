import MySQLdb
import datetime
from database.queries.database_utilities import DatabaseUtilities


class DocumentReturn:
  """
  Class DocumentReturn provides methods to return a document borrowed by a borrower.
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.db_utilities = DatabaseUtilities(connection)


  def execute(self,
              bor_no: str,
              docid: str,
              copyno: str,
              bid: str,
              reader_id: str) -> dict:
    """
    Get document information from the database.

    Args:
      bor_no (str): The borrower number.
      docid (str): The document ID.
      copyno (str): The copy number.
      bid (str): The branch ID.
      reader_id (str): The reader ID.
    
    Returns:
      dict: The document information.
    """

    query_to_check_if_document_copoy_is_actually_borrowed = f"""
    SELECT COUNT(*)
    FROM BORROWS AS B
    WHERE B.BOR_NO = '{bor_no}' AND B.DOCID = '{docid}' AND B.COPYNO = '{copyno}' AND B.BID = '{bid}' AND B.RID = '{reader_id}';
    """
    result_query_to_check_if_document_copy_is_actually_borrowed = self.db_utilities.format_query_result(
      query=query_to_check_if_document_copoy_is_actually_borrowed,
      description="Check if document copy is actually borrowed"
    )
    if result_query_to_check_if_document_copy_is_actually_borrowed['query_result'][0]['COUNT(*)'] == 0:
      result_query_to_check_if_document_copy_is_actually_borrowed["descriptive_error"] = "Document copy is not borrowed"
      return result_query_to_check_if_document_copy_is_actually_borrowed
    
    query_to_get_bdtime = f"""
    SELECT BDTIME
    FROM BORROWING
    WHERE BOR_NO = '{bor_no}';
    """
    result_query_to_get_bdtime = self.db_utilities.format_query_result(
      query=query_to_get_bdtime,
      description="Get borrowing date"
    )
    print(result_query_to_get_bdtime)
    if result_query_to_get_bdtime['query_result'][0]['BDTIME'] is None:
      result_query_to_get_bdtime["descriptive_error"] = "Document is not borrowed. There is some issue with the consistency of the database. Please contact the library staff."
      return result_query_to_get_bdtime
    else:
      bdtime = result_query_to_get_bdtime['query_result'][0]['BDTIME']
      rdtime = datetime.datetime.now()
      fine = (rdtime - bdtime).total_seconds() / 86400 * 0.2

    query_to_return_document = f"""
    UPDATE BORROWING
    SET RDTIME = '{rdtime.strftime('%Y-%m-%d %H:%M:%S')}'
    WHERE BOR_NO = '{bor_no}';
    """
    result_query_to_return_document = self.db_utilities.format_query_result(
      query=query_to_return_document,
      description="Return document"
    )
    if result_query_to_return_document['status'] == "error":
      result_query_to_return_document["descriptive_error"] = "There was an error while returning the document"
      return result_query_to_return_document
    
    query_to_set_reader_id_to_null = f"""
    UPDATE BORROWS
    SET RID = NULL
    WHERE BOR_NO = '{bor_no}' AND DOCID = '{docid}' AND COPYNO = '{copyno}' AND BID = '{bid}';
    """
    result_query_to_set_reader_id_to_null = self.db_utilities.format_query_result(
      query=query_to_set_reader_id_to_null,
      description="Set reader ID to NULL"
    )
    if result_query_to_set_reader_id_to_null['status'] == "error":
      result_query_to_set_reader_id_to_null["descriptive_error"] = "There was an error while setting the reader ID to NULL"
      return result_query_to_set_reader_id_to_null
    
    result_query_to_return_document['fine'] = fine
    self.db_utilities.connection.commit()
    return result_query_to_return_document