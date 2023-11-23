def _my_rule_impl(ctx):
    # The outputs of the dependency rule will be available in the depset 'ctx.files.deps'
    for dep in ctx.files.deps:
        ctx.actions.run(
            outputs = [ctx.outputs.out],
            inputs = depset([dep]),
            executable = ctx.executable._tool,
            arguments = [dep.path],
        )

my_rule = rule(
    implementation = _my_rule_impl,
    attrs = {
        "deps": attr.label_list(allow_files = True),
        "_tool": attr.label(default = "//path/to:tool", cfg = "host", executable = True),
        "out": attr.output(),
    },
)
