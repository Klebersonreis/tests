import unittest 

#definindo a classe Calc
class Calc():
    #funcao dobro
    def dobro(self, num):
        #retorna o valor de num e multiplica por 2
        return num * 2
#definindoa a classe MyCalcTest

class MyCalcTest(unittest.TestCase):
    #funcao testDobro
    def testDobro(self):
        #chamada para a class Calc
        obj = Calc()
        #parametro para a chamada  da funcao --self--
        self.assertEqual(16, obj.dobro(8))



if __name__ == '__main__':
    unittest.main()