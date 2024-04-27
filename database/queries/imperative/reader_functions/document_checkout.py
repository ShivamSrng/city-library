import MySQLdb
import datetime
from faker import Faker
from database.queries.database_utilities import DatabaseUtilities


class DocumentCheckout:
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.dbutilites = DatabaseUtilities(connection)
  

  def execute(self,
              document_id: str,
              reader_id: str,
              copy_no: str,
              branch_id: str) -> dict:
    """
    Checkout a document from the library using the given parameters
    
    Args:
      document_id (int): It is the unique identifier of the document
      reader_id (int): It is the unique identifier of the reader who is checking out the document
      copy_no (int): It is the unique identifier of the copy of the document
      branch_id (int): It is the unique identifier of the branch of the library
      
    Returns:
      dict: A dictionary containing the information of the document
    """

    reader_exists_query = f"""
    SELECT COUNT(*)
    FROM READER AS R
    WHERE R.RID = '{reader_id}';
    """
    
    result_reader_exists_query = self.dbutilites.format_query_result(
      query=reader_exists_query,
      description="Check if reader exists"
    )
    if result_reader_exists_query['query_result'][0]['COUNT(*)'] == 0:
      result_reader_exists_query["descriptive_error"] = "Reader does not exist"
      return result_reader_exists_query
    
    branch_exists_query = f"""
    SELECT COUNT(*)
    FROM BRANCH AS B
    WHERE B.BID = '{branch_id}';
    """
    result_branch_exists_query = self.dbutilites.format_query_result(
      query=branch_exists_query,
      description="Check if branch exists"
    )
    if result_branch_exists_query['query_result'][0]['COUNT(*)'] == 0:
      result_branch_exists_query["descriptive_error"] = "Branch does not exist"
      return result_branch_exists_query
    
    document_exists_query = f"""
    SELECT COUNT(*)
    FROM DOCUMENT AS DOC
    WHERE DOC.DOCID = '{document_id}';
    """
    result_document_exists_query = self.dbutilites.format_query_result(
      query=document_exists_query,
      description="Check if document exists"
    )
    if result_document_exists_query['query_result'][0]['COUNT(*)'] == 0:
      result_document_exists_query["descriptive_error"] = "Document does not exist"
      return result_document_exists_query
    
    copy_exists_at_a_branch_query = f"""
    SELECT COUNT(*)
    FROM COPY AS COP
    WHERE COP.DOCID = '{document_id}' AND COP.COPYNO = '{copy_no}' AND COP.BID = '{branch_id}';
    """
    result_copy_exists_at_a_branch_query = self.dbutilites.format_query_result(
      query=copy_exists_at_a_branch_query,
      description="Check if copy exists at a branch"
    )
    if result_copy_exists_at_a_branch_query['query_result'][0]['COUNT(*)'] == 0:
      result_copy_exists_at_a_branch_query["descriptive_error"] = "Copy does not exist at the branch"
      return result_copy_exists_at_a_branch_query
    
    query_to_get_reader_previous_borrows = f"""
    SELECT RID, BID, COUNT(DISTINCT DOCID) AS PREVIOUSLY_BORROWED
    FROM BORROWS AS BOR
    WHERE BOR.RID = '{reader_id}' AND BOR.BID = '{branch_id}'
    GROUP BY RID, BID;
    """

    result_query_to_get_reader_previous_borrows = self.dbutilites.format_query_result(
      query=query_to_get_reader_previous_borrows,
      description="Get the count of previous borrows of the reader"
    )
    if result_query_to_get_reader_previous_borrows['query_result']:
      if result_query_to_get_reader_previous_borrows['query_result'][0]['PREVIOUSLY_BORROWED'] > 10:
        result_query_to_get_reader_previous_borrows["descriptive_error"] = "Reader has already borrowed 10 documents, hence it is not possible to checkout more documents"
        return result_query_to_get_reader_previous_borrows
    
    query_to_check_already_borrowed = f"""
    SELECT COUNT(*)
    FROM BORROWS AS BOR
    WHERE BOR.DOCID = '{document_id}' AND BOR.COPYNO = '{copy_no}' AND BOR.BID = '{branch_id}' AND BOR.RID = '{reader_id}';
    """
    result_query_to_check_already_borrowed = self.dbutilites.format_query_result(
      query=query_to_check_already_borrowed,
      description="Check if the document is already borrowed"
    )
    if result_query_to_check_already_borrowed['query_result'][0]['COUNT(*)'] > 0:
      result_query_to_check_already_borrowed["descriptive_error"] = "The document is already borrowed by you."
      return result_query_to_check_already_borrowed
    
    fake_borno = "BOR" + Faker().password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
    bd_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rd_datetime = (datetime.datetime.now() + datetime.timedelta(days=20)).strftime("%Y-%m-%d %H:%M:%S")
    query_insert_new_record_in_borrowing = f"""
    INSERT INTO BORROWING (BOR_NO, BDTIME, RDTIME) VALUES ('{fake_borno}', '{bd_datetime}', '{rd_datetime}');
    """
    result_query_insert_new_record_in_borrowing = self.dbutilites.format_query_result(
      query=query_insert_new_record_in_borrowing,
      description="Insert new record in BORROWING"
    )
    if result_query_insert_new_record_in_borrowing['status'] == "error":
      result_query_insert_new_record_in_borrowing["descriptive_error"] = "There was an error while checking out your requested copy of the document (in BORROWING Relation)."
    
    query_to_check_insertion_in_borrowing = f"""
    SELECT COUNT(*)
    FROM BORROWING AS BOR
    WHERE BOR.BOR_NO = '{fake_borno}';
    """
    result_query_to_check_insertion_in_borrowing = self.dbutilites.format_query_result(
      query=query_to_check_insertion_in_borrowing,
      description="Check if the insertion in BORROWING was successful"
    )
    if result_query_to_check_insertion_in_borrowing['query_result'][0]['COUNT(*)'] == 0:
      result_query_to_check_insertion_in_borrowing["descriptive_error"] = "There was an error while checking out your requested copy of the document (in BORROWING Relation)."
      return result_query_to_check_insertion_in_borrowing
    
    query_insert_new_record_in_borrows = f"""
    INSERT INTO BORROWS (BOR_NO, DOCID, COPYNO, BID, RID) VALUES ('{fake_borno}', '{document_id}', '{copy_no}', '{branch_id}', '{reader_id}');
    """
    result_query_insert_new_record_in_borrows = self.dbutilites.format_query_result(
      query=query_insert_new_record_in_borrows,
      description="Insert new record in BORROWS"
    )
    if result_query_insert_new_record_in_borrows['status'] == "error":
      result_query_insert_new_record_in_borrows["descriptive_error"] = "There was an error while checking out your requested copy of the document (in BORROWS Relation)."
    
    query_to_check_insertion_in_borrows = f"""
    SELECT *
    FROM BORROWS AS BOR
    WHERE BOR.BOR_NO = '{fake_borno}' AND BOR.DOCID = '{document_id}' AND BOR.COPYNO = '{copy_no}' AND BOR.BID = '{branch_id}' AND BOR.RID = '{reader_id}';
    """
    result_query_to_check_insertion_in_borrows = self.dbutilites.format_query_result(
      query=query_to_check_insertion_in_borrows,
      description="Check if the insertion in BORROWS was successful"
    )
    if not result_query_to_check_insertion_in_borrows['query_result']:
      result_query_to_check_insertion_in_borrows["descriptive_error"] = "There was an error while checking out your requested copy of the document (in BORROWS Relation)."
      return result_query_to_check_insertion_in_borrows
    
    self.dbutilites.connection.commit()
    return result_query_to_check_insertion_in_borrows