import os
import ftplib
from datetime import datetime
from django.conf import settings

class AAAIMXStorage():
    def __init__(self):
        self.user = settings.FTP_USER
        self.password = settings.FTP_PASS
        self.session = None

    def login(self):
        self.session = ftplib.FTP('ftp.aaaimx.org', self.user, self.password)

    def save(self, file, folder, filename):
        try:
            self.session.storbinary('STOR %s/%s' % (folder, filename), file)
        except Exception as err:
            print(err)
            if 'No such file or directory' in str(err):
                self.session.mkd(folder)
                self.session.storbinary('STOR %s/%s' %
                                        (folder, filename), file)

    def remove(self, folder, filename):
        self.session.cwd(folder)
        self.session.delete(filename)

    def list(self, path):
        return self.session.nlst(path)

    def exit(self):
        self.session.quit()