def spaced_randoms(n, d, R, first=None):
    solver = z3.SolverFor("QF_FD")
    numbers = [z3.Int("x{}".format(x)) for x in range(n)]
    for number in numbers:
        solver.add(number >= 0)
        solver.add(number <= R)
    for ii in range(n):
        for jj in range(ii+1,n):
            solver.add(z3.Or(numbers[ii] - numbers[jj] > d, numbers[ii] - numbers[jj] < -d))
    if first is not None:
        solver.add(numbers[0] == first)
    result = solver.check()
    if str(result) != "sat":
        raise Exception("Unsatisfiable")
    model = solver.model()
    return [model.get_interp(number) for number in numbers]
