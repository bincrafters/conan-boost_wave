#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostWaveConan(ConanFile):
    name = "boost_wave"
    version = "1.67.0"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["wave"]
    is_header_only = False

    options = {"shared": [True, False]}
    default_options = "shared=False"

    # TODO: date_time
    requires = (
        "boost_assert/1.67.0@bincrafters/testing",
        "boost_concept_check/1.67.0@bincrafters/testing",
        "boost_config/1.67.0@bincrafters/testing",
        "boost_core/1.67.0@bincrafters/testing",
        "boost_filesystem/1.67.0@bincrafters/testing",
        "boost_iterator/1.67.0@bincrafters/testing",
        "boost_lexical_cast/1.67.0@bincrafters/testing",
        "boost_mpl/1.67.0@bincrafters/testing",
        "boost_multi_index/1.67.0@bincrafters/testing",
        "boost_package_tools/1.67.0@bincrafters/testing",
        "boost_pool/1.67.0@bincrafters/testing",
        "boost_preprocessor/1.67.0@bincrafters/testing",
        "boost_serialization/1.67.0@bincrafters/testing",
        "boost_smart_ptr/1.67.0@bincrafters/testing",
        "boost_spirit/1.67.0@bincrafters/testing",
        "boost_static_assert/1.67.0@bincrafters/testing",
        "boost_throw_exception/1.67.0@bincrafters/testing",
        "boost_type_traits/1.67.0@bincrafters/testing"
    )

    def package_id_additional(self):
        boost_deps_only = [dep_name for dep_name in self.info.requires.pkg_names if dep_name.startswith("boost_")]

        for dep_name in boost_deps_only:
            self.info.requires[dep_name].full_version_mode()

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost_wave"
    description = "Please visit http://www.boost.org/doc/libs/1_67_0"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.67.0@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()

    # END
