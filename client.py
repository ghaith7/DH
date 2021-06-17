


class Client:
    def __init__(self,login):
        
        self.login=login
        self.public_key,self.private_key = self.genParams()

    def genParams(self):
        #generate keys with d
        pbk=0
        prk=0
        return pbk,prk