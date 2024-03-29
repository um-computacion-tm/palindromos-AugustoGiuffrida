import unittest

def is_palindrome(mystring):
    print(mystring + " --> " + mystring[::-1]) 
    for indice in range(len(mystring)):
        mystring = mystring.lower()
        mystring = mystring.replace("á","a")
        mystring = mystring.replace("é","e")
        mystring = mystring.replace("í","i")
        mystring = mystring.replace("ó","o")
        mystring = mystring.replace("ú","u")
        mystring = mystring.replace(" ","")  

        if mystring ==  mystring[::-1]:
            if indice ==0:
                print("La palabra",mystring," es palindromo")
                print(" ")
        else:
            print("La palabra",mystring," no es palindromo") 
            print(" ")
            return False   
     
    return True

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)

    def test_b(self):
        resultado = is_palindrome('B')
        self.assertEqual(resultado, True)

    def test_aa(self):
        resultado = is_palindrome('aa')
        self.assertEqual(resultado, True)

    def test_ab(self):
        resultado = is_palindrome('ab')
        self.assertEqual(resultado, False)

    def test_osO(self):
        resultado = is_palindrome('osO')
        self.assertEqual(resultado, True)

    def test_aNA(self):
        resultado = is_palindrome('aNA')
        self.assertEqual(resultado, True)        

    def test_aCs(self):
        resultado = is_palindrome('aCs')
        self.assertEqual(resultado, False)

    def test_ABBA(self):
        resultado = is_palindrome('ABBA')
        self.assertEqual(resultado, True)

    def test_ABCA(self):
        resultado = is_palindrome('BACB')
        self.assertEqual(resultado, False)

    def test_ABCBA(self):
        resultado = is_palindrome('ABCBA')
        self.assertEqual(resultado, True)

    def test_Casas(self):
        resultado = is_palindrome('Casas')
        self.assertEqual(resultado, False)    

    def test_ABCCBA(self):
        resultado = is_palindrome('ABCCBA')
        self.assertEqual(resultado, True)

    def test_ZBCCBA(self):
        resultado = is_palindrome('ZBCCBA')
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)

    def test_neUquén(self):
        resultado = is_palindrome('neUquén')
        self.assertEqual(resultado, True)

    def test_Aérea(self):
        resultado = is_palindrome('Aérea')
        self.assertEqual(resultado, True)

    def test_Ananá(self):
        resultado = is_palindrome('Ananá')
        self.assertEqual(resultado, True)    

    def test_neuqueM(self):
        resultado = is_palindrome('neuqueM')
        self.assertEqual(resultado, False)

    def test_neuquen(self):
        resultado = is_palindrome('S o M E t e M O s')
        self.assertEqual(resultado, True)

        

unittest.main()

 