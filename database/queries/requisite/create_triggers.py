import MySQLdb


class CreateTriggers:
  def __init__(self, connection: MySQLdb.Connection) -> None:
    self.connection= connection


  def __trigger_for_insert_document(self) -> bool:
    trigger_for_insert_document_query = """
    CREATE TRIGGER INSERT_IN_DOCUMENT
    AFTER INSERT ON DOCUMENT
    FOR EACH ROW
    BEGIN ATOMIC
      SELECT COUNT(*)
      FROM PUBLISHER AS P
      WHERE P.PUBLISHERID = NEW.PUBLISHERID
    END;
    """
    cursor = self.connection.cursor()
    res = cursor.execute(trigger_for_insert_document_query)
    self.connection.commit()
    cursor.close()
    if res == 0:
      return False
    return True
  
  def __trigger_for_insert_authors(self) -> bool:
    trigger_for_insert_authors_query = """
    CREATE TRIGGER INSERT_IN_AUTHORS
    AFTER INSERT ON AUTHORS
    FOR EACH ROW
    BEGIN ATOMIC
      SELECT COUNT(*)
      FROM PERSON AS P
      WHERE P.PID = NEW.PID
    END;
    """
    cursor = self.connection.cursor()
    res = cursor.execute(trigger_for_insert_authors_query)
    self.connection.commit()
    cursor.close()
    if res == 0:
      return False
    return True
  

  def __trigger_for_insert_gedits(self) -> bool:
    trigger_for_insert_gedits_query = """
    CREATE TRIGGER INSERT_IN_GEDITS
    AFTER INSERT ON GEDITS
    FOR EACH ROW
    BEGIN ATOMIC
      SELECT COUNT(*)
      FROM PERSON AS P
      WHERE P.PID = NEW.PID
    END;
    """
    cursor = self.connection.cursor()
    res = cursor.execute(trigger_for_insert_gedits_query)
    self.connection.commit()
    cursor.close()
    if res == 0:
      return False
    return True
  

  def __trigger_for_insert_chairs(self) -> bool:
    trigger_for_insert_chairs_query = """
    CREATE TRIGGER INSERT_IN_CHAIRS
    AFTER INSERT ON CHAIRS
    FOR EACH ROW
    BEGIN ATOMIC
      SELECT COUNT(*)
      FROM PERSON AS P
      WHERE P.PID = NEW.PID
    END;
    """
    cursor = self.connection.cursor()
    res = cursor.execute(trigger_for_insert_chairs_query)
    self.connection.commit()
    cursor.close()
    if res == 0:
      return False
    return True
  



  def execute(self) -> dict:
    results = {
      "trigger_for_insert_authors": self.__trigger_for_insert_authors()
    }
    return {
      "status": "success",
      "message": "Triggers created successfully",
      "results": results
    }