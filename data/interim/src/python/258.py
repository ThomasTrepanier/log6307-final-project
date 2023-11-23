def _cc_binary_impl(ctx):
    toolchain = ctx.toolchains["//my_pkg:c_toolchain_type"]

    if toolchain.single_step_build_and_link:
        # Use the compiler to build and link in a single step
        ctx.actions.run(
            inputs = ctx.files.srcs,
            outputs = [ctx.outputs.binary],
            executable = toolchain.compiler,
            arguments = [/* ... */],
        )
    else:
        # Use the compiler and linker separately
        obj_files = []
        for src in ctx.files.srcs:
            obj_file = ctx.actions.declare_file(src.basename + ".o")
            ctx.actions.run(
                inputs = [src],
                outputs = [obj_file],
                executable = toolchain.compiler,
                arguments = [/* ... */],
            )
            obj_files.append(obj_file)

        ctx.actions.run(
            inputs = obj_files,
            outputs = [ctx.outputs.binary],
            executable = toolchain.linker,
            arguments = [/* ... */],
        )
