import pytest
from Level1.DriveFinder import SystemDriveFinder
from Level1.searchfile import FileFinder
class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('filename1.txt','C:/hcl1')
        act=['C:/hcl1\\filename1.txt']
        self.expected_filename=act
        self.actual_res=d
        assert self.expected_filename==self.actual_res