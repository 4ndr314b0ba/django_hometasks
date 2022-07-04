import sqlite3 as SQLite

class database:
    def __init__( self, name ):
        self.connected = True

        try:
            self.connection = SQLite.connect( name + ".db" )
        except SQLite.Error as error:
            self.connected = False

            print( f"'{ name }' Unable to connect: " + error )

        if self.connected:
            cursor = self.connection.cursor( )

            query = "CREATE TABLE IF NOT EXISTS sales( id INTEGER PRIMARY KEY, summ INTEGER );"

            cursor.executescript( query )

            cursor.close( )


    def add( self, id, summ ):
        cursor = self.connection.cursor( )

        cursor.execute( "INSERT OR REPLACE INTO sales( id, summ ) VALUES( ?, ? )", [ id, summ ] )

        cursor.close( )

        self.connection.commit( )


    def remove( self, id ):
        cursor = self.connection.cursor( )

        cursor.execute( "DELETE FROM sales WHERE id = ?", [ id ] )

        cursor.close( )

        self.connection.commit( )


    def get( self, id ):
        cursor = self.connection.cursor( )

        cursor.execute( "SELECT summ FROM sales WHERE id = ?", [ id ] )

        result = cursor.fetchone( )

        if result is None:
            print( "Unknown id" )
        else:
            print( result[ 0 ] )

        cursor.close( )

        self.connection.commit( )


_database = database( "sales" )
_database.add( 1, 100 )
_database.get( 1 )
_database.remove( 1 )
_database.get( 1 )

_database.connection.close( )