import os
import sys
import time

import brother_ql
from airtable import Airtable

import constants as c
import labels


# Ensure required envvars have been provided.
if os.environ.get('AIRTABLE_API_KEY') == None:
    sys.exit("ERROR: Please provide AIRTABLE_API_KEY as env var.")
if os.environ.get('AIRTABLE_BASE_ID') == None:
    sys.exit("ERROR: Please provide AIRTABLE_BASE_ID as env var.")

label_images = []         # Label images to be printed
record_ids = []    # Airtable record IDs that have been printed

for table in c.AIRTABLE_TABLE_FUNCTIONS:
    label_create_function = c.AIRTABLE_TABLE_FUNCTIONS[table]
    airtable = Airtable(os.environ['AIRTABLE_BASE_ID'], table)
    records = airtable.get_all(view=c.AIRTABLE_QUEUE_VIEW, maxRecords=10)
    for record in records:
        label_images.append(label_create_function(record, c.FONT))
        record_ids.append(record['id'])

print('Data pulled from Airtable and label images created: ' +
      str(len(label_images)) + ' total records')

if len(label_images) == 0:
    print('No records to print, exiting ...')
    sys.exit(0)

# Create temporary directory if it doesn't exist
os.system('mkdir -p ' + c.TEMP_DIR)
print('Temporary directory created at ' + c.TEMP_DIR)

# Print labels
for label in label_images:
    # DEBUG: Uncomment for helpful debugging purposes.
    # Shows label image in viewer. Uncomment line for the relevant OS.
    # os.system('open %s' % (label_path))          # macOS
    # os.system('gpicview %s' % (label_path))      # Linux (requires gpicview)

    # Rotate image 90 degrees since printer requires image width along 29mm side
    # (roll width) and image height along limitless side (roll length).
    label = label.rotate(90, expand=1)

    # Save image to temp directory
    label_path = c.TEMP_DIR + '/label-%s.png' % (int(time.time()))
    label.save(label_path)

    # Send print job to Brother printer
    # The if-else awaits and catches errors in the asynchronous system call
    if os.system('brother_ql --backend pyusb --printer %s --model %s print -l %s %s' % (c.PRINTER_ADDR, c.PRINTER_MODEL, c.PRINTER_LABEL_ROLL_SIZE, label_path)) == 0:
        continue
    else:
        sys.exit('ERROR: Could not print label.')

print('Labels sent to Brother printer')

# Update records in Airtable as printed
for id in record_ids:
    airtable.update(id, {c.AIRTABLE_PRINTED_COL: True})

print('Airtable: Printed rows updated to "' + c.AIRTABLE_PRINTED_COL + '=true"')

# Delete temporary directory
os.system('rm -Rf ' + c.TEMP_DIR)

print('Temporary directory deleted.')
print('Success! Print batch successfully completed')
