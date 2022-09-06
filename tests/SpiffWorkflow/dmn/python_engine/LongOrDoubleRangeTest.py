import unittest

from decimal import Decimal

from .PythonDecisionRunner import PythonDecisionRunner


class LongOrDoubleDecisionRangeTestClass(unittest.TestCase):
    """
    Doc: https://docs.camunda.org/manual/7.7/user-guide/dmn-engine/
    """

    def test_long_or_double_decision_string_output_inclusive(self):
        runner = PythonDecisionRunner('long_or_double_decision_range_inclusive.dmn')

        res = runner.decide({"Age":Decimal('100.05')})
        self.assertEqual(res.description, '100.05-110.05 Inclusive Annotation')

        res = runner.decide({"Age":Decimal('99')})
        self.assertEqual(res.description, 'ELSE Row Annotation')

        res = runner.decide({"Age":Decimal('110.05')})
        self.assertEqual(res.description, '100.05-110.05 Inclusive Annotation')

        res = runner.decide({"Age":Decimal('111')})
        self.assertEqual(res.description, 'ELSE Row Annotation')

    def test_long_or_double_decision_string_output_exclusive(self):
        runner = PythonDecisionRunner('long_or_double_decision_range_exclusive.dmn')

        res = runner.decide({"Age":Decimal('100.05')})
        self.assertEqual(res.description, 'ELSE Row Annotation')

        res = runner.decide({"Age":Decimal('101')})
        self.assertEqual(res.description, '100.05-110.05 Exclusive Annotation')

        res = runner.decide({"Age":Decimal('110.05')})
        self.assertEqual(res.description, 'ELSE Row Annotation')

        res = runner.decide({"Age":Decimal('109')})
        self.assertEqual(res.description, '100.05-110.05 Exclusive Annotation')

    def test_long_or_double_decision_string_output_excl_inclusive(self):
        runner = PythonDecisionRunner('long_or_double_decision_range_excl_inclusive.dmn')

        res = runner.decide({"Age":Decimal('100.05')})
        self.assertEqual(res.description, 'ELSE Row Annotation')

        res = runner.decide({"Age":Decimal('101')})
        self.assertEqual(res.description, '100.05-110.05 ExclInclusive Annotation')

        res = runner.decide({"Age":Decimal('110.05')})
        self.assertEqual(res.description, '100.05-110.05 ExclInclusive Annotation')

        res = runner.decide({"Age":Decimal('111')})
        self.assertEqual(res.description, 'ELSE Row Annotation')

    def test_long_or_double_decision_string_output_incl_exclusive(self):
        runner = PythonDecisionRunner('long_or_double_decision_range_incl_exclusive.dmn')

        res = runner.decide({"Age":Decimal('100.05')})
        self.assertEqual(res.description, '100.05-110.05 InclExclusive Annotation')

        res = runner.decide({"Age":Decimal('99')})
        self.assertEqual(res.description, 'ELSE Row Annotation')

        res = runner.decide({"Age":Decimal('110.05')})
        self.assertEqual(res.description, 'ELSE Row Annotation')

        res = runner.decide({"Age":Decimal('109')})
        self.assertEqual(res.description, '100.05-110.05 InclExclusive Annotation')

def suite():
    return unittest.TestLoader().loadTestsFromTestCase(LongOrDoubleDecisionRangeTestClass)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
