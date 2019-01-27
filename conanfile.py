#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostWaveConan(base.BoostBaseConan):
    name = "boost_wave"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_wave"
    lib_short_names = ["wave"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    b2_requires = [
        "boost_assert",
        "boost_concept_check",
        "boost_config",
        "boost_core",
        "boost_filesystem",
        "boost_iterator",
        "boost_lexical_cast",
        "boost_mpl",
        "boost_multi_index",
        "boost_pool",
        "boost_preprocessor",
        "boost_serialization",
        "boost_smart_ptr",
        "boost_spirit",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits"
    ]
