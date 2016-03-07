from conans import ConanFile
from conans.tools import download, unzip
import os

VERSION = "0.0.1"


class CMakeMultiTargetsConan(ConanFile):
    name = "cmake-multi-targets"
    version = os.environ.get("CONAN_VERSION_OVERRIDE", VERSION)
    generators = "cmake"
    requires = ("cmake-include-guard/master@smspillaz/cmake-include-guard",
                "tooling-cmake-util/master@smspillaz/tooling-cmake-util",
                "cmake-unit/master@smspillaz/cmake-unit")
    url = "http://github.com/polysquare/cmake-multi-targets"
    license = "MIT"

    def source(self):
        zip_name = "cmake-multi-targets.zip"
        download("https://github.com/polysquare/"
                 "cmake-multi-targets/archive/{version}.zip"
                 "".format(version="v" + VERSION),
                 zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def package(self):
        self.copy(pattern="*.cmake",
                  dst="cmake/cmake-multi-targets",
                  src="cmake-multi-targets-" + VERSION,
                  keep_path=True)
