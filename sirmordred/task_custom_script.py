#!/usr/bin/env python3

import logging
import time

from sirmordred.task import Task
from typing import Any

logger = logging.getLogger(__name__)

class TaskCustomScript(Task):

#  def __init__(self,config, backend_section=None):
#     super().__init__(config)
#     self.backend_section = backend_section

   def execute(self):
      cfg = self.config

      exec(open(cfg['custom_script']['scriptsource']).read(),self.create_script_args())

   def create_script_args(self) -> dict:
      argdict = {}
      args = self.config['custom_script']['scriptargs']
      for i in range(0,len(args)):
         argdict['arg'+str(i+1)] = args[i]
      return argdict


