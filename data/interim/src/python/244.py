# my_rule.bzl

def _my_rule_impl(ctx):
    # Retrieve the toolchain
    toolchain = ctx.toolchains["@my_repo//:my_gcc_toolchain"]
    compiler_executable = toolchain.compiler_executable
    compiler_flags = toolchain.compiler_flags

    # Here you can use the compiler_executable and compiler_flags to set up actions.
    # This is just an example and the details will depend on your specific use case.
    ctx.actions.run(
        executable = compiler_executable,
        arguments = compiler_flags + ctx.files.srcs,
        outputs = [ctx.outputs.out],
    )

# Define a rule that uses the toolchain
my_rule = rule(
    implementation = _my_rule_impl,
    attrs = {
        "srcs": attr.label_list(allow_files = True),
        "out": attr.output(),
    },
    toolchains = ["@my_repo//:my_gcc_toolchain"],
)
