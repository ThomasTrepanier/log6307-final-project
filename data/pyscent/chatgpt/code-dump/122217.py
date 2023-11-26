# gcc_toolchain.bzl

CCToolchainInfo = provider(
    fields = {
        "compiler_executable": "Path to the gcc compiler",
        "compiler_flags": "List of flags for the compiler",
        "linker_executable": "Path to the linker",
        "linker_flags": "List of flags for the linker",
    },
)

def _gcc_toolchain_impl(ctx):
    """Implementation of the gcc_toolchain rule."""
    compiler_executable = ctx.file.compiler_executable
    compiler_flags = ctx.attr.compiler_flags
    linker_executable = ctx.file.linker_executable
    linker_flags = ctx.attr.linker_flags
    return CCToolchainInfo(
        compiler_executable = compiler_executable,
        compiler_flags = compiler_flags,
        linker_executable = linker_executable,
        linker_flags = linker_flags,
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
        "linker_executable": attr.label(
            doc = "Label for the linker executable.",
            allow_single_file = True,
            mandatory = True,
            cfg = "host",
        ),
        "linker_flags": attr.string_list(
            doc = "List of flags for the linker",
            default = ["-s"],
        ),
    },
)
