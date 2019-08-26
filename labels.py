import pprint

from PIL import Image, ImageDraw

import constants as c


def create_base_img():
    '''Creates a base image of the correct label size for a liquid container and
    with the logo in corner.'''

    img = Image.new('RGB', (c.LABEL_WIDTH, c.LABEL_HEIGHT),
                    color=(255, 255, 255))
    img.paste(c.LOGO, (c.LABEL_WIDTH-c.LOGO_WIDTH,
                       c.LABEL_HEIGHT-c.LOGO_HEIGHT))
    return img


def create_stock(record, font):
    '''Creates a label for a record in the 'Stock' table. Takes an
    Airtable record from this table and a font.'''
    fields = record['fields']
    img = create_base_img()
    d = ImageDraw.Draw(img)

    xOffset = 0
    yOffset = 0
    d.text((xOffset, yOffset),                   'ID:       ' + default_if_none(fields.get('Reagent ID (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + c.LINE_HEIGHT),   'Type:     ' + default_if_none(fields.get('Type'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 2*c.LINE_HEIGHT), 'Desc:     ' + default_if_none(fields.get('Description (Optional)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 3*c.LINE_HEIGHT), 'Expiry:   ' + default_if_none(fields.get('Date of Expiry'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 4*c.LINE_HEIGHT), 'Storage:  ' + first_or_default(fields.get('Storage conditions (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 5*c.LINE_HEIGHT), 'Supplier: ' + default_if_none(fields.get('Supplier'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8

    return img


def create_aliquot(record, font):
    '''Creates a label image for a record in the 'Aliquots' table. Takes an
    Airtable record from this table and a font.'''
    fields = record['fields']
    img = create_base_img()
    d = ImageDraw.Draw(img)

    # pp = pprint.PrettyPrinter(indent=2)
    # pp.pprint(fields)
    # sys.exit(0)

    xOffset = 0
    yOffset = 0
    d.text((xOffset, yOffset),                   'ID:       ' + default_if_none(fields.get('Aliquot ID (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + c.LINE_HEIGHT),   'Type:     ' + first_or_default(fields.get('Type (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 2*c.LINE_HEIGHT), 'Desc:     ' + first_or_default(fields.get('Description (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 3*c.LINE_HEIGHT), 'Expiry:   ' + first_or_default(fields.get('Date of Expiry (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 4*c.LINE_HEIGHT), 'Storage:  ' + first_or_default(fields.get('Storage conditions (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 5*c.LINE_HEIGHT), 'Supplier: ' + first_or_default(fields.get('Supplier (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8

    return img


def create_mix(record, font):
    '''Creates a label image for a record in the 'Mixes' table. Takes an
    Airtable record from this table and a font.'''

    fields = record['fields']
    img = create_base_img()
    d = ImageDraw.Draw(img)

    xOffset = 0
    yOffset = 0
    d.text((xOffset, yOffset),                   'ID:      ' + default_if_none(fields.get('Mix ID (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + c.LINE_HEIGHT),   'Type:    ' + default_if_none(fields.get('Type'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 2*c.LINE_HEIGHT), 'Desc:    ' + default_if_none(fields.get('Description (Optional)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 3*c.LINE_HEIGHT), 'Expiry:  ' + default_if_none(fields.get('Date of Expiry (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 4*c.LINE_HEIGHT), 'Storage: ' + first_or_default(fields.get('Storage conditions (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8

    return img


def create_storage(record, font):
    '''Creates a label image for a record in the 'Storages' table. Takes an
    Airtable record from this table and a font.'''

    fields = record['fields']

    img = Image.new('RGB', (c.LABEL_WIDTH_STORAGE,
                            c.LABEL_HEIGHT), color=(255, 255, 255))
    img.paste(c.LOGO, (c.LABEL_WIDTH_STORAGE-c.LOGO_WIDTH,
                       c.LABEL_HEIGHT-c.LOGO_HEIGHT))

    d = ImageDraw.Draw(img)

    xOffset = 0
    yOffset = 0
    d.text((xOffset, yOffset),                   'ID:   ' + default_if_none(fields.get('Storage ID (Auto field)'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + c.LINE_HEIGHT),   'Desc: ' + default_if_none(fields.get('Description'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 2*c.LINE_HEIGHT), 'Lab:  ' + default_if_none(fields.get('Lab'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 3*c.LINE_HEIGHT), 'Cond: ' + default_if_none(fields.get('Condition comments'), ''), font=c.FONT, fill=(0, 0, 0))  # nopep8

    return img

def default_if_none(val, default):
    # Returns default value if val is None
    return val if val is not None else default

def first_or_default(listArg, default):
    # Returns first element of list if given argument is a list and of length
    # one or more, the default value otherwise
    if isinstance(listArg, list) and len(listArg) > 0:
        return listArg[0]
    else:
        return default
