config_setting(
    name = "optimization",
    values = {"compilation_mode": "opt"},
)

config_setting(
    name = "debugging",
    values = {"compilation_mode": "dbg"},
)

cc_binary(
    name = "my_binary",
    srcs = ["my_binary.cc"],
    deps = select({
        ":optimization": [":optimized_dependency"],
        ":debugging": [":debugging_dependency"],
        "//conditions:default": [":default_dependency"],
    }),
)
