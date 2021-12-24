class CmdResponse:
    cmd=exec_time=id=out=None
    def set_cmd(self,cmd):
        self.cmd=cmd
    def set_exec_time(self,exe_time):
        self.exec_time=exe_time
    def set_id(self,id):
        self.id=id
    def set_out(self,out):
        self.out=out
    def get(self):
        return self.__dict__