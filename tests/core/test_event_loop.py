import unittest
import st
from quite6.core import EventLoop


class MyTestCase(unittest.TestCase):
    def test_event_loop_timeout(self):
        st.set_time_point('start')
        with EventLoop(0.1):
            pass
        self.assertTrue(80 <= st.microsecond_from('start') <= 120)


if __name__ == '__main__':
    unittest.main()
