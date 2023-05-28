import unittest 
import funciones

# Definimos classe para hacer testeo
class TestFunciones(unittest.TestCase):

#Test autoIncrement
    def test_autoIncrement(self):
        self.assertEqual(funciones.autoIncrement(100), 1)
        self.assertEqual(funciones.autoIncrement(10), 10)
        self.assertEqual(funciones.autoIncrement(20), 20)
        
        with self.assertRaises(ValueError):
            funciones.autoIncrement("texto")

#Test remainder
    def test_remainder(self):
        self.assertEqual(funciones.remainder(100,10),0)
        self.assertEqual(funciones.remainder(17,5),2)
        self.assertEqual(funciones.remainder(20,3),2)
        
        with self.assertRaises(ValueError):
            funciones.remainder(10,0)
            
#Test squarreRoot     
    def test_squarreRoot(self):
        self.assertEqual(funciones.squarreRoot(100),10)
        self.assertEqual(funciones.squarreRoot(4),2)
        self.assertEqual(funciones.squarreRoot(9),3)
        
        with self.assertRaises(ValueError):
            funciones.squarreRoot(-2)