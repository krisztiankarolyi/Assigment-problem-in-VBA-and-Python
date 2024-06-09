import numpy as np

from myfunctions import *
import unittest


class TestFeltolt0(unittest.TestCase):

    def test_kimenet(self):
        matrix = []
        feltolt0(matrix, 2, 3)
        self.assertEqual(matrix, [[0, 0, 0], [0, 0, 0]])

        matrix = []
        feltolt0(matrix, 3, 2)
        self.assertEqual(matrix, [[0, 0], [0, 0], [0, 0]])

    def test_type_n(self):
        matrix = []
        with self.assertRaises(TypeError):
            feltolt0(matrix, "2", 2)
        with self.assertRaises(TypeError):
            feltolt0(matrix, 2, "2")
        with self.assertRaises(TypeError):
            feltolt0(matrix, "alma", True)


class TestFeltoltBinarisMatrix(unittest.TestCase):

    def test_feltoltes(self):
        binarismatrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        eredmenytomb = [0., 1., - 0., 0., 0., -0., 0., 1., 0., 0.]
        feltolt_binarismatrix(2, 5, binarismatrix, eredmenytomb)
        self.assertEqual(binarismatrix, [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0]])


class TestSpaceMentesit(unittest.TestCase):

    def test_kimenet(self):
        self.assertEqual(space_mentesit("1 2 3 4"), "1234")
        self.assertEqual(space_mentesit("  1   2   3   4  "), "1234")


class TestFeltoltJegymatrix(unittest.TestCase):

    def test_feltolt(self):
        jegymatrix = []
        line = " 1 2 3 "
        feltolt_jegymatrix(jegymatrix, line)
        self.assertEqual(jegymatrix, [[1, 2, 3]])
        feltolt_jegymatrix(jegymatrix, line)
        self.assertEqual(jegymatrix, [[1, 2, 3], [1, 2, 3]])
        feltolt_jegymatrix(jegymatrix, line)
        self.assertEqual(jegymatrix, [[1, 2, 3], [1, 2, 3], [1, 2, 3]])


class TestConvert1D(unittest.TestCase):
    def test_kimenet(self):
        jegymatrix = [[4, 9, 8, 6, 5], [6, 4, 7, 4, 4]]
        eredmeny = [4, 9, 8, 6, 5, 6, 4, 7, 4, 4]
        self.assertEqual(convert_1D(jegymatrix), eredmeny)


class TestTranszponalas(unittest.TestCase):
    def test_kimenet(self):
        jegymatrix = [[8, 4, 5], [8, 7, 7], [4, 10, 6], [5, 8, 7]]
        eredemeny = [[8, 8, 4, 5], [4, 7, 10, 8], [5, 7, 6, 7]]
        self.assertEqual(transzponalas(jegymatrix), eredemeny)


class TestGeneralKfbe(unittest.TestCase):
    def test_hallgato_kisebb_mint_tetel(self):
        n = 2
        m = 3
        eredmeny = [[1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1]]
        self.assertEqual(general_kfbe(n, m), eredmeny)

    def test_hallgato_egyenlo_tetel2(self):
        n = 2
        m = 2
        eredmeny = [[1, 1, 0, 0], [0, 0, 1, 1],
                    [1, 0, 1, 0], [0, 1, 0, 1]]
        self.assertEqual(general_kfbe(n, m), eredmeny)

    def test_hallgato_egyenlo_tetel3(self):
        n = 3
        m = 3
        eredmeny = [[1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 1, 0, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 0, 1]]
        self.assertEqual(general_kfbe(n, m), eredmeny)

    def test_hallgato_nagyobb_mint_tetel(self):
        n = 4
        m = 3
        eredmeny = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]]
        self.assertEqual(general_kfbe(n, m), eredmeny)


class TestGeneralKfje(unittest.TestCase):
    def test_kimenet(self):
        self.assertEqual(general_kfje(2), [1, 1])
        self.assertEqual(general_kfje(3), [1, 1, 1])
        self.assertEqual(general_kfje(0), [])


class TestGeneralKfjeEgyenlo(unittest.TestCase):
    def test_kimenet(self):
        self.assertEqual(general_kfje_egyenlo(2), [1, 1, 1, 1])
        self.assertEqual(general_kfje_egyenlo(3), [1, 1, 1, 1, 1, 1])
        self.assertEqual(general_kfje_egyenlo(0), [])


class TestGeneralKfb(unittest.TestCase):
    def test_kimenet(self):
        eredmeny = [[1, 0, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1]]
        self.assertEqual(general_kfb(2, 3), eredmeny)


class TestGeneralKfj(unittest.TestCase):
    def test_hallgato_kisebb_mint_tetel(self):
        eredmeny = [1, 1, 1]
        self.assertEqual(general_kfj(2, 3), eredmeny)

    def test_hallgato_nagyobb_mint_tetel(self):
        eredmeny = [1, 1, 1]
        self.assertEqual(general_kfj(4, 3), eredmeny)
        self.assertEqual(general_kfj(5, 3), eredmeny)
        eredmeny = [2, 2, 2]
        self.assertEqual(general_kfj(6, 3), eredmeny)
        self.assertEqual(general_kfj(8, 3), eredmeny)


class TestGeneralBounds(unittest.TestCase):
    def test_kimenet(self):
        eredmeny = [(0, 1), (0, 1), (0, 1), (0, 1)]
        self.assertEqual(general_bounds(2, 2), eredmeny)
        eredmeny = [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]
        self.assertEqual(general_bounds(2, 3), eredmeny)


class TestSorMaxAvg(unittest.TestCase):
    def test_kimenet_2x2(self):
        eredmeny = (10+6)/2
        jegymatrix = [[7, 10], [4, 6]]
        self.assertEqual(sorMaxAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_2x3(self):
        eredmeny = (10+7)/2
        jegymatrix = [[10, 6, 7], [4, 7, 6]]
        self.assertEqual(sorMaxAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_2x5(self):
        eredmeny = (9+7)/2
        jegymatrix = [[4, 9, 8, 6, 5], [6, 4, 7, 4, 4]]
        self.assertEqual(sorMaxAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_3x3(self):
        eredmeny = (10+9+9)/3
        jegymatrix = [[10, 4, 8], [7, 9, 8], [7, 9, 5]]
        self.assertEqual(sorMaxAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_4x3(self):
        eredmeny = (8+8+10+8)/4
        jegymatrix = [[8, 4, 5], [8, 7, 7], [4, 10, 6], [5, 8, 7]]
        self.assertEqual(sorMaxAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_5x5(self):
        eredmeny = (10+10+10+9+10)/5
        jegymatrix = [[10, 10, 4, 8, 5], [7, 10, 5, 7, 8],
                      [8, 7, 10, 7, 10], [9, 4, 8, 4, 8], [10, 8, 8, 6, 6]]
        self.assertEqual(sorMaxAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_6x4(self):
        eredmeny = (10+9+10+9+10+7)/6
        jegymatrix = [[10, 6, 7, 7], [8, 9, 7, 5], [10, 10, 4, 4],
                      [9, 7, 7, 6], [7, 7, 4, 10], [5, 4, 5, 7]]
        self.assertEqual(sorMaxAvg(len(jegymatrix), jegymatrix), eredmeny)


class TestSorMinAvg(unittest.TestCase):
    def test_kimenet_2x2(self):
        eredmeny = (7+4) / 2
        jegymatrix = [[7, 10], [4, 6]]
        self.assertEqual(sorMinAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_2x3(self):
        eredmeny = (6+4) / 2
        jegymatrix = [[10, 6, 7], [4, 7, 6]]
        self.assertEqual(sorMinAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_2x5(self):
        eredmeny = (4+4) / 2
        jegymatrix = [[4, 9, 8, 6, 5], [6, 4, 7, 4, 4]]
        self.assertEqual(sorMinAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_3x3(self):
        eredmeny = (4+7+5) / 3
        jegymatrix = [[10, 4, 8], [7, 9, 8], [7, 9, 5]]
        self.assertEqual(sorMinAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_4x3(self):
        eredmeny = (4+7+4+5) / 4
        jegymatrix = [[8, 4, 5], [8, 7, 7], [4, 10, 6], [5, 8, 7]]
        self.assertEqual(sorMinAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_5x5(self):
        eredmeny = (4+5+7+4+6) / 5
        jegymatrix = [[10, 10, 4, 8, 5], [7, 10, 5, 7, 8],
                      [8, 7, 10, 7, 10], [9, 4, 8, 4, 8], [10, 8, 8, 6, 6]]
        self.assertEqual(sorMinAvg(len(jegymatrix), jegymatrix), eredmeny)

    def test_kimenet_6x4(self):
        eredmeny = (6+5+4+6+4+4) / 6
        jegymatrix = [[10, 6, 7, 7], [8, 9, 7, 5], [10, 10, 4, 4],
                      [9, 7, 7, 6], [7, 7, 4, 10], [5, 4, 5, 7]]
        self.assertEqual(sorMinAvg(len(jegymatrix), jegymatrix), eredmeny)


class TestCfEredmenyGeneralas(unittest.TestCase):
    def test_kimenet_2x2_min(self):
        eredmeny = 7 + 6
        jegymatrix =    [[7, 10], [4, 6]]
        binarismatrix = [[1, 0] , [0, 1]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_2x2_max(self):
        eredmeny = 10 + 4
        jegymatrix =    [[7, 10], [4, 6]]
        binarismatrix = [[0, 1], [1, 0]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_2x3_min(self):
        eredmeny = 6+4
        jegymatrix =    [[10, 6, 7], [4, 7, 6]]
        binarismatrix = [[0 , 1, 0], [1, 0, 0]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_2x3_max(self):
        eredmeny = 10+7
        jegymatrix =    [[10, 6, 7], [4, 7, 6]]
        binarismatrix = [[1, 0, 0] , [0, 1, 0]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_2x5_min(self):
        eredmeny = 4+4
        jegymatrix =    [[4, 9, 8, 6, 5], [6, 4, 7, 4, 4]]
        binarismatrix = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_2x5_max(self):
        eredmeny = 9+7
        jegymatrix =    [[4, 9, 8, 6, 5], [6, 4, 7, 4, 4]]
        binarismatrix = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_3x3_min(self):
        eredmeny = 4+7+5
        jegymatrix =    [[10, 4, 8], [7, 9, 8], [7, 9, 5]]
        binarismatrix = [[0 , 1, 0], [1, 0, 0], [0, 0, 1]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_3x3_max(self):
        eredmeny = 10+8+9
        jegymatrix =    [[10, 4, 8], [7, 9, 8], [7, 9, 5]]
        binarismatrix = [[1 , 0, 0], [0, 0, 1], [0, 1, 0]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_4x3_min(self):
        eredmeny = 4+7+4+5
        jegymatrix =    [[8, 4, 5], [8, 7, 7], [4, 10, 6], [5, 8, 7]]
        binarismatrix = [[0, 1, 0], [0, 0, 1], [1, 0, 0], [1, 0, 0]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_4x3_max(self):
        eredmeny = 8+7+10+8
        jegymatrix =    [[8, 4, 5], [8, 7, 7], [4, 10, 6], [5, 8, 7]]
        binarismatrix = [[1, 0, 0], [0, 0, 1], [0, 1 , 0], [0, 1, 0]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_5x5_min(self):
        eredmeny = 4+7+7+4+6
        jegymatrix =    [[10, 10, 4, 8, 5], [7, 10, 5, 7, 8],
                         [8, 7, 10, 7, 10], [9, 4, 8, 4, 8], [10, 8, 8, 6, 6]]
        binarismatrix = [[0 , 0 , 1, 0, 0], [1, 0 , 0, 0, 0],
                         [0, 0, 0 , 1, 0 ], [0, 1, 0, 0, 0], [0 , 0, 0, 0, 1]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_5x5_max(self):
        eredmeny = 8+10+10+8+10
        jegymatrix =    [[10, 10, 4, 8, 5], [7, 10, 5, 7, 8],
                         [8, 7, 10, 7, 10], [9, 4, 8, 4, 8], [10, 8, 8, 6, 6]]
        binarismatrix = [[0 , 0 , 0, 1, 0], [0, 1 , 0, 0, 0],
                         [0, 0, 1 , 0, 0 ], [0, 0, 0, 0, 1], [1 , 0, 0, 0, 0]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_6x4_min(self):
        eredmeny = 6+5+4+6+4+5
        jegymatrix =    [[10, 6, 7, 7], [8, 9, 7, 5], [10, 10, 4, 4],
                         [9, 7, 7, 6], [7, 7, 4, 10], [5, 4, 5, 7]]
        binarismatrix = [[0 , 1, 0, 0], [0, 0, 0, 1], [0 , 0 , 0, 1],
                         [0, 0, 0, 1], [0, 0, 1, 0 ], [1, 0, 0, 0]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)

    def test_kimenet_6x4_max(self):
        eredmeny = 10+9+10+9+10+5
        jegymatrix =    [[10, 6, 7, 7], [8, 9, 7, 5], [10, 10, 4, 4],
                         [9, 7, 7, 6], [7, 7, 4, 10], [5, 4, 5, 7]]
        binarismatrix = [[1 , 0, 0, 0], [0, 1, 0, 0], [1 , 0 , 0, 0],
                         [1, 0, 0, 0], [0, 0, 0, 1 ], [0, 0, 1, 0]]
        self.assertEqual(cfEredmenyGeneralas(jegymatrix, binarismatrix), eredmeny)


class TestLp(unittest.TestCase):
    def test_lp_2x2_min(self):
        n = 2
        m = 2
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[7, 10], [4, 6]]
        c = convert_1D(jegymatrix)
        binarismatrix = [[1, 0] , [0, 1]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_2x2_max(self):
        n = 2
        m = 2
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[7, 10], [4, 6]]
        c = -1 * np.array(convert_1D(jegymatrix))
        binarismatrix = [[0, 1], [1, 0]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_2x3_min(self):
        n = 2
        m = 3
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[10, 6, 7], [4, 7, 6]]
        c = convert_1D(jegymatrix)
        binarismatrix = [[0, 1, 0], [1, 0, 0]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_2x3_max(self):
        n = 2
        m = 3
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[10, 6, 7], [4, 7, 6]]
        c = -1 * np.array(convert_1D(jegymatrix))
        binarismatrix = [[1, 0, 0], [0, 1, 0]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_2x5_min(self):
        n = 2
        m = 5
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[4, 9, 8, 6, 5], [6, 4, 7, 4, 4]]
        c = convert_1D(jegymatrix)
        binarismatrix = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_2x5_max(self):
        n = 2
        m = 5
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[4, 9, 8, 6, 5], [6, 4, 7, 4, 4]]
        c = -1 * np.array(convert_1D(jegymatrix))
        binarismatrix = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_3x3_min(self):
        n = 3
        m = 3
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[10, 4, 8], [7, 9, 8], [7, 9, 5]]
        c = convert_1D(jegymatrix)
        binarismatrix = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_3x3_max(self):
        n = 3
        m = 3
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[10, 4, 8], [7, 9, 8], [7, 9, 5]]
        c = -1 * np.array(convert_1D(jegymatrix))
        binarismatrix = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_4x3_min(self):
        n = 4
        m = 3
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[8, 4, 5], [8, 7, 7], [4, 10, 6], [5, 8, 7]]
        c = convert_1D(jegymatrix)
        binarismatrix = [[0, 1, 0], [0, 0, 1], [1, 0, 0], [1, 0, 0]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_4x3_max(self):
        n = 4
        m = 3
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[8, 4, 5], [8, 7, 7], [4, 10, 6], [5, 8, 7]]
        c = -1 * np.array(convert_1D(jegymatrix))
        binarismatrix = [[1, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 0]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_5x5_min(self):
        n = 5
        m = 5
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[10, 10, 4, 8, 5], [7, 10, 5, 7, 8],
                      [8, 7, 10, 7, 10], [9, 4, 8, 4, 8], [10, 8, 8, 6, 6]]
        c = convert_1D(jegymatrix)
        binarismatrix = [[0, 0, 1, 0, 0], [1, 0, 0, 0, 0],
                         [0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 1]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_5x5_max(self):
        n = 5
        m = 5
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[10, 10, 4, 8, 5], [7, 10, 5, 7, 8],
                      [8, 7, 10, 7, 10], [9, 4, 8, 4, 8], [10, 8, 8, 6, 6]]
        c = -1 * np.array(convert_1D(jegymatrix))
        binarismatrix = [[0, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 1], [1, 0, 0, 0, 0]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_6x4_min(self):
        n = 6
        m = 4
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[10, 6, 7, 7], [8, 9, 7, 5], [10, 10, 4, 4],
                      [9, 7, 7, 6], [7, 7, 4, 10], [5, 4, 5, 7]]
        c = convert_1D(jegymatrix)
        binarismatrix = [[0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1],
                         [0, 0, 0, 1], [0, 0, 1, 0], [1, 0, 0, 0]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)

    def test_lp_6x4_max(self):
        n = 6
        m = 4
        nullmatrix = []
        feltolt0(nullmatrix, n, m)
        jegymatrix = [[10, 6, 7, 7], [8, 9, 7, 5], [10, 10, 4, 4],
                      [9, 7, 7, 6], [7, 7, 4, 10], [5, 4, 5, 7]]
        c = -1 * np.array(convert_1D(jegymatrix))
        binarismatrix = [[1, 0, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0],
                         [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
        lp(cf=c, n=n, m=m, binarismatrix=nullmatrix)
        self.assertEqual(binarismatrix, nullmatrix)
