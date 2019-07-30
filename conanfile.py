from conans import ConanFile, CMake, tools
#from conans import ConanFile, AutoToolsBuildEnvironment, tools

class CurllibConan(ConanFile):
    name = "curl"
    version = "0.0.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "conan file to build package for curl"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    requires = "openssl/0.0.1@jenkins/master"
    options = {"shared": [True, False]}
    default_options = "shared=False","openssl:no_asm=True"
    generators = "cmake"
    #generators = "make"

    def build(self):
        cmake = CMake(self)
        if (self.settings.os == "Android"):
            cmake.definitions[ "Platform" ] = "android"
        cmake.configure(source_folder=".")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include/curl", src="package/include/curl")
        self.copy("*", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [ "curl" ]
