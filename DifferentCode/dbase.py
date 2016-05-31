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
                username_id=test[0]
                self.cur.execute('''UPDATE Password SET password = ? WHERE username_id = ?''', (password, username_id))
                self.conn.commit()
        else:
            self.cur.execute('SELECT id FROM Username WHERE username = ?',(username,))
            username_id=self.cur.fetchone()[0]
            self.cur.execute('''INSERT OR REPLACE INTO Password (username_id, password) VALUES (?,?)''', (username_id, password))
            self.conn.commit()
    
    def addNameAndPassword(self, username, password, replace = True):
        self.cur.execute('''INSERT OR IGNORE INTO Username (username) VALUES (?)''', (username,))
        self.conn.commit()
        if replace == True:
            self.cur.execute('SELECT id FROM Username WHERE username = ?',(username,))
            test=self.cur.fetchone()
            if test is not None:
                username_id=test[0]
                self.cur.execute('SELECT username_id FROM Password WHERE username_id = ?', (username_id,))
                item = self.cur.fetchone()
                if item is not None:
                    self.cur.execute('''UPDATE Password SET password = ? WHERE username_id = ?''', (password, username_id))
                    self.conn.commit()
                else:
                    self.cur.execute('''INSERT OR REPLACE INTO Password (username_id, password) VALUES (?,?)''', (username_id, password))
                    self.conn.commit()
        else:
            self.cur.execute('SELECT id FROM Username WHERE username = ?',(username,))
            username_id=self.cur.fetchone()[0]
            self.cur.execute('''INSERT OR REPLACE INTO Password (username_id, password) VALUES (?,?)''', (username_id, password))
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
    
    def retrieveUsers(self, prn=True):
        self.cur.execute('SELECT * FROM Username')
        selected = self.cur.fetchall()
        if not selected:
            return 'No entries found.'
        elif selected is not None and prn == True:
            for id_,username in selected:
                print 'id: '+str(id_)+' Username: '+str(username)
        elif selected is not None and prn == False:
            return selected
        else:
            return None
    
    def retrievePasswords(self, prn=True):
        self.cur.execute('SELECT * FROM Password')
        selected = self.cur.fetchall()
        if not selected:
            return 'No entries found.'
        elif selected is not None and prn == True:
            for id_,password in selected:
                print 'id: '+str(id_)+' password: '+str(password)
        elif selected is not None and prn == False:
            return selected
    
    def retrieveAll(self, prn=True):
        self.cur.execute('SELECT Username.username, Password.password FROM Username INNER JOIN Password ON Username.id = Password.username_id')
        selected = self.cur.fetchall()
        if not selected:
            if self.retrieveUsers(False) != None and prn == True:
                return self.retrieveUsers()
            elif self.retrieveUsers(False) != None and prn == False:
                return self.retrieveUsers(False)
            else:
                return 'You have users without passwords.'
        elif selected is not None and prn == True:
            for name,password in selected:
                print 'Username: '+str(name)+', password: '+str(password)
        elif selected is not None and prn == False:
            return selected
        else:
            return None
        
    def deleteUser(self, username):
        self.cur.execute('SELECT id FROM Username WHERE username = ?',(username,))
        test=self.cur.fetchone()
        if test is not None:
            username_id=test[0]
            self.cur.execute('DELETE FROM Username WHERE username = ?',(username,))
            self.conn.commit()
            self.cur.execute('DELETE FROM Password WHERE username_id = ?',(username_id,))
            self.conn.commit()
        else:
            print 'No such user in database.'
        
    def cleanDatabase(self):
        self.cur.executescript('''
        DELETE FROM Username; 
        DELETE FROM Password;
        VACUUM;''')
        self.conn.commit()
        
    #def makeCSV(self,filename):
        
    def makeTxt(self, filename):
        with open(filename, 'w') as f_out:
            f_out.write(str(self.retrieveAll(False)))
    
    def closeConnection(self):
        self.conn.commit()
