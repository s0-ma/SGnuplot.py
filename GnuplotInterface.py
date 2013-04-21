# -*- coding:utf-8 -*-

import subprocess
import os

class GnuplotInterface.py:

    def __init__(self):
            self.gnuplot_command = "gnuplot"
            self.proc = subprocess.Popen([self.gnuplot_command,], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def write(self,cmd):
            cmd += "\n"
            self.proc.stdin.write(cmd)

    def read(self):
            return os.read(self.proc.stdout.fileno(),1024)

    def close_window(self):
            self.proc.kill()

