import socket
import smtplib
import re
import time
import dns.resolver
import threading as thread
import pandas as pd


class validation:
    def __init__(self,email=None,verify=False,check_mx=False):
        self.Email = email
        self.Verify = verify
        self.Check_mx = check_mx

       #if self.Verify:
        #    self.Verify_email(self.Email,self.MX(self.Email))
        #if self.Check_mx:
        #    self.MX(self.Email)

    def Format_pass(self,email):
        addressToVerify =email
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
        if match == None:
                raise ValueError('Bad Syntax')
        else:
            return True

    def MX(self,email):
        domain = str(email).split("@")[-1]
        records = dns.resolver.query(domain, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)
        return mxRecord

    def Verify_email(self,email,mxRecord):
        host = socket.gethostname()
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        server.connect(mxRecord)
        server.helo(host)
        server.mail(email)
        code, message = server.rcpt(str(email))
        server.quit()
        return email,code

    def Status(self,email):
        email,code = (self.Verify_email(email,self.MX(email)))
        if code == 250:
            return "ok"
        else:
            return "invalid"
        # Assume 250 as Success
        #if code == 250:
         #       return email
        #
        #else:
        #        pass
def main():
    v=validation()
    print(v.Status("ahsabbir@gmail.com"))
    
if __name__=='__main__':
    main()
