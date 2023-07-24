
import mysql.connector
from mysql.connector import Error



CONNECTION_ERROR = 'Connection error'
SUCCESSFULL = 'True'
DEFAULT_SCHEMA = False   

NULL = 'NULL'
NOT_NULL = 'NOT NULL'
AUTO_INCREMENT = 'AUTO_INCREMENT'
INT = 'INT'
VARCHAR = 'VARCHAR(255)'
FLOAT = 'FLOAT'
DEFAULT = 'DEFAULT '

NOTHING = 0   # Print nothing
INFO = 1      # Only print errors
WARNING = 2   # Print All messages 



Error_auto_increment = 'AUTO INCREMENT Only can set on INT type'

class databaseConnector:
    """this class used to create connection and do some functions such as : add , delete , create , etc
    """
    def __init__(self,username,password,host,database_name,log_level=1):
        pass
        self.user_name=username
        self.password=password
        self.host=host
        self.data_base_name=database_name
        self.log_level=log_level
        self.check_connection()
        



    def set_log_level(self,num):
        
        """_this function used to set log level
        """
        self.log_level = num

    def connect(self):
        """
        Establishes a connection to the MySQL database using the provided parameters and set self parameters for connecting.

        Returns:
            tuple: A tuple containing the cursor and connection objects.
        """
        connection = mysql.connector.connect(host=self.host,
                                            database=self.data_base_name,
                                            user=self.user_name,
                                            password=self.password,
                                            auth_plugin='mysql_native_password')  
        cursor = connection.cursor()
        self.cursor, self.connection = cursor, connection  
        return cursor,connection     


    def check_connection(self):
        """
        Check if the connection to the database can be established.

        Inputs: None

        Returns:
            bool: A boolean value determining if the connection is established or not.
        """

        try:
            self.connect() # connect to database
            #
            flag=True
            #
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info() # get informations of database
                cursor = self.connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchall()
                #
                return True

        except Exception as e:
            self.show_message(('Error while connecting to MySQL' ,e))
            return False


    def execute_quary(self, query):
        """
        Executes the specified query on the database.
    
        Args:
            query (str): The SQL query to execute.
    
        Returns:
            Cursor: The database cursor object.
    
        Raises:
            None.
    
        Example:
            To execute an SQL query "SELECT * FROM users", you can call the function like this:
                execute_quary("SELECT * FROM users")
    
            This will execute the query on the database and return the cursor object.
    
        """
        try:
            if self.check_connection():
                self.cursor.execute(query)
            else:
                self.show_message('Error in SQL Connection')
                return False

        except Exception as e:
            self.show_message(('Error while E xecute Quary' ,e))
            return False


        return self.cursor


    def add_record(self,table_name , data):
        """this function is used to add a new record to table

        Inputs:
            table_name : name of table
            data: data that want to add to the database
        
        Returns: Flag of doing query
        """
        parametrs = self.get_col_name(table_name=table_name,without_auto_incresment=True)
        len_parameters = len(parametrs)
        cols =''
        for parm in parametrs:
            cols+=parm+','
        cols = cols[:-1]
        cols = '(' + cols + ')'
        parametrs = cols
        s ='%s,'*len_parameters
        s = s[:-1]
        s = '(' + s + ')'

        try:

            if self.check_connection():
                mySql_insert_query = """INSERT INTO {} {} 
                                    VALUES 
                                    {} """.format(table_name,parametrs,s)
                self.cursor.execute(mySql_insert_query,data)
                self.connection.commit()
                self.cursor.close()
                return True

            else:
                self.show_message('Error in SQL Connection')
                return False

        except Exception as e:
            self.show_message(e)
            return False


    def update_record(self,table_name,col_name,value,id_name,id_value):

        """this function used to update a row with input parms

        Inputs:
            table_name (str): name of that table we want to change data
            col_name (str): column name of table
            value (str): new vlaue
            id_name (str): name of column for selecting the row 
            id_value (str): Row specifier
        
        Returns: Flag of doing query
        """

       
        try:
            if self.check_connection():
                mySql_insert_query = """UPDATE {} 
                                        SET {} = {}
                                        WHERE {} ={} """.format(table_name,col_name,("'"+value+"'"),id_name,("'"+id_value+"'"))
                self.cursor.execute(mySql_insert_query)
                self.connection.commit()
                self.show_message((self.cursor.rowcount, "Record Updated successfully "),level=1)
                self.cursor.close()
                return True
            else:
                self.show_message('Error in SQL Connection')
                return False
            
        except mysql.connector.Error as e:
            self.show_message(("Error Update Record ", e))
            return False
            


    def remove_record(self, table_name , col_name, value ):
        """
        this function is used to remove a record from table acourding to specified column value

        Inputs:
            col_name: name of the column to check for (in string)
            value: value of the column (in string)
            table_name: name of the table (in string)
        
        Returns:
            results: a boolean determining if the record is removed or not
        """
        
        try:
            if self.check_connection():
                mySql_delete_query = """DELETE FROM {} WHERE {}={};""".format(table_name,col_name,"'"+value+"'")

                self.execute_quary(mySql_delete_query)
                self.connection.commit()
                self.cursor.close()
                self.show_message((self.cursor.rowcount, "Remove successfully from table {}".format(table_name)))
                return True
            
            else:
                self.show_message('Error in SQL Connection')
                return False
            
        except Exception as e:
            self.show_message(("Error In Remove Record ", e))
            return False



    def search(self, table_name, col_name, value):
        """
        Searches the specified table for records matching the given column name and value.

        Args:
            table_name (str): The name of the table to search.
            col_name (str): The name of the column to match against.
            value (Any): The value to search for. It will be converted to a string for comparison.

        Returns:
            list: A list of dictionaries representing the matching records. Each dictionary contains
                the field names as keys and corresponding field values as values.

        Raises:
            None.

        Example:
            To search for all records in the table 'employees' where the 'department' column is 'Sales',
            you can call the function like this:
                search('employees', 'department', 'Sales')

            This will return a list of dictionaries representing the matching records.

        """

        try:
            value = str(value)
            int_type=False
            if value.isnumeric():
                int_type = True


            # try:
            if self.check_connection():
                if int_type:
                    sql_select_Query = "SELECT * FROM {} WHERE {} = {};".format(table_name,col_name,str(value))
                    cursor=self.execute_quary(sql_select_Query)
                else:

                    sql_select_Query = """SELECT * FROM {} WHERE {} = {} """.format(table_name,col_name,("'"+str(value)+"'"))
                    cursor=self.execute_quary(sql_select_Query)

                records = cursor.fetchall()
                
                field_names = [col[0] for col in cursor.description]
                res = []

                for record in records:
                    record_dict = {}
                    for i in range( len(field_names) ):
                        record_dict[ field_names[i] ] = record[i]
                    # print('record_dict',record_dict)
                    
                    res.append( record_dict )
                
                return res

            else:
                self.show_message('Error in SQL Connection')
                return []

        except Exception as e:
            self.show_message(("Error In Search Table ", e))
            return []


    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------

    def delete_table(self,table_name):
        """
        Deletes the specified table from the database.

        Args:
            table_name (str): The name of the table to delete.

        Returns:
            bool: True if the table was successfully deleted, False otherwise.

        Raises:
            None.

        Example:
            To delete a table named 'employees', you can call the function like this:
                delete_table('employees')

            This will drop the 'employees' table from the database and return True if successful,
            or False if there was an error.

        """
        try:
            if self.check_connection():
                sql_Delete_table = "DROP TABLE {};".format(table_name)
                cursor=self.execute_quary(sql_Delete_table)  
                return True  
            else:
                self.show_message('Error in SQL Connection')
                return False                               
        except Exception as e:
            self.show_message(("Error In Delete Table ", e))
            return False
    # #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------

    def delete_column(self,table_name,col_name):
        """
        Deletes the specified column from the given table.

        Args:
            table_name (str): The name of the table from which to delete the column.
            col_name (str): The name of the column to delete.

        Returns:
            bool: True if the column was successfully deleted, False otherwise.

        Raises:
            None.

        Example:
            To delete a column named 'email' from a table named 'users', you can call the function like this:
                delete_column('users', 'email')

            This will drop the 'email' column from the 'users' table and return True if successful,
            or False if there was an error.

        """
        try:
            if self.check_connection():
                if self.check_column_exist(table_name=table_name,col_name=col_name):
                    try:
                        query = "ALTER TABLE {} DROP COLUMN {};".format(table_name,col_name)
                        self.execute_quary(query=query)
                        self.show_message('Column Deleted',level=1)
                        return True

                    except mysql.connector.Error as e:
                        self.show_message(("Error Drop Column ", e))
                        return False
                else:
                    self.show_message('Column Not Exist for Drop')
                    return False
            else:
                self.show_message('Error in SQL Connection')
                return False
        except mysql.connector.Error as e:
            self.show_message(("Error In D elete Column ", e))
            return False



    def get_col_name(self,table_name,without_auto_incresment=False):
        """
        Retrieves the column names of the specified table.

        Args:
            table_name (str): The name of the table from which to retrieve column names.
            without_auto_increment (bool): Optional. If True, excludes the auto-increment column(s)
                from the returned list of column names. Default is False.

        Returns:
            list: A list of column names as strings.

        Raises:
            None.

        Example:
            To get the column names of a table named 'users', you can call the function like this:
                get_col_name('users')

            This will return a list of column names for the 'users' table.

            To exclude auto-increment columns from the returned list, you can pass True as the second argument:
                get_col_name('users', without_auto_increment=True)

            This will return a list of column names for the 'users' table, excluding any auto-increment columns.

        """
        try:
            if self.check_connection():
                cursor=self.execute_quary("select * from {}".format(table_name))
                records = cursor.fetchall()
                field_names = [col[0] for col in cursor.description]

                if without_auto_incresment:
                    col_name = list(self.get_auto_increment_col_name(table_name=table_name))
                    res = []
                    for name in field_names:
                        if name not in col_name:
                            res.append(name)

                    return res
            else:
                self.show_message('Error in SQL Connection')
                return []

            return field_names
        except mysql.connector.Error as e:
            self.show_message(("Error In Get Column Name ", e))
            return []


    def get_auto_increment_col_name(self,table_name):
        """
        Retrieves the column name(s) with auto-increment property from the specified table.

        Args:
            table_name (str): The name of the table from which to retrieve the auto-increment column name(s).

        Returns:
            list: A list of column name(s) with auto-increment property.

        Raises:
            None.

        Example:
            To get the auto-increment column name(s) from a table named 'users', you can call the function like this:
                get_auto_increment_col_name('users')

            This will return a list of column name(s) with auto-increment property in the 'users' table.

        """

        if self.check_connection():
            cursor=self.execute_quary("select COLUMN_NAME from information_schema.columns where TABLE_SCHEMA='test2' and TABLE_NAME='users' and EXTRA like '%auto_increment%';")
            records = cursor.fetchall()
            if records:
                records=records[0]
            return records
        else:
            self.show_message('Error in SQL Connection')
            return []

    def get_all_content(self,table_name, limit=False, limit_size=20, offset=0, reverse_order=False,column_order = 'id'):
        """
        Retrieves all content from the specified table.

        Args:
            table_name (str): The name of the table from which to retrieve the content.
            limit (bool): Optional. If True, limits the number of records returned by limit_size.
                Default is False.
            limit_size (int): Optional. The maximum number of records to retrieve if limit is True.
                Default is 20.
            offset (int): Optional. The number of records to skip before retrieving the content.
                Default is 0.
            reverse_order (bool): Optional. If True, retrieves the content in reverse order.
                Default is False.
            column_order (str): Optional. The name of the column used for sorting the content.
                Default is 'id'.

        Returns:
            list: A list of dictionaries representing the content. Each dictionary contains
                the field names as keys and corresponding field values as values.

        Raises:
            None.

        Example:
            To retrieve all content from a table named 'users', you can call the function like this:
                get_all_content('users')

            This will return a list of dictionaries representing all content in the 'users' table.

            You can specify additional parameters to limit the number of records, offset, sorting order, etc.
            For example, to retrieve the first 10 records sorted by the 'name' column in reverse order, you can call:
                get_all_content('users', limit=True, limit_size=10, reverse_order=True, column_order='name')

            This will return a list of dictionaries representing the first 10 records sorted by 'name' column
            in reverse order from the 'users' table.

        """
            
        sort_order = 'DESC' if reverse_order else 'ASC'
        try:
            if self.check_connection():
                if not limit:
                    sql_select_Query = "select * from {} ORDER BY {} {}".format(table_name,column_order, sort_order)
                else:
                    sql_select_Query = "select * from {} ORDER BY {} {} LIMIT {} OFFSET {}".format(table_name,column_order, sort_order, limit_size, offset)
                    
                cursor=self.execute_quary(sql_select_Query)
                records = cursor.fetchall()
                field_names = [col[0] for col in cursor.description]
                cursor.close()
                res = []
                for record in records:
                        record_dict = {}
                        for i in range( len(field_names) ):
                            record_dict[ field_names[i] ] = record[i]
                        res.append( record_dict )
                return res
            else:
                self.show_message('Error in SQL Connection')
                return []
        except Exception as e:
            self.show_message(("Error In Get all Content", e))
            return []


    def check_table_exist(self,table_name):
        """
        Checks if the specified table exists in the database.

        Args:
            table_name (str): The name of the table to check.

        Returns:
            bool: True if the table exists, False otherwise.

        Raises:
            None.

        Example:
            To check if a table named 'users' exists in the database, you can call the function like this:
                check_table_exist('users')

            This will return True if the 'users' table exists, or False if it does not exist.

        """
        try:
            sql_check_table = "SELECT * FROM {}.{};".format(self.data_base_name,table_name)
            self.execute_quary(sql_check_table)        
            return True                              
        except mysql.connector.Error as e:
            self.show_message(("Error reading data from MySQL table", e))
            return False


    def create_table(self,table_name):
        """
        Creates a new table with the specified name, if it doesn't already exist.

        Args:
            table_name (str): The name of the table to create.

        Returns:
            bool: True if the table was created or already exists, False otherwise.

        Raises:
            None.

        Example:
            To create a table named 'users', you can call the function like this:
                create_table('users')

            This will create the 'users' table with a primary key column named 'id' if it doesn't already exist.
            If the table already exists, the function will return True without creating it.

        """
        try:
            if self.check_connection():
                query = "CREATE TABLE IF NOT EXISTS {} (id INT NOT NULL PRIMARY KEY);".format(table_name)
                self.execute_quary(query=query)
                return True
            else:
                self.show_message('Error in SQL Connection')
                return False
        except mysql.connector.Error as e:
            self.show_message(("Error Create Table ", e))
            return False


    def check_column_exist(self,table_name,col_name):
        """
        Checks if the specified column exists in the given table.

        Args:
            table_name (str): The name of the table to check.
            col_name (str): The name of the column to check.

        Returns:
            bool: True if the column exists in the table, False otherwise.

        Raises:
            None.

        Example:
            To check if a column named 'email' exists in a table named 'users', you can call the function like this:
                check_column_exist('users', 'email')

            This will return True if the 'email' column exists in the 'users' table, or False if it does not exist.

        """
        try:
            if self.check_connection():
                query = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}'".format(table_name)
                cursor=self.execute_quary(query=query)
                schemas = cursor.fetchall()
                for col in schemas:
                    if col_name == col[3]:
                        self.show_message('Column Exist')
                        return True
            else:
                self.show_message('Error in SQL Connection')
                return False
            return False
        except mysql.connector.Error as e:
            self.show_message(("Error check_column_exist ", e))
            return False



    def add_column(self,table_name,col_name,type,len=255,Null=NULL,AI=False,default=''):
        """
        Adds a new column to the specified table.

        Args:
            table_name (str): The name of the table to add the column to.
            col_name (str): The name of the column to add.
            type (str): The data type of the column.
            len (int): Optional. The length of the column if the data type is VARCHAR. Default is 255.
            Null (str): Optional. The NULL constraint for the column. Default is NULL.
            AI (bool): Optional. If True, the column has the AUTO_INCREMENT property. Default is False.
            default (Any): Optional. The default value for the column. Default is an empty string.

        Returns:
            bool: True if the column was successfully added, False otherwise.

        Raises:
            None.

        Example:
            To add a column named 'email' with data type VARCHAR(50) to a table named 'users', you can call the function like this:
                add_column('users', 'email', 'VARCHAR', len=50)

            This will add the 'email' column with the specified data type and length to the 'users' table.

            You can specify additional parameters such as Null, AI, and default value for the column.

        """
        
        if not AI:
            AI=''
        else:
            AI=AUTO_INCREMENT

        self.create_table(table_name=table_name)

        if type == VARCHAR:
            type='VARCHAR({})'.format(len)

        if default!= '':
            if isinstance(default,str):
                default = DEFAULT+"'"+default+"'"
            else:
                default = DEFAULT+str(default)

           


        if type !=INT and AI==AUTO_INCREMENT:
            self.show_message((' Error Add Column {}'.format(Error_auto_increment)))
            return False

        if not self.check_column_exist(table_name=table_name,col_name=col_name):

            try:
                if self.check_connection():
                    query = "ALTER TABLE  {} ADD {} {} {} {} {};".format(table_name,col_name,type,Null,AI,default)
                    self.execute_quary(query=query)
                    return True
                else:
                    self.show_message('Error in SQL Connection')
                    return False

            except mysql.connector.Error as e:
                self.show_message(("Error Add Column ", e))
                return False

        else:
            return False


    def create_schema(self,schema_name):
        """
        Creates a new database schema with the specified name, if it doesn't already exist.

        Args:
            schema_name (str): The name of the schema to create.

        Returns:
            bool: True if the schema was created or already exists, False otherwise.

        Raises:
            None.

        Example:
            To create a schema named 'mydb', you can call the function like this:
                create_schema('mydb')

            This will create the 'mydb' schema if it doesn't already exist.
            If the schema already exists, the function will return True without creating it.

        """
        try:
            if self.check_connection():
                query = "CREATE SCHEMA IF NOT EXISTS {};".format(schema_name)
                self.execute_quary(query=query)
                return True
            else:
                self.show_message('Error in SQL Connection')
                return False
        except mysql.connector.Error as e:
            print("Error create schema ", e)
            return False


    def get_all_schemas(self):
        """
        Retrieves the names of all available database schemas.

        Returns:
            list: A list of schema names.

        Raises:
            None.

        Example:
            To retrieve the names of all available schemas, you can call the function like this:
                get_all_schemas()

            This will return a list of schema names.

        """
        try:
            if self.check_connection():
                query = "show schemas"
                cursor=self.execute_quary(query=query)
                schemas = cursor.fetchall()
                return schemas
            else:
                self.show_message('Error in SQL Connection')
                return []
        except mysql.connector.Error as e:
            print("Error Get schema names ", e)
            return False



    def show_message(self,error,level=0):
        """
        Displays an error message.

        Args:
            error (str): The error message to display.
            level (int): Optional. The level of the error message. Default is 0.

        Returns:
            None.

        Raises:
            None.

        Example:
            To display an error message "Error in SQL Connection", you can call the function like this:
                show_message('Error in SQL Connection')

            This will print the error message to the console.

            You can also specify a level for the error message. For example:
                show_message('Error in SQL Connection', level=1)

            This will print the error message to the console only if the log level is set to 1.

        """
        
        if self.log_level==1:
            print(error)







if __name__ == "__main__":
    db=dataBase('root','Dorsa-1400','localhost','test2')
    db.create_table('users')   # you can dont create table
    a=db.get_all_schemas()
    db.add_column(table_name='users',col_name='first_name',type=VARCHAR,len=80,Null=NOT_NULL)
    db.add_column(table_name='users',col_name='last_name',type=VARCHAR,len=80,Null=NOT_NULL)
    db.add_column(table_name='users',col_name='email',type=VARCHAR,len=80,Null=NOT_NULL)

    content=db.get_all_content('asdw2')

    col_name=db.get_col_name('asdw')

    # db.delete_column('users','id')

    # data = ('milad','moltaji','m.moltaji')
    # for _ in range(50):
    #     ret =db.add_record('users',data='__YOUR_DATA__')

    db.get_auto_increment_col_name('users')

    db.update_record(table_name='asdw2',col_name='test4',value='11',id_name='id',id_value='1')

    db.remove_record(table_name='users',col_name='first_name',value='m')
    
    r = db.get_all_content(table_name='users',limit=True,column_order='email')
    
    a=db.search(table_name='users',col_name='first_name',value='m')




