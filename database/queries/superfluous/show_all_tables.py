import MySQLdb


class ShowAllTables:
  """
  Used to show all the tables in the database
  """


  def __init__(self, mysqlconnection: MySQLdb.Connection) -> None:
    self.connection = mysqlconnection
    self.total_records = 0


  def __count_records(self, table: str) -> int:
    """
    Used to count the number of records in a table
    
    Args:
      table (str): The table name
    
    Returns:
      int: The number of records in the table
    """
    
    count_query = f"""
    SELECT COUNT(*)
    FROM {table};
    """
    cursor = self.connection.cursor()
    cursor.execute(count_query)
    count = cursor.fetchone()[0]
    cursor.close()
    self.total_records += count
    return count
  

  def execute(self) -> dict:
    """
    Used to show all the tables in the database
    
    Args:
      None
    
    Returns:
      dict: The status of the query execution along with the query and metadata
    """
    
    show_all_tables_query = """
    SHOW TABLES;
    """
    cursor = self.connection.cursor()
    cursor.execute(show_all_tables_query)
    tables = cursor.fetchall()
    tables = [table[0] for table in tables]
    tables_metadata = [{table: {"row_count":self.__count_records(table)}} for table in tables]

    return {
      "status": "success",
      "query:": show_all_tables_query.replace("\n", " ").strip(),
      "tables": tables,
      "tables_metadata": tables_metadata,
      "total_tables": len(tables),
      "total_records": self.total_records
    }