# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:06:38 2019

@author: lars-johan.brannmark
"""

import calendar
import sys

yyyy = sys.argv[1]
mm = sys.argv[2]
dd = sys.argv[3]

weekday = calendar.day_name[calendar.weekday(int(yyyy),int(mm),int(dd))]

print 'The weekday of the date %s-%s-%s is: %s' %(yyyy,mm,dd,weekday)