import unittest

from file import File


class TestFile(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.file = File()

    @classmethod
    def tearDownClass(self):
        self.file.name = ""

    def setUp(self):
        self.file.name = "teste.txt"
        self.file.create()
    
    def tearDown(self):
        self.file.delete()

    def test_create_a_file(self):
        created = self.file.wasCreate()
        self.assertEqual(created, True)

    def test_create_a_existing_file(self):
        with self.assertRaises(FileExistsError):
            self.file.create()

    def test_change_file_name(self):
        text = "Teste 1"
        self.file.write(text)
        self.file.name = "changing_file_name.txt"
        readed = self.file.read()
        self.assertEqual(readed, "Teste 1\n")

    def test_read_a_file(self):
        text = ["Linha 1", "Linha 2", "Linha 3"]
        self.file.write(text)
        readed = self.file.read()
        self.assertEqual(readed, "Linha 1\nLinha 2\nLinha 3\n")

    def test_overwrite_file(self):
        text = "Teste 1"
        self.file.write(text)
        text = "Teste 2"
        self.file.write(text)
        readed = self.file.read()
        self.assertEqual(readed, "Teste 2\n")

    def test_append_to_file(self):
        text = "Linha 1"
        self.file.write(text)
        text = "Linha 2"
        self.file.append(text)
        readed = self.file.read()
        self.assertEqual(readed, "Linha 1\nLinha 2\n")

    def test_name_with_wrong_type(self):
        with self.assertRaises(TypeError):
            self.file.name = 2
    
    def test_empty_name(self):
        self.file.name = ""
        name = self.file.name
        self.assertEqual(name, "")