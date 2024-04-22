import MySQLdb
from database.queries.requisite.insert_fake_data import InsertFakeData


class PopulateAllTables:
  """
  Used to populate all the tables in the database with random data
  """
  
  def __init__(self, connection: MySQLdb.Connection, fake_data_config: dict) -> None:
    self.connection = connection
    self.insert_fake_data = InsertFakeData(
      connection=connection, 
      fake_data_config=fake_data_config
    )
  

  def insert_random_data(self) -> dict:
    """
    Used to populate all the tables in the database

    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query and metadata
    """
    
    publisher_metadata = self.insert_fake_data.insert("publisher")
    branch_metadata = self.insert_fake_data.insert("branch")
    borrowing_metadata = self.insert_fake_data.insert("borrowing")
    reservation_metadata = self.insert_fake_data.insert("reservation")
    reader_metadata = self.insert_fake_data.insert("reader")
    person_metadata = self.insert_fake_data.insert("person")
    document_metadata = self.insert_fake_data.insert("document")
    copy_metadata = self.insert_fake_data.insert("copy")
    borrows_metadata = self.insert_fake_data.insert("borrows")
    reserves_metadata = self.insert_fake_data.insert("reserves")
    journal_volume_metadata = self.insert_fake_data.insert("journal_volume")
    book_metadata = self.insert_fake_data.insert("book")
    authors_metadata = self.insert_fake_data.insert("authors")
    journal_issue_metadata = self.insert_fake_data.insert("journal_issue")
    gedits_metadata = self.insert_fake_data.insert("gedits")
    proceedings_metadata = self.insert_fake_data.insert("proceedings")
    chairs_metadata = self.insert_fake_data.insert("chairs")

    return {
      "status": "success",
      "message": "All tables populated successfully",
      "metadata": {
        "publisher": publisher_metadata,
        "branch": branch_metadata,
        "borrowing": borrowing_metadata,
        "reservation": reservation_metadata,
        "reader": reader_metadata,
        "person": person_metadata,
        "document": document_metadata,
        "copy": copy_metadata,
        "borrows": borrows_metadata,
        "reserves": reserves_metadata,
        "journal_volume": journal_volume_metadata,
        "book": book_metadata,
        "authors": authors_metadata,
        "journal_issue": journal_issue_metadata,
        "gedits": gedits_metadata,
        "proceedings": proceedings_metadata,
        "chairs": chairs_metadata
      }
    }