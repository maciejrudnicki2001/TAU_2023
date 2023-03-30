import unittest
from scenario1 import TestScenario1
from scenario2 import TestScenario2
from scenario3 import TestScenario3

if __name__ == '__main__':
    suite = unittest.TestSuite()
    TestScenario1.browser = 'chrome'
    suite.addTest(TestScenario1('test_open_saucedemo'))
    TestScenario2.browser = 'chrome'
    suite.addTest(TestScenario2('test_login'))
    suite.addTest(TestScenario2('test_locked_out_user'))
    suite.addTest(TestScenario2('test_invalid_username'))
    suite.addTest(TestScenario2('test_invalid_password'))
    suite.addTest(TestScenario2('test_empty_username'))
    suite.addTest(TestScenario2('test_empty_password'))
    suite.addTest(TestScenario2('test_empty_username_and_password'))
    suite.addTest(TestScenario2('test_login_with_special_characters'))
    TestScenario3.browser = 'chrome'
    suite.addTest(TestScenario3('test_additional_feature'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

    
                  