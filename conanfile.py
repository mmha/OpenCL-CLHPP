from conans import ConanFile, CMake

class OpenCLHPPConan(ConanFile):
    name = "opencl-clhpp"
    version = "20190109"
    requires = "opencl-headers/[>=0]@mmha/testing"
    exports_sources = "*"
    no_copy_source = True

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_DOCS"] = False
        cmake.definitions["BUILD_TESTS"] = False
        cmake.definitions["BUILD_EXAMPLES"] = False
        cmake.configure()
        cmake.build()
        cmake.install()
