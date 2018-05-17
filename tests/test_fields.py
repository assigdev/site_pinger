import unittest
from site_pinger.core.fields import CharField, EmailField, IntField, UrlField, XmlUriField, ChoiceField
from .utils import cases


class FieldsTestCase(unittest.TestCase):
    @cases([
        (True, None, IntField, ['is require']),
        (True, '', CharField, ['is require']),
        (True, 0, IntField, []),
        (True, 1, IntField, []),
        (False, None, IntField, []),
    ])
    def test_require(self, case):
        required, value, cls, error = case
        field = cls(required=required)
        field.set_value(value)
        field.validate()
        self.assertEqual(field.errors, error)

    @cases([
        (0, []),
        (10, []),
        (-10, []),
        ('string', ['is not integer']),
        ([], ['is not integer']),
    ])
    def test_int(self, case):
        value, error = case
        field = IntField()
        field.set_value(value)
        field.validate()
        self.assertEqual(field.errors, error)

    @cases([
        ('string', []),
        ('''many textes''', []),
        (-10, ['is not string']),
        (0, ['is not string']),
        ([], ['is not string']),
    ])
    def test_char(self, case):
        value, error = case
        field = CharField()
        field.set_value(value)
        field.validate()
        self.assertEqual(field.errors, error)

    @cases([
        ('sitemap.xml', []),
        ('string', ['is not xml']),
        ('''many textes''', ['is not xml']),
        (-10, ['is not string']),
        (0, ['is not string']),
        ([], ['is not string']),
    ])
    def test_xml_url(self, case):
        value, error = case
        field = XmlUriField()
        field.set_value(value)
        field.validate()
        self.assertEqual(field.errors, error)

    @cases([
        ('assigdev@gmail.com', []),
        ('assigdev@gmail', ['bad email']),
        ('sitemap@', ['bad email']),
        ('string', ['bad email']),
        ('''many textes''', ['bad email']),
        (-10, ['is not string']),
        (0, ['is not string']),
        ([], ['is not string']),
    ])
    def test_email(self, case):
        value, error = case
        field = EmailField()
        field.set_value(value)
        field.validate()
        self.assertEqual(field.errors, error)

    @cases([
        ('http://assig.ru', []),
        ('https://163.172.172.108', []),
        ('http://course.assig.ru', []),
        ('assigdev@gmail', ['bad url']),
        ('sitemap@', ['bad url']),
        ('string', ['bad url']),
        ('''many textes''', ['bad url']),
        (-10, ['is not string']),
        (0, ['is not string']),
        ([], ['is not string']),
    ])
    def test_url(self, case):
        value, error = case
        field = UrlField()
        field.set_value(value)
        field.validate()
        self.assertEqual(field.errors, error)

    @cases([
        ('wrong', False),
        ([], False),
        (1, False),
        ('sitemap', True),
        ('urls', True),
    ])
    def test_url(self, case):
        value, error = case
        field = ChoiceField(choices=['sitemap', 'urls'])
        field.set_value(value)
        field.validate()
        self.assertEqual(len(field.errors) == 0, error)
