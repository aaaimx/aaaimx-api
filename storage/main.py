import ftplib
from datetime import datetime
import os

class AAAIMXStorage():
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.session = None

    def login(self):
        self.session = ftplib.FTP('ftp.aaaimx.org', self.user, self.password)

    def save(self, file, path):
        self.session.storbinary('STOR ' + str(path), file)

    def create(self, folder):
        try:
            self.session.mkd(folder)
        except ftplib.error_perm:
            pass

    def list(self, path):
        return self.session.nlst(path) 

    def exit(self):
        self.session.quit()

USER = os.environ.get('USER')
PASS = os.environ.get('PASS')
file = open('./storage/file.png','rb')
ftp = AAAIMXStorage(USER, PASS)
ftp.login()
ftp.create('certificates/2020')
ftp.save(file, 'certificates/2020/file.png')
print(ftp.list('certificates/2019'))
file.close()   
