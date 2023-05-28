import unittest 
import funciones

# Definimos classe para hacer testeo

class TestFunciones(unittest.TestCase):
    
    def setUp(self):
        print("setUp")
    
    def tearDown(self):
        print("TearDown")
        
    def test_suma(self):
        self.assertEqual(funciones.sumar(10,20),30)
        self.assertEqual(funciones.sumar(10,20),20)
        self.assertEqual(funciones.sumar(10,10),20)
        
        with self.assertRaises(ValueError):
            funciones.sumar(10,0)

