# coding: utf8
import sys
print sys.getdefaultencoding()
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
