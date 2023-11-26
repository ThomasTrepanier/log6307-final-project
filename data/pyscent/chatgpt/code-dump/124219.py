# A rule that generates a message.
def _message_generator_impl(ctx):
    output = ctx.actions.declare_file(ctx.label.name + ".txt")
    ctx.actions.write(output, ctx.attr.message)
    return [DefaultInfo(files = depset([output]))]

message_generator = rule(
    implementation = _message_generator_impl,
    attrs = {"message": attr.string()},
)
