import click

from buttler.jenkins_wrapper import JenkinsWrapper


@click.group()
def jenkins():
    pass


@click.command()
@click.argument("name")
def create_view(name):
    """Create new list view in Jenkins."""
    jenkins_wrapper = JenkinsWrapper()
    jenkins_wrapper.create_list_view(name)


@click.command()
def show_version():
    """Show version of the Jenkins instance."""
    jenkins_wrapper = JenkinsWrapper()
    jenkins_wrapper.print_version()


@click.command()
@click.argument("name")
@click.argument("view")
def create_job(name, view):
    """Create a new job."""
    jenkins_wrapper = JenkinsWrapper()
    jenkins_wrapper.create_job(name, view)


jenkins.add_command(show_version)
jenkins.add_command(create_view)
jenkins.add_command(create_job)


if __name__ == '__main__':
    jenkins()
