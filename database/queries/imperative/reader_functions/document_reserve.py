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
    SELECT * FROM READER
    WHERE rid = '{rid}';
    """
    query_to_check_if_reader_exists_result = self.db_utilities.format_query_result(
      query=query_to_check_if_reader_exists,
      description="To check if the reader exists."
    )
    if len(query_to_check_if_reader_exists_result["query_result"]) == 0:
      return {
        "status": "error",
        "error": "No such reader exists.",
        "query": query_to_check_if_reader_exists
      }
    
    query_to_check_if_document_exists = f"""
    SELECT * FROM DOCUMENT
    WHERE docid = '{doc_id}'
    AND copyno = '{copy_no}'
    AND bid = '{bid}';
    """
    query_to_check_if_document_exists_result = self.db_utilities.format_query_result(
      query=query_to_check_if_document_exists,
      description="To check if the document exists."
    )
    if len(query_to_check_if_document_exists_result["query_result"]) == 0:
      return {
        "status": "error",
        "error": "No such document exists.",
        "query": query_to_check_if_document_exists
      }
    query_to_check_if_reader_has_reserved_more_than_10_documents = f"""
    SELECT COUNT(*) FROM RESERVES
    WHERE rid = '{rid}'
    GROUP BY {rid};
    """
    query_to_check_if_reader_has_reserved_more_than_10_documents_result = self.db_utilities.format_query_result(
      query=query_to_check_if_reader_has_reserved_more_than_10_documents,
      description="To check if the reader has reserved more than 10 documents."
    )
    if len(query_to_check_if_reader_has_reserved_more_than_10_documents_result["query_result"]) >= 10:
      return {
        "status": "error",
        "error": "The reader has already reserved 10 documents.",
        "query": query_to_check_if_reader_has_reserved_more_than_10_documents
      }
    while True:
      fake_resno = "RES" + Faker().profile.password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
      query_to_check_whether_generated_resno_already_exists = f"""
      SELECT * FROM RESERVES
      WHERE resno = '{fake_resno}';
      """
      query_to_check_whether_generated_resno_already_exists_result = self.db_utilities.format_query_result(
        query=query_to_check_whether_generated_resno_already_exists,
        description="To check whether the generated reservation number already exists."
      )
      if len(query_to_check_whether_generated_resno_already_exists_result["query_result"]) == 0:
        break
    query_to_reserve_document = f"""
    INSERT INTO RESERVES (RID, RESERVATION_NO, DOCID, COPYNO, BID) VALUES ({rid}, {fake_resno}, {doc_id}, {copy_no}, {bid});
    """
    query_to_reserve_document_result = self.db_utilities.format_query_result(
      query=query_to_reserve_document,
      description="To reserve the document."
    )
    query_to_insert_reservation_no_in_reservation = f"""
    INSERT INTO RESERVATION (RESERVATION_NO, DTIME) VALUES ('{fake_resno}', '{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');
    """
    query_to_insert_reservation_no_in_reservation_result = self.db_utilities.format_query_result(
      query=query_to_insert_reservation_no_in_reservation,
      description="To insert the reservation number in the reservation table."
    )
    return {
      "status": "success",
      "message": "Document reserved successfully.",
      "reservation_no": fake_resno,
      "queries": {
        "query_to_check_if_reader_exists": query_to_check_if_reader_exists_result,
        "query_to_check_if_document_exists": query_to_check_if_document_exists_result,
        "query_to_check_if_reader_has_reserved_more_than_10_documents": query_to_check_if_reader_has_reserved_more_than_10_documents_result,
        "query_to_reserve_document": query_to_reserve_document_result,
        "query_to_insert_reservation_no_in_reservation": query_to_insert_reservation_no_in_reservation_result
      }
    }