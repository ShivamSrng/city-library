import MySQLdb


class PreventChickenEgg:
  """
  Used to prevent the chicken-egg problem in the database
  """
  
  
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection = connection
  

  def __alter_authors_table(self) -> dict:
    """
    Used to alter the authors table in a way that it doesn't cause the chicken-egg problem even before and after the insertion of data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query
    """
    
    alter_authors_query = """
    ALTER TABLE AUTHORS
    ADD CONSTRAINT AUTHORS_PERSON_FK
    FOREIGN KEY (PID) REFERENCES PERSON(PID)
    ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT AUTHORS_BOOK_FK
    FOREIGN KEY (DOCID) REFERENCES BOOK(DOCID)
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor = self.connection.cursor()
    cursor.execute(alter_authors_query)
    self.connection.commit()
    cursor.close()
    return {
      "status": "success",
      "message": "Authors table altered successfully",
      "query": alter_authors_query.replace("\n", "").replace("\t", "").strip()
    }


  def __alter_gedits_table(self) -> dict:
    """
    Used to alter the gedits table in a way that it doesn't cause the chicken-egg problem even before and after the insertion of data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query
    """
    
    alter_gedits_query = """
    ALTER TABLE GEDITS
    ADD CONSTRAINT GEDITS_PERSON_FK
    FOREIGN KEY (PID) REFERENCES PERSON(PID)
    ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT GEDITS_JOURNAL_ISSUE_FK
    FOREIGN KEY (DOCID, ISSUE_NO) REFERENCES JOURNAL_ISSUE(DOCID, ISSUE_NO)
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor = self.connection.cursor()
    cursor.execute(alter_gedits_query)
    self.connection.commit()
    cursor.close()
    return {
      "status": "success",
      "message": "Gedits table altered successfully",
      "query": alter_gedits_query.replace("\n", "").replace("\t", "").strip()
    }


  def __alter_chairs_table(self) -> dict:
    """
    Used to alter the chairs table in a way that it doesn't cause the chicken-egg problem even before and after the insertion of data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query
    """
    
    alter_chairs_query = """
    ALTER TABLE CHAIRS
    ADD CONSTRAINT CHAIRS_PERSON_FK
    FOREIGN KEY (PID) REFERENCES PERSON(PID)
    ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT CHAIRS_PROCEEDINGS_FK
    FOREIGN KEY (DOCID) REFERENCES PROCEEDINGS(DOCID)
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor = self.connection.cursor()
    cursor.execute(alter_chairs_query)
    self.connection.commit()
    cursor.close()
    return {
      "status": "success",
      "message": "Chairs table altered successfully",
      "query": alter_chairs_query.replace("\n", "").replace("\t", "").strip()
    }
  

  def __alter_book_table(self) -> dict:
    """
    Used to alter the book table in a way that it doesn't cause the chicken-egg problem even before and after the insertion of data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query
    """
    
    alter_book_query = """
    ALTER TABLE BOOK
    ADD CONSTRAINT BOOK_DOCUMENT_FK
    FOREIGN KEY (DOCID) REFERENCES DOCUMENT(DOCID)
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor = self.connection.cursor()
    cursor.execute(alter_book_query)
    self.connection.commit()
    cursor.close()
    return {
      "status": "success",
      "message": "Book table altered successfully",
      "query": alter_book_query.replace("\n", "").replace("\t", "").strip()
    }


  def __alter_journal_issue_table(self) -> dict:
    """
    Used to alter the journal issue table in a way that it doesn't cause the chicken-egg problem even before and after the insertion of data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query
    """
    
    alter_journal_issue_query = """
    ALTER TABLE JOURNAL_ISSUE
    ADD CONSTRAINT JOURNAL_ISSUE_JOURNAL_VOLUME_FK
    FOREIGN KEY (DOCID) REFERENCES JOURNAL_VOLUME(DOCID)
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor = self.connection.cursor()
    cursor.execute(alter_journal_issue_query)
    self.connection.commit()
    cursor.close()
    return {
      "status": "success",
      "message": "Journal Issue table altered successfully",
      "query": alter_journal_issue_query.replace("\n", "").replace("\t", "").strip()
    }


  def __alter_journal_volume_table(self) -> dict:
    """
    Used to alter the journal volume table in a way that it doesn't cause the chicken-egg problem even before and after the insertion of data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query
    """
    
    alter_journal_volume_query = """
    ALTER TABLE JOURNAL_VOLUME
    ADD CONSTRAINT JOURNAL_VOLUME_DOCUMENT_FK
    FOREIGN KEY (DOCID) REFERENCES DOCUMENT(DOCID)
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor = self.connection.cursor()
    cursor.execute(alter_journal_volume_query)
    self.connection.commit()
    cursor.close()
    return {
      "status": "success",
      "message": "Journal Volume table altered successfully",
      "query": alter_journal_volume_query.replace("\n", "").replace("\t", "").strip()
    }
  

  def __alter_proceedings_table(self) -> dict:
    """
    Used to alter the proceedings table in a way that it doesn't cause the chicken-egg problem even before and after the insertion of data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query
    """
    
    alter_proceedings_query = """
    ALTER TABLE PROCEEDINGS
    ADD CONSTRAINT PROCEEDINGS_DOCUMENT_FK
    FOREIGN KEY (DOCID) REFERENCES DOCUMENT(DOCID)
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor = self.connection.cursor()
    cursor.execute(alter_proceedings_query)
    self.connection.commit()
    cursor.close()
    return {
      "status": "success",
      "message": "Proceedings table altered successfully",
      "query": alter_proceedings_query.replace("\n", "").replace("\t", "").strip()
    }
  

  def __alter_document_table(self) -> dict:
    """
    Used to alter the document table in a way that it doesn't cause the chicken-egg problem even before and after the insertion of data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query
    """
    
    alter_document_query = """
    ALTER TABLE DOCUMENT
    ADD CONSTRAINT DOCUMENT_PUBLISHER_FK
    FOREIGN KEY (PUBLISHERID) REFERENCES PUBLISHER(PUBID)
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor = self.connection.cursor()
    cursor.execute(alter_document_query)
    self.connection.commit()
    cursor.close()
    return {
      "status": "success",
      "message": "Document table altered successfully",
      "query": alter_document_query.replace("\n", "").replace("\t", "").strip()
    }
  

  def __alter_copy_table(self) -> dict:
    """
    Used to alter the copy table in a way that it doesn't cause the chicken-egg problem even before and after the insertion of data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query
    """
    
    alter_copy_query = """
    ALTER TABLE COPY
    ADD CONSTRAINT COPY_DOCUMENT_FK
    FOREIGN KEY (DOCID) REFERENCES DOCUMENT(DOCID)
    ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT COPY_BRANCH_FK
    FOREIGN KEY (BID) REFERENCES BRANCH(BID)
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor = self.connection.cursor()
    cursor.execute(alter_copy_query)
    self.connection.commit()
    cursor.close()
    return {
      "status": "success",
      "message": "Copy table altered successfully",
      "query": alter_copy_query.replace("\n", "").replace("\t", "").strip()
    }
  

  def __alter_borrows_table(self) -> dict:
    """
    Used to alter the borrows table in a way that it doesn't cause the chicken-egg problem even before and after the insertion of data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query
    """
    
    alter_borrows_query = """
    ALTER TABLE BORROWS
    ADD CONSTRAINT BORROWS_READER_FK
    FOREIGN KEY (RID) REFERENCES READER(RID)
    ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT BORROWS_COPY_FK
    FOREIGN KEY (DOCID, COPYNO, BID) REFERENCES COPY(DOCID, COPYNO, BID)
    ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT BORROWS_BORROWING_FK
    FOREIGN KEY (BOR_NO) REFERENCES BORROWING(BOR_NO)
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor = self.connection.cursor()
    cursor.execute(alter_borrows_query)
    self.connection.commit()
    cursor.close()
    return {
      "status": "success",
      "message": "Borrows table altered successfully",
      "query": alter_borrows_query.replace("\n", "").replace("\t", "").strip()
    }
  

  def __alter_reserves_table(self) -> dict:
    """
    Used to alter the reserves table in a way that it doesn't cause the chicken-egg problem even before and after the insertion of data
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query
    """
    
    alter_reserves_query = """
    ALTER TABLE RESERVES
    ADD CONSTRAINT RESERVES_READER_FK
    FOREIGN KEY (RID) REFERENCES READER(RID)
    ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT RESERVES_COPY_FK
    FOREIGN KEY (DOCID, COPYNO, BID) REFERENCES COPY(DOCID, COPYNO, BID)
    ON DELETE CASCADE ON UPDATE CASCADE,
    ADD CONSTRAINT RESERVES_RESERVATION_FK
    FOREIGN KEY (RESERVATION_NO) REFERENCES RESERVATION(RES_NO)
    ON DELETE CASCADE ON UPDATE CASCADE;
    """
    cursor = self.connection.cursor()
    cursor.execute(alter_reserves_query)
    self.connection.commit()
    cursor.close()
    return {
      "status": "success",
      "message": "Reserves table altered successfully",
      "query": alter_reserves_query.replace("\n", "").replace("\t", "").strip()
    }
  

  def execute(self) -> dict:
    """
    Used to prevent the chicken-egg problem in the database
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the metadata of the database after altering the tables
    """
    
    alter_authors_metadata = self.__alter_authors_table()
    alter_gedits_metadata = self.__alter_gedits_table()
    alter_chairs_metadata = self.__alter_chairs_table()
    alter_book_metadata = self.__alter_book_table()
    alter_journal_issue_metadata = self.__alter_journal_issue_table()
    alter_journal_volume_metadata = self.__alter_journal_volume_table()
    alter_proceedings_metadata = self.__alter_proceedings_table()
    alter_document_metadata = self.__alter_document_table()
    alter_copy_metadata = self.__alter_copy_table()
    alter_borrows_metadata = self.__alter_borrows_table()
    alter_reserves_metadata = self.__alter_reserves_table()

    return {
      "status": "success",
      "metadata": {
        "authors": alter_authors_metadata,
        "gedits": alter_gedits_metadata,
        "chairs": alter_chairs_metadata,
        "book": alter_book_metadata,
        "journal_issue": alter_journal_issue_metadata,
        "journal_volume": alter_journal_volume_metadata,
        "proceedings": alter_proceedings_metadata,
        "document": alter_document_metadata,
        "copy": alter_copy_metadata,
        "borrows": alter_borrows_metadata,
        "reserves": alter_reserves_metadata
      }
    }