# gcc_toolchain.bzl

# Use this struct to define what the toolchain represents.
# In this case, we need the path to the gcc compiler and the flags we want to use.
CCToolchainInfo = provider(
    fields = {
        "compiler_executable": "Path to the gcc compiler",
        "compiler_flags": "List of flags for the compiler",
    },
)

def _gcc_toolchain_impl(ctx):
    """Implementation of the gcc_toolchain rule."""
    compiler_executable = ctx.file.compiler_executable
    compiler_flags = ctx.attr.compiler_flags
    return CCToolchainInfo(
        compiler_executable = compiler_executable,
        compiler_flags = compiler_flags,
    )

# Define the toolchain rule.
gcc_toolchain = rule(
    implementation = _gcc_toolchain_impl,
    attrs = {
        "compiler_executable": attr.label(
            doc = "Label for the GCC executable.",
            allow_single_file = True,
            mandatory = True,
            cfg = "host",
        ),
        "compiler_flags": attr.string_list(
            doc = "List of flags for the compiler",
            default = ["-O2"],
        ),
    },
)
