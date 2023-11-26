def _my_rule_impl(ctx):
    # Retrieve the toolchain
    toolchain = ctx.toolchains["@my_repo//:my_gcc_toolchain"]
    # Check if all expected fields are present
    if not hasattr(toolchain, "compiler_executable") or \
       not hasattr(toolchain, "compiler_flags") or \
       not hasattr(toolchain, "linker_executable") or \
       not hasattr(toolchain, "linker_flags"):
        fail("Invalid toolchain. Expecting fields: compiler_executable, compiler_flags, linker_executable, linker_flags.")
    # ...
