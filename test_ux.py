#TESTWITH workflows/1.0
import unittest

class app_testing(unittest.TestCase):
    def test_import(self):
        try:
            import ux
            self.assertEqual(True, True)
        except:
            self.assertEqual(True, False)
        
    def test_initialization(self):
        try:
            import ux
            my_app = ux.app(app_mode=True, debug=True)
            self.assertEqual(True, True)
        except:
            self.assertEqual(True, False)
        