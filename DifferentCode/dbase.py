class Dbase(object):
    import sqlite3
    conn = sqlite3.connect('base.sqlite')
    cur = conn.cursor()
    
    def __init__(self):
        self.conn = Dbase.conn
        self.cur = Dbase.cur
        self.cur.executescript('''CREATE TABLE IF NOT EXISTS Username
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, username TEXT UNIQUE);
        CREATE TABLE IF NOT EXISTS Password
        (username_id INTEGER, password TEXT)''')
    
    def addName(self, username):
        self.cur.execute('''INSERT OR IGNORE INTO Username (username) VALUES (?)''', (username,))
        self.conn.commit()
        
    def addPassword(self, username, password, replace = True):
        if replace == True:
            self.cur.execute('SELECT id FROM Username WHERE username = ?',(username,))
            test=self.cur.fetchone()
            if test is not None:
                username_id=self.cur.fetchone()[0]
                self.cur.execute('''UPDATE Password SET password = ? WHERE username_id = ?''', (password, username_id))
                self.conn.commit()
        else:
            self.cur.execute('SELECT id FROM Username WHERE username = ?',(username,))
            username_id=self.cur.fetchone()[0]
            self.cur.execute('''INSERT OR REPLACE INTO Password (username_id, password) VALUES (?,?)''', (username_id, password))
            self.conn.commit()
    
    def addNameAndPassword(self, username, password, replace = True):
        if replace == True:
            self.cur.execute('''INSERT OR IGNORE INTO Username (username) VALUES (?)''', (username,))
            self.conn.commit()
            self.cur.execute('SELECT id FROM Username WHERE username = ?',(username,))
            username_id=self.cur.fetchone()[0]
            if self.cur.execute('') != None:
                self.cur.execute('''INSERT OR REPLACE INTO Password (username_id, password) VALUES (?,?)''', (username_id, password))
                self.conn.commit()
            else:
                self.cur.execute('''UPDATE Password SET password = ? WHERE username_id = ?''', (password, username_id))
                self.conn.commit()
            
    def chekUserName(self, username):
        self.cur.execute('SELECT Username.id, Username.username FROM Username WHERE username = ?', (username,))
        row = self.cur.fetchone()
        if row is not None:
            return row
        else:
            return 'Name does not exist.'
        
    def getUserPassword(self, username):
        self.cur.execute('SELECT id FROM Username WHERE username = ?',(username,))
        test=self.cur.fetchone()
        if test is not None:
            username_id=self.cur.fetchone()[0]
            password = self.cur.execute('''SELECT password FROM Password WHERE username_id = ?''',(username_id,))
            for item in password:
                print item
        else:
            print 'This user has no password or there is no such user in database.'
    
    def retrieveUsers(self):
        selected = self.cur.execute('SELECT * FROM Username')
        for item in selected:
            print item
    
    def retrievePasswords(self):
        selected = self.cur.execute('SELECT * FROM Password')
        for item in selected:
            print item
    
    def retrieveAll(self):
        self.cur.execute('SELECT Username.username,Password.password FROM Username INNER JOIN Password ON Username.id = Password.username_id ORDER BY Username.id')
        selected = self.cur.fetchone()
        if selected is not None:
            print selected
        else:
            print 'Your database has no enteries.'
    
    def deleteUser(self, username):
        self.cur.execute('SELECT id FROM Username WHERE username = ?',(username,))
        test=self.cur.fetchone()
        if test is not None:
            username_id=self.cur.fetchone()[0]
            self.cur.execute('DELETE FROM Username WHERE username = ?',(username,))
            self.conn.commit()
            self.cur.execute('DELETE FROM Password WHERE username_id = ?',(username_id,))
            self.conn.commit()
        else:
            print 'No such user in database.'
    
    def closeConnection(self):
        self.conn.commit()
