load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "<enter_sha256>",  # Update this with the correct sha256 of the version you want to use
    strip_prefix = "rules_docker-<enter_version>",  # Update this with the correct version
    urls = ["https://github.com/bazelbuild/rules_docker/releases
