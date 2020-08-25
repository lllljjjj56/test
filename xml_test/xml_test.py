try:
    from xml_test.file_operator import XMLOperator
except Exception as e:
    pass


def run():
    xml_instance = XMLOperator('displays_template.xml')
    root = xml_instance.get_root()
    print(root.tag)
    print(root.find('property').attrib)
    for i in xml_instance.find_nodes('property/property/property'):
        print(i.attrib)
        print(i.tail)


if __name__ == '__main__':
    from file_operator import XMLOperator
    run()
