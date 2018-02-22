import unittest

from tests.assignments import test_assign1

suite = unittest.TestLoader().loadTestsFromModule(test_assign1)
unittest.TextTestRunner(verbosity=2).run(suite)
