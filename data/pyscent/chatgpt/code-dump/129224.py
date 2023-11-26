def _my_rule_impl(ctx):
    output_file = ctx.actions.declare_file(ctx.attr.name + ".out")
    
    commands = []
    for src in ctx.files.srcs:
        # You can add multiple commands here
        commands.append("echo 'Processing {src}'".format(src = src.path))
        commands.append("cat {src} >> {out}".format(src = src.path, out = output_file.path))

    ctx.actions.run_shell(
        outputs = [output_file],
        inputs = ctx.files.srcs,
        command = "\n".join(commands),
    )

my_rule = rule(
    implementation = _my_rule_impl,
    attrs = {
        "srcs": attr.label_list(allow_files = True),
    },
)
