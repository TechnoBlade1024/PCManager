import json
import os
import subprocess

from plyer import notification
from plyer.utils import platform
from win10toast import ToastNotifier
import traceback
from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from PCManager.PCM.wincmd.models import ExecutedCmd
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def executewincmd(request):
    if request.method =='POST':
        cmd=json.loads(request.body.decode('utf-8'))['cmd']
        try:
            if(isinstance(cmd,list)):
                cmdout_list=[]
                for cmds in cmd:
                    cmdout = subprocess.check_output(cmds, shell=True).decode('utf-8').replace('\r\n','')
                    cmdout_list.append(cmdout.decode('utf-8'))
                    exec_cmd_obj = ExecutedCmd()
                    exec_cmd_obj.cmd = cmds
                    exec_cmd_obj.out = cmdout
                    exec_cmd_obj.save()
                    toaster = ToastNotifier()
                    toaster.show_toast("PCManager",
                                       cmdout,duration=1)
                return HttpResponse(str(cmdout_list))
            else:
                cmdout=subprocess.check_output(cmd,shell=True)
                exec_cmd_obj=ExecutedCmd()
                exec_cmd_obj.cmd=cmd
                exec_cmd_obj.out = cmdout.decode('utf-8').replace('\r\n','')
                exec_cmd_obj.save()
                return HttpResponse(str(cmdout.decode('utf-8')))
        except:
            traceback.print_exc()
            return HttpResponse('Fail')
    else:
        from PCManager.PCM.wincmd.Data.Response.CmdResponse import CmdResponse
        data=ExecutedCmd.objects.all()
        data_list=[]
        for record in data:
            cmdresp=CmdResponse()
            cmdresp.set_cmd(record.cmd)
            cmdresp.set_exec_time(record.exec_time)
            # cmdresp.set_id(record._id)
            cmdresp.set_out(record.out)
            data_list.append(cmdresp.get())
        return JsonResponse(data_list,safe=False)
def dictdefault(data):
    if isinstance(data,datetime):
        return str(data)

def
