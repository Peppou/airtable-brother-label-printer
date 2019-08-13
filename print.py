import os
import time
import brother_ql

from brother_ql.devicedependent import models, label_type_specs, label_sizes
from brother_ql import BrotherQLRaster, create_label

# TODO: Get the printer USB address without hard-coding.
os.environ["BROTHER_QL_PRINTER"] = "usb://0x04f9:0x2042"
os.environ["BROTHER_QL_MODEL"] = "QL-700"

qlr = BrotherQLRaster("QL-700")
create_label(qlr, 'testimage-29.png', "29", cut=True)
