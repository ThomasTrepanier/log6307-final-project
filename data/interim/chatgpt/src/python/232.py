# my_rule_test.bzl
load("//:my_rule.bzl", "my_rule")
load("@bazel_skylib//lib:unittest.bzl", "asserts", "unittest")

def _my_rule_test_impl(ctx):
    env = unittest.begin(ctx)
    target_under_test = "//:target"
    
    # Test that the rule produces the expected file.
    asserts.true(env, env.file_exists(target_under_test + ".txt"))

    # Test the contents of the file.
    contents = env.file_contents(target_under_test + ".txt")
    asserts.equals(env, "Hello, World!", contents)

    return unittest.end(env)

my_rule_test = unittest.make(_my_rule_test_impl)

def _my_rule_test_suite():
    my_rule_test(
        name = "my_rule_test",
        target_under_test = ":target",
    )

# Generate the test suite.
_my_rule_test_suite()
