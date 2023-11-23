def _my_rule_impl(ctx):
    # Declare an output file.
    output = ctx.actions.declare_file(ctx.attr.name + ".txt")

    # Write some text to the output file.
    ctx.actions.write(output, "Hello, world!")

    # Return the output file so that it can be used by other rules.
    return [DefaultInfo(files = depset([output]))]

my_rule = rule(
    implementation = _my_rule_impl,
    attrs = {"name": attr.string()},
)
