# TODO: Removed unused imports
import pprint
import os
import sys
import time

import brother_ql
from airtable import Airtable

from PIL import Image, ImageDraw, ImageFont

# TODO: Improve error handling.
# TODO: Add VOW logo to labels.

PROJECT_NAME='airtable-brother-label-printer'
TEMP_DIR='/tmp/' + PROJECT_NAME

AIRTABLE_QUEUE_VIEW='Label print queue'
AIRTABLE_PRINTED_COL='Label printed? (Auto field)'

PRINTER_ADDR = 'usb://0x04f9:0x2042' # TODO: Get the printer USB address without hard-coding.
PRINTER_MODEL = 'QL-700'
PRINTER_LABEL_ROLL_SIZE = '29'

FONT_SIZE=32
FONT=ImageFont.truetype('./assets/monofonto.ttf', FONT_SIZE)
LINE_HEIGHT=50

LABEL_HEIGHT=306 # height: max for 29mm size Brother printer label
LABEL_WIDTH=493  # width: chosen to comfortably fit on most lab containers

# create_label_stock takes an Airtable record from the 'Stock' table and a font,
# and returns a PIL image of a label.
def create_label_stock(record, font):
  label = Image.new('RGB', (493, 306), color = (255, 255, 255))
  d = ImageDraw.Draw(label)

  xOffset=0
  yOffset=10
  d.text((xOffset, yOffset),                 'ID:       ' + fields['Reagent ID (Auto field)'], font=FONT, fill=(0,0,0))
  d.text((xOffset, yOffset + LINE_HEIGHT),   'Type:     ' + fields['Type'], font=FONT, fill=(0,0,0))
  d.text((xOffset, yOffset + 2*LINE_HEIGHT), 'Desc:     ' + fields['Description (Optional)'], font=FONT, fill=(0,0,0))
  d.text((xOffset, yOffset + 3*LINE_HEIGHT), 'Expiry:   ' + fields['Date of Expiry'], font=FONT, fill=(0,0,0))
  d.text((xOffset, yOffset + 4*LINE_HEIGHT), 'Storage:  ' + fields['Storage conditions (Auto field)'][0], font=FONT, fill=(0,0,0))
  d.text((xOffset, yOffset + 5*LINE_HEIGHT), 'Supplier: ' + fields['Supplier'], font=FONT, fill=(0,0,0))

  return label


# Ensure required envvars have been provided.
if os.environ.get('AIRTABLE_API_KEY') == None:
  sys.exit("ERROR: Please provide AIRTABLE_API_KEY as env var.");
if os.environ.get('AIRTABLE_BASE_ID') == None:
  sys.exit("ERROR: Please provide AIRTABLE_BASE_ID as env var.");

# Create temporary directory if it doesn't exist
os.system('mkdir -p ' + TEMP_DIR)
print('Temporary directory created at ' + TEMP_DIR)

labels = []         # Label images to be printed
record_ids = []    # Airtable record IDs that have been printed

# TODO: Handle all Airtable tables: currently just 'Stock'
# Create labels for table 'Stock'
airtable = Airtable(os.environ['AIRTABLE_BASE_ID'], 'Stock')
records = airtable.get_all(view=AIRTABLE_QUEUE_VIEW, maxRecords=10)
for record in records:
  fields = record['fields']
  labels.append(create_label_stock(record, FONT))
  record_ids.append(record['id'])

print('Data pulled from Airtable and label images created: ' + str(len(labels)) + ' total records')

if len(labels) == 0:
  print('No records to print, exiting ...')
  sys.exit(0)

# Print labels
for label in labels:
  # Rotate image 90 degrees since printer requires image width along 29mm side
  # (roll width) and image height along limitless side (roll length).
  label = label.rotate(90, expand=1)

  # Save image to temp directory
  label_path = TEMP_DIR + '/label-%s.png' % (int(time.time()))
  label.save(label_path)

  # UNCOMMENT for debugging purposes
  # Shows label image in viewer. Uncomment line for the relevant OS.
  # os.system('open %s' % (label_path))          # macOS
  # os.system('gpicview %s' % (label_path))      # Linux (requires gpicview)

  # Send print job
  # The if-else waits for and catches errors in the asynchronous system call.
  if os.system('brother_ql --backend pyusb --printer %s --model %s print -l %s %s' % (PRINTER_ADDR, PRINTER_MODEL, PRINTER_LABEL_ROLL_SIZE, label_path)) == 0:
    continue
  else:
    sys.exit('ERROR: Could not print label.')

print('Labels sent to Brother printer')
  

# Update records in Airtable as printed
for id in record_ids:
  airtable.update(id, {AIRTABLE_PRINTED_COL: True})

print('Airtable: Printed rows updated to "' + AIRTABLE_PRINTED_COL + '=true"')

# Delete temporary directory
os.system('rm -Rf ' + TEMP_DIR)

print ('Temporary directory deleted.')
print ('Success! Print batch successfully completed')
  