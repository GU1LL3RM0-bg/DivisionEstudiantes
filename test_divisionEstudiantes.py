import unittest
from divisionEstudiantes import Code

class TestDivisionEstudiantes(unittest.TestCase):

    def test_AleatoriedadEstudiantes(self):

        est_prueba = ["Juan","Pedro", "Maria", "Jose",
         "Raul", "Francisco", "Laura", "Gabriela", "Fernando","Pepe"]
        grupos = 5

        for g in range(grupos):
            for e in est_prueba:
                contador = 0
                for i in range(1000):
                    gruposfinales = Code(est_prueba,[],grupos)
                    if e in gruposfinales[g].members:
                        contador = contador + 1
                errorPorcentual = abs(contador - 200)/200 * 100
                self.assertTrue(errorPorcentual < 20)

    def test_AleatoriedadTemas(self):

        temas_prueba = ["tema1","tema2", "tema3", "tema4",
         "tema5", "tema6", "tema7", "tema8", "tema9","tema10","tema11"]
        grupos = 5

        for g in range(grupos):
            for t in temas_prueba:
                contador = 0
                for i in range(1000):
                    gruposfinales = Code([],temas_prueba,grupos)
                    if t in gruposfinales[g].topics:
                        contador = contador + 1
                errorPorcentual = abs(contador - 200)/200 * 100
                self.assertTrue(errorPorcentual < 20)
