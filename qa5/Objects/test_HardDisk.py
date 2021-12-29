from unittest import TestCase, mock
from HardDisk import HardDisk
from unittest.mock import patch


class TestHardDisk(TestCase):
    def setUp(self):
        self.hd = HardDisk(50, 17)

    def test_show(self):
        print(self.hd.show())
        self.assertTrue(self.hd.show() == "occupied space: 50, total space: 100, files: 17")

    def test_free_space_false(self):
        self.assertFalse(self.hd.freeSpace() != 50)

    def test_free_space_true(self):
        self.assertTrue(self.hd.freeSpace() == 50)

    def test_add_file_false(self):
        self.hd.addFile(12)
        print(self.hd.show())
        self.assertFalse(self.hd.show() != "occupied space: 62, total space: 100, files: 18")

    def test_add_file_true(self):
        self.hd.addFile(12)
        print(self.hd.show())
        self.assertTrue(self.hd.show() == "occupied space: 62, total space: 100, files: 18")

    def test_del_file_false(self):
        self.hd.delFile(12)
        print(self.hd.show())
        self.assertFalse(self.hd.show() != "occupied space: 38, total space: 100, files: 16")

    def test_del_file_true(self):
        self.hd.delFile(12)
        print(self.hd.show())
        self.assertTrue(self.hd.show() == "occupied space: 38, total space: 100, files: 16")
