import unittest

from students import verifier_nom


class TestVerifierNom(unittest.TestCase):
    def test_nom_valide(self):
        resultat = verifier_nom("Dupont")
        self.assertTrue(resultat)

    def test_nom_vide_refuse(self):
        with self.assertRaises(ValueError):
            verifier_nom("")

    def test_nom_espaces_refuse(self):
        with self.assertRaises(ValueError):
            verifier_nom("   ")

    def test_nom_absent_refuse(self):
        with self.assertRaises(ValueError):
            verifier_nom(None)


if __name__ == "__main__":
    unittest.main()