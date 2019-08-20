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
    d.text((xOffset, yOffset),                   'ID:       ' + fields['Reagent ID (Auto field)'], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + c.LINE_HEIGHT),   'Type:     ' + fields['Type'], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 2*c.LINE_HEIGHT), 'Desc:     ' + fields['Description (Optional)'], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 3*c.LINE_HEIGHT), 'Expiry:   ' + fields['Date of Expiry'], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 4*c.LINE_HEIGHT), 'Storage:  ' + fields['Storage conditions (Auto field)'][0], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 5*c.LINE_HEIGHT), 'Supplier: ' + fields['Supplier'], font=c.FONT, fill=(0, 0, 0))  # nopep8

    return img


def create_aliquot(record, font):
    '''Creates a label image for a record in the 'Aliquots' table. Takes an
    Airtable record from this table and a font.'''
    fields = record['fields']
    img = create_base_img()
    d = ImageDraw.Draw(img)

    xOffset = 0
    yOffset = 0
    d.text((xOffset, yOffset),                   'ID:       ' + fields['Aliquot ID (Auto field)'], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + c.LINE_HEIGHT),   'Type:     ' + fields['Type (Auto field)'][0], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 2*c.LINE_HEIGHT), 'Desc:     ' + fields['Description (Auto field)'][0], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 3*c.LINE_HEIGHT), 'Expiry:   ' + fields['Date of Expiry (Auto field)'][0], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 4*c.LINE_HEIGHT), 'Storage:  ' + fields['Storage conditions (Auto field)'][0], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 5*c.LINE_HEIGHT), 'Supplier: ' + fields['Supplier (Auto field)'][0], font=c.FONT, fill=(0, 0, 0))  # nopep8

    return img


def create_mix(record, font):
    '''Creates a label image for a record in the 'Mixes' table. Takes an
    Airtable record from this table and a font.'''

    fields = record['fields']
    img = create_base_img()
    d = ImageDraw.Draw(img)

    xOffset = 0
    yOffset = 0
    d.text((xOffset, yOffset),                   'ID:      ' + fields['Mix ID (Auto field)'], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + c.LINE_HEIGHT),   'Type:    ' + fields['Type'], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 2*c.LINE_HEIGHT), 'Desc:    ' + fields['Description (Optional)'], font=c.FONT, fill=(0, 0, 0))  # nopep8
    # TODO: Need to define what "Expiry" means for mixes to add this field to Mixes labels.
    # d.text((xOffset, yOffset + 3*c.LINE_HEIGHT), 'Expiry:   ' + fields['Date of Expiry (Auto field)'][0], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 4*c.LINE_HEIGHT), 'Storage: ' + fields['Storage conditions (Auto field)'][0], font=c.FONT, fill=(0, 0, 0))  # nopep8

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
    d.text((xOffset, yOffset),                   'ID:   ' + fields['Storage ID (Auto field)'], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + c.LINE_HEIGHT),   'Desc: ' + fields['Description'], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 2*c.LINE_HEIGHT), 'Lab:  ' + fields['Lab'], font=c.FONT, fill=(0, 0, 0))  # nopep8
    d.text((xOffset, yOffset + 3*c.LINE_HEIGHT), 'Cond: ' + fields['Condition comments'], font=c.FONT, fill=(0, 0, 0))  # nopep8

    return img
