from PIL import Image, ImageFont

import labels

PROJECT_NAME = 'airtable-brother-label-printer'
TEMP_DIR = '/tmp/' + PROJECT_NAME

AIRTABLE_QUEUE_VIEW = 'Label print queue'
AIRTABLE_PRINTED_COL = 'Label printed? (Auto field)'

# A mapping of Airtable table names to their label create functions. A new table
# can be added by adding it here and adding its label create function to
# labels.py
AIRTABLE_TABLE_FUNCTIONS = {
    'Stock': labels.create_stock,
    'Aliquots': labels.create_aliquot,
    'Mixes': labels.create_mix,
    'Storages (Admin)': labels.create_storage,
}

PRINTER_ADDR = 'usb://0x04f9:0x2042'
PRINTER_MODEL = 'QL-700'
PRINTER_LABEL_ROLL_SIZE = '29'

FONT_SIZE = 32
FONT = ImageFont.truetype('./assets/monofonto.ttf', FONT_SIZE)
LINE_HEIGHT = 36
LOGO = Image.open('./assets/logo.png')

# Height: max for 29mm size Brother printer label
LABEL_HEIGHT = 306
# Width: chosen to comfortably fit on most lab containers
# Note: width for Storages is intentionally longer since storage containers are
# typically larger (e.g. a fridge vs a test tube).
LABEL_WIDTH = 493
LABEL_WIDTH_STORAGE = 750
LOGO_HEIGHT = 72
LOGO_WIDTH = 72
