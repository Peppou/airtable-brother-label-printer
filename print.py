import os
import time
import brother_ql

from brother_ql.devicedependent import models, label_type_specs, label_sizes
from brother_ql import BrotherQLRaster, create_label

os.environ["BROTHER_QL_PRINTER"] = "/dev/usb/lp0"
os.environ["BROTHER_QL_MODEL"] = "QL-700"

qlr = BrotherQLRaster("QL-700")
image_path = 'testimage-29.png'
create_label(qlr, image_path, "29", cut=True)
