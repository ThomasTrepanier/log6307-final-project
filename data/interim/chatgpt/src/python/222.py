def _docker_run_impl(ctx):
    # Generate the Docker command to be run
    command = "\n".join([
        "docker pull {image}".format(image = ctx.attr.image),
        "docker run {image} {command}".format(image = ctx.attr.image, command = ctx.attr.command),
    ])

    # Use ctx.actions.write to create a shell script that contains the Docker command
    script_file = ctx.actions.declare_file(ctx.attr.name + ".sh")
    ctx.actions.write(script_file, command)

    # Use ctx.actions.run to execute the shell script
    ctx.actions.run(
        outputs = [ctx.outputs.out],
        inputs = [script_file],
        executable = "bash",
        arguments = [script_file.path],
    )

docker_run = rule(
    implementation = _docker_run_impl,
    attrs = {
        "image": attr.string(mandatory = True),
        "command": attr.string(mandatory = True),
        "out": attr.output(mandatory = True),
    },
)
