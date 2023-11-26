# gcc_toolchain.bzl

# ...

def _find_gcc_repository_impl(repository_ctx):
    """Implementation of the find_gcc rule."""
    gcc_path = repository_ctx.which("gcc")
    if not gcc_path:
        fail("gcc not found")

    repository_ctx.file("BUILD", """
exports_files(["gcc"])
""")

    repository_ctx.symlink(gcc_path, "gcc")

find_gcc = repository_rule(
    implementation = _find_gcc_repository_impl,
    local = True,
)

# ...
