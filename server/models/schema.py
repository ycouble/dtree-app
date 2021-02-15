from schema import SchemaError

def is_valid(conf_schema, conf):
    try:
        conf_schema.validate(conf)
        return True
    except SchemaError as err:
        print(err)
        return False