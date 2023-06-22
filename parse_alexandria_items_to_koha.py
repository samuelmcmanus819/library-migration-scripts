from pymarc import MARCReader, Record, Field, Subfield

record_types=[]

def parse_record(record):
    title_field = record.get_fields('245')
    record_type = title_field[0].get('h')
    if "[" in record_type:
        record_type = record_type[1:-1]
    if record_type == "paperback" or record_type == "big book" or record_type == "great books" or record_type == "boardbook" or record_type == "hardback" or record_type == "text large print" or record_type == "signed by author" or record_type == "wall chart" or record_type == "oprah book" or record_type == "manipulative":
        record_type = "book"
    elif record_type == "ringed notebook":
        record_type = "notebook"
    elif record_type == "audio book":
        record_type = "Audiobook"
    elif record_type == "spanish video" or record_type == "child video":
        record_type = "video"
    elif record_type == "audio cd":
        record_type = "CD"
    elif record_type == "hot spot":
        record_type = "hotspot"

    if record_type not in record_types:
        record_types.append(record_type)
        print(record_type)

    custom_fields = record.get_fields('852')
    for custom_field in custom_fields:
        barcode = custom_field.get('p')
        call_number = custom_field.get('h')
        cost = custom_field.get('9')
        copy_tag = custom_field.get('t')
        record.add_field(
            Field(
                tag = '952',
                indicators = ['0', '1'],
                subfields = [
                    Subfield(code='a', value='NEWW'),
                    Subfield(code='b', value='NEWW'),
                    Subfield(code='p', value=barcode),
                    Subfield(code='o', value=call_number),
                    Subfield(code='g', value=cost),
                    Subfield(code='t', value=copy_tag),
                    Subfield(code='y', value=record_type)
                ]
            )
        )
    return record

                        



with open('items.marc', 'rb') as reader:
    with open('items_parsed.marc', 'wb') as writer:
        reader = MARCReader(reader)
        record = next(reader)
        while True:
            try:
                record = parse_record(record)
                writer.write(record.as_marc())
                record = next(reader)
            except:
                break
