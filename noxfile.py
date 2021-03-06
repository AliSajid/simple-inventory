import nox

@nox.session(python=["3.7", "3.8", "3.9"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")
