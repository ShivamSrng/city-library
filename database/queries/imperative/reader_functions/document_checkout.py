import MySQLdb
import datetime
from faker import Faker


class DocumentCheckout:
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
  

  def checkout_document(self,
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
    SELECT *
    FROM READER AS R
    WHERE R.RID = '{reader_id}';
    """
    cursor = self.connection.cursor()
    cursor.execute(reader_exists_query)
    reader = cursor.fetchall()
    
    if len(reader) == 0:
      cursor.close()
      return {
        "message": "Reader does not exist"
      }
    else:
      document_exists_query = f"""
      SELECT *
      FROM COPY AS COP
      WHERE COP.DOCID = '{document_id}' AND COP.COPYNO = '{copy_no}' AND COP.BID = '{branch_id}';
      """
      cursor.execute(document_exists_query)
      document = cursor.fetchall()
      
      if len(document) == 0:
        cursor.close()
        return {
          "message": "Document does not exist"
        }
      else:
        fake_borno = "BOR" + Faker().password(length=6, special_chars=False, digits=True, upper_case=True, lower_case=False)
        bd_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        due_datetime = (datetime.datetime.now() + datetime.timedelta(days=20)).strftime("%Y-%m-%d %H:%M:%S")
        add_new_borrower_query = f"""
        INSERT INTO BORROWING (BOR_NO, BDTIME, RDTIME) VALUES ('{fake_borno}', '{bd_datetime}', '{due_datetime}');
        """
        cursor.execute(add_new_borrower_query)
        check_if_reader_has_borrowed_query = f"""
        SELECT COUNT(*)
        FROM BORROWS AS BOR
        WHERE BOR.RID = '{reader_id}' AND BOR.DOCID = '{document_id}' AND BOR.COPYNO = '{copy_no}' AND BOR.BID = '{branch_id}';
        """
        cursor.execute(check_if_reader_has_borrowed_query)
        reader_has_borrowed = cursor.fetchall()
        if len(reader_has_borrowed) > 0:
          cursor.close()
          return {
            "message": "Reader has already borrowed the document"
          }
        add_new_data_in_borrows_query = f"""
        INSERT INTO BORROWS (BOR_NO, DOCID, COPYNO, BID, RID) VALUES ('{fake_borno}', '{document_id}', '{copy_no}', '{branch_id}', '{reader_id}');
        """
        cursor.execute(add_new_data_in_borrows_query)
        self.connection.commit()
        cursor.close()
        return {
          "status": "success",
          "message": "Document checked out successfully",
          "queries": {
            "reader_exists_query": reader_exists_query.replace("\n", "").replace("\t", "").strip(),
            "document_exists_query": document_exists_query.replace("\n", "").replace("\t", "").strip(),
            "add_new_borrower_query": add_new_borrower_query.replace("\n", "").replace("\t", "").strip(),
            "add_new_data_in_borrows_query": add_new_data_in_borrows_query.replace("\n", "").replace("\t", "").strip()
          },
          "table_afftected": "BORROWS",
          "table_affected": "BORROWING",
          "new_data_inserted": {
            "BORROWS": {
              "BOR_NO": fake_borno,
              "DOCID": document_id,
              "COPYNO": copy_no,
              "BID": branch_id,
              "RID": reader_id
            },
            "BORROWING": {
              "BOR_NO": fake_borno,
              "BDTIME": bd_datetime,
              "RDTIME": due_datetime
            }
          }
        }