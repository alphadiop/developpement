class MyImpoter(BaseImpoter):
  class Meta:
    config_file = 'import_test.json'
    model = Contact
    delimiter = ','
    ignore_first_line = True