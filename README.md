## This repository holds a conan recipe for Boost.Wave.
[![Build status](https://ci.appveyor.com/api/projects/status/lwhqujr7avicpfna/branch/stable/1.65.1?svg=true)](https://ci.appveyor.com/project/BinCrafters/conan-boost-wave/branch/stable/1.65.1)
[![Travis Status](https://travis-ci.org/bincrafters/conan-boost-wave.svg?branch=stable%2F1.65.1)](https://travis-ci.org/bincrafters/conan-boost-wave)
[![Download](https://api.bintray.com/packages/bincrafters/public-conan/Boost.Wave%3Abincrafters/images/download.svg?version=1.65.1%3Astable) ](https://bintray.com/bincrafters/public-conan/Boost.Wave%3Abincrafters/1.65.1%3Astable/link)

[Conan.io](https://conan.io) package for [Boost.Wave](https://github.com/Boostorg/Wave) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/public-conan/Boost.Wave%3Abincrafters).

## For Users: Use this package

### Basic setup

    $ conan install Boost.Wave/1.65.1@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Boost.Wave/1.65.1@bincrafters/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..
	
Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git. 

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly. 

## Build  

This is a header only library, so nothing needs to be built.

## Package 

    $ conan create bincrafters/stable
	
## Add Remote

	$ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

## Upload

    $ conan upload Boost.Wave/1.65.1@bincrafters/stable --all -r bincrafters

### License
[Boost](www.boost.org/LICENSE_1_0.txt)
