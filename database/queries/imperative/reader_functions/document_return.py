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
                   bid: str) -> dict:
    """
    Get document information from the database.

    Args:
      bor_no (str): The borrower number.
      docid (str): The document ID.
      copyno (str): The copy number.
      bid (str): The branch ID.
    
    Returns:
      dict: The document information.
    """

    query_to_check_if_any_such_document_is_borrowed = f"""
      SELECT * FROM BORROWS
      WHERE bor_no = '{bor_no}'
      AND docid = '{docid}'
      AND copyno = '{copyno}'
      AND bid = '{bid}';
    """
    query_to_check_if_any_such_document_is_borrowed_result = self.db_utilities.format_query_result(
      query=query_to_check_if_any_such_document_is_borrowed,
      description="To check if any such document is borrowed."
    )
    if len(query_to_check_if_any_such_document_is_borrowed_result["query_result"]) == 0:
      return {
        "error": "No such document is borrowed or no such document exists."
      }
    
    query_to_fetch_document_borrow_date = f"""
    SELECT BDATE FROM BORROWING
    WHERE bor_no = '{bor_no}  '  
    """
    query_to_fetch_document_borrow_date_result = self.db_utilities.format_query_result(
      query=query_to_fetch_document_borrow_date,
      description="To fetch the document borrow date."
    )
    result = query_to_fetch_document_borrow_date_result["query_result"]
    borrow_date = datetime.datetime.strptime(result[0][0], '%Y-%m-%d').strftime('%Y-%m-%d')
    days_borrowed = (datetime.datetime.now() - datetime.datetime.strptime(borrow_date, '%Y-%m-%d')).days
    fine = 0.20 * days_borrowed

    query_to_update_return_date = f"""
    UPDATE BORROWING
    SET RDATE = '{datetime.datetime.now().strftime('%Y-%m-%d')}'
    WHERE bor_no = '{bor_no}'
    """
    query_to_update_return_date_result = self.db_utilities.format_query_result(
      query=query_to_update_return_date,
      description="To update the return date."
    )
    return {
      "message": "Document returned successfully.",
      "query_result": query_to_update_return_date_result["query_result"],
      "fine": fine,
      "queries": {
        "query_to_check_if_any_such_document_is_borrowed": query_to_check_if_any_such_document_is_borrowed_result,
        "query_to_fetch_document_borrow_date": query_to_fetch_document_borrow_date_result,
        "query_to_update_return_date": query_to_update_return_date_result,
      }
    }
