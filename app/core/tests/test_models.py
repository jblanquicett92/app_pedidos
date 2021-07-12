
import unittest

class Test_Tipo_clienteView(unittest.TestCase):

    def test_len_tipo_cliente(self, text):

        self.assertEqual(True, len(text)<45)