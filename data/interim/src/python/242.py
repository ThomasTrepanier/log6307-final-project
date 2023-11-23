# protoc_py.bzl
load("@bazel_skylib//lib:paths.bzl", "paths")

def _protoc_py_impl(ctx):
    """Implementation of the protoc_py rule."""
    srcs = ctx.files.srcs
    output_dir = paths.join(ctx.bin_dir.path, ctx.label.package)

    # Get the protoc executable from the system
    protoc = ctx.executable._protoc

    # Create the list of arguments for protoc
    args = ctx.actions.args()
    args.add_all(["--python_out", output_dir])
    args.add_all(["--proto_path", paths.dirname(src.path) for src in srcs])
    args.add_all([src.path for src in srcs])

    # Define the output files
    outs = [ctx.actions.declare_file(paths.join(output_dir, paths.relativize(src.path, paths.dirname(src.path)) + ".pb2.py") for src in srcs)]

    # Create the action that runs protoc
    ctx.actions.run(
        inputs = srcs,
        outputs = outs,
        executable = protoc,
        arguments = [args],
        mnemonic = "ProtocPy",
        progress_message = "Generating Python code from %d .proto files" % len(srcs)
    )

    # Return a struct that represents the output of the rule
    return [DefaultInfo(files = depset(outs))]

protoc_py = rule(
    implementation = _protoc_py_impl,
    attrs = {
        "srcs": attr.label_list(allow_files = [".proto"]),
        "_protoc": attr.label(default = Label("//tools:protoc"), executable = True, cfg = "host"),
    },
    doc = "Generates Python code from .proto files using protoc."
)
