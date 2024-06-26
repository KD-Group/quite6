import unittest
import quite6
import os


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.delete_caches()

    def test_generate_cache(self):
        quite6.auto_generate_cache(self.root_path)
        ui_files = self.find_format_files('.ui')
        cache_files = self.find_format_files('.cache')
        qrc_files = self.find_format_files('.qrc')
        for ui_file in ui_files:
            self.assertTrue(ui_file in cache_files)
        for qrc_file in qrc_files:
            self.assertTrue(qrc_file in cache_files)

    def tearDown(self):
        self.delete_caches()

    def find_format_files(self, file_format: str = None) -> list:
        assert isinstance(file_format, str)
        found_file_name = []
        for root_dir, _, files in os.walk(self.root_path):
            for file in files:
                if os.path.splitext(file)[1] == file_format:
                    found_file_name.append(os.path.splitext(file)[0].split('@')[0])
        return found_file_name

    def delete_caches(self):
        # delete old cache file for test
        self.root_path = os.path.dirname(__file__)
        for i in range(2):
            self.root_path = os.path.dirname(self.root_path)
        self.old_caches = os.path.join(self.root_path, 'cache')
        if os.path.exists(self.old_caches):
            for cached_file in os.listdir(self.old_caches):
                os.remove(os.path.join(self.old_caches, cached_file))
            os.rmdir(os.path.join(self.root_path, 'cache'))


if __name__ == '__main__':
    unittest.main()
