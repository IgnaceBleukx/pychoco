import unittest

from pychoco import create_model


class TestPow(unittest.TestCase):

    def testPow1(self):
        m = create_model()
        dividend = m.intvar(2, 3, "dividend")
        divisor = 1
        remainder = m.intvar(1, 2, "remainder")
        m.pow(dividend, divisor, remainder).post()
        s = m.get_solver()
        s.set_input_order_lb_search(dividend, remainder)
        s.solve()

    def testPow2(self):
        model = create_model("model");
        a = model.intvar(2, 6);
        b = 2;
        c = model.intvar(5, 30);
        model.pow(a, b, c).post()
        self.assertEquals(len(model.get_solver().find_all_solutions()), 3)

    def testPow3(self):
        model = create_model("model")
        x = model.intvar(-5, 5)
        z = model.intvar(-5, 5)
        model.pow(x, 3, z).post()
        self.assertEquals(len(model.get_solver().find_all_solutions()), 3)
