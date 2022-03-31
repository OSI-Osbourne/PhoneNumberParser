from qtpy import uic
import sys
import os

path = os.path.dirname(os.path.abspath(sys.argv[0])) + os.sep + "ui"
uic.compileUi(path)