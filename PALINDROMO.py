##def mostrar_indices(unstrig):
 ###  for indice in range(len(unstrig)):
  ####     print( stg(indice)+"->"+ print() )

import unittest

def is_palindrome(mystring):
    for indice in range(len(mystring)):
        print(mystring[indice]+"-->"mystring[-(indice+1)])


class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome("a")
        self.assertEqual(resultado,True)

    def test_aa(self):
        resultado = is_palindrome("aa")
        self.assertEqual(resultado,True)

    def test_ab(self):
       resultado = is_palindrome("ab")
       self.assertEqual(resultado,False)

    def test_aCa(self):
       resultado = is_palindrome("aCa")
       self.assertEqual(resultado,True)

    def test_aCs(self):
        resultado = is_palindrome("aCs")
        self.assertEqual(resultado,False)

    def test_ABBA(self):
       resultado = is_palindrome("ABBA")
       self.assertEqual(resultado,False)           

    def test_ABCA(self):
       resultado = is_palindrome("ABCA")
       self.assertEqual(resultado,False)

    def test_ABBCA(self):
       resultado = is_palindrome("ABBCA")
       self.assertEqual(resultado,False)     

unittest.main()

 