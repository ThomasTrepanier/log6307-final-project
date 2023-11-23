# my_cpp_rule.bzl

load(":gcc_toolchain.bzl", "CCToolchainInfo")

def _my_cpp_rule_impl(ctx):
    """Implementation of the my_cpp_rule."""
    toolchain = ctx.toolchains["@my_repo//:my_gcc_toolchain"]
    compiler_executable = toolchain.compiler_executable
    compiler_flags = toolchain.compiler_flags

    obj_files = []
    for src in ctx.files.srcs:
        obj_file = ctx.actions.declare_file(src.short_path + ".o")
        obj_files.append(obj_file)
        ctx.actions.run(
            inputs = [src],
            outputs = [obj_file],
            executable = compiler_executable,
            arguments = compiler_flags + ["-c", src.path, "-o", obj_file.path],
            mnemonic = "CppCompile",
            progress_message = "Compiling " + src.path,
        )

    executable = ctx.outputs.executable
    ctx.actions.run(
        inputs = obj_files,
        outputs = [executable],
        executable = compiler_executable,
        arguments = compiler_flags + obj_files + ["-o", executable.path],
        mnemonic = "CppLink",
        progress_message = "Linking " + executable.path,
    )

my_cpp_rule = rule(
    implementation = _my_cpp_rule_impl,
    attrs = {
        "srcs": attr.label_list(allow_files = [".cpp"]),
        "out": attr.output(executable = True),
    },
    toolchains = ["@my_repo//:my_gcc_toolchain"],
    outputs = {"executable": "%{name}"},
)
