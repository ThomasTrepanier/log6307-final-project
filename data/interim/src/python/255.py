def _my_rule_impl(ctx):
    output_file_1 = ctx.actions.declare_file(ctx.attr.name + "_1.out")
    output_file_2 = ctx.actions.declare_file(ctx.attr.name + "_2.out")
    
    # Assume 'stuff' attribute is a list of labels to File targets
    stuff_files = [f for target in ctx.attr.stuff for f in target.files.to_list()]

    # First action
    ctx.actions.run(
        outputs = [output_file_1],
        inputs = ctx.files.srcs + stuff_files,  # Add 'stuff_files' as inputs
        executable = ctx.executable._tool,  # Your tool executable
        arguments = [...],  # Your command-line arguments
    )

    # Second action
    ctx.actions.run(
        outputs = [output_file_2],
        inputs = ctx.files.srcs + stuff_files,  # Add 'stuff_files' as inputs again
        executable = ctx.executable._tool,  # Your tool executable
        arguments = [...],  # Your command-line arguments
    )

my_rule = rule(
    implementation = _my_rule_impl,
    attrs = {
        "srcs": attr.label_list(allow_files = True),
        "stuff": attr.label_list(allow_files = True),  # Declare 'stuff' attribute
        "_tool": attr.label(label = executable = True, cfg = "host", default = "//path/to:my_tool"),
    },
)
