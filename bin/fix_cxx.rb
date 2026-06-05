# Build shim for a broken local C++ toolchain on this machine. Two defects:
#
#  1. This Ruby (ruby-3.4.1) was installed with CXX="false" in its rbconfig,
#     so every native C++ gem extension (eventmachine, etc.) fails to compile.
#  2. The Command Line Tools' libc++ header dir
#     (/Library/Developer/CommandLineTools/usr/include/c++/v1) is empty, so
#     clang++ can't find <iostream>. The complete copy lives in the SDK.
#
# We patch the compiler and inject the SDK's libc++ include path in-memory for
# gem-build subprocesses only — the global Ruby install and toolchain are left
# untouched. The proper permanent fix is to reinstall the Command Line Tools
# (`sudo rm -rf /Library/Developer/CommandLineTools && xcode-select --install`)
# and a Ruby built with a working C++ compiler; then this shim is unnecessary.
#
# Used via:  RUBYOPT="-r$(pwd)/bin/fix_cxx.rb" bundle install
require "rbconfig"

# (1) Repair CXX if it was disabled at Ruby-build time.
%w[CXX].each do |key|
  if RbConfig::CONFIG[key].to_s.strip == "false"
    RbConfig::CONFIG[key] = "clang++"
    RbConfig::MAKEFILE_CONFIG[key] = "clang++" if defined?(RbConfig::MAKEFILE_CONFIG)
  end
end

# (2) If the CLT libc++ headers are missing, point clang at the SDK's copy.
clt_iostream = "/Library/Developer/CommandLineTools/usr/include/c++/v1/iostream"
sdk_cxx = "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1"
if !File.exist?(clt_iostream) && File.directory?(sdk_cxx)
  inject = " -isystem #{sdk_cxx}"
  %w[CXXFLAGS].each do |key|
    [RbConfig::CONFIG, (RbConfig::MAKEFILE_CONFIG if defined?(RbConfig::MAKEFILE_CONFIG))].compact.each do |cfg|
      cfg[key] = "#{cfg[key]}#{inject}" unless cfg[key].to_s.include?(sdk_cxx)
    end
  end
end
