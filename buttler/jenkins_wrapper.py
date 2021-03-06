from xml.etree import ElementTree as ET

from jenkins import Jenkins
from jenkins import EMPTY_CONFIG_XML

from buttler.config import get_config


class JenkinsWrapper:
    def __init__(self):
        config = get_config()
        self.server = Jenkins(
            config.jenkins_url,
            username=config.jenkins_user,
            password=config.jenkins_password)
        # DON'T REMOVE: workaround to await connection
        self.server.get_info()

    def print_version(self):
        version = self.server.get_version()
        print(f"Jenkins is on version {version}")

    def create_list_view(self, name: str):
        config_xml = """
            <listView>
                <description />
                <jobNames />
            </listView>"""

        if self._exists_view(name):
            print("View exists already. Nothing was done.")
        else:
            self.server.create_view(name, config_xml)
            print(f"View {name} was created successfully.")

    def create_job(self, name: str, view: str):
        if self._exists_job(name):
            print(f"Job {name} already exists. Nothing was done.")
            return
        if not self._exists_view(view):
            self.create_list_view(view)
        self.server.create_job(name, EMPTY_CONFIG_XML)
        print(f"Job {name} was created successfully.")
        self._add_job_to_view(name, view)
        print(f"Job has been added to the view {view}")

    def _exists_job(self, name: str) -> bool:
        jobs = [job.get("name") for job in self.server.get_jobs()
                if job.get("name")]
        return name in jobs

    def _exists_view(self, name: str) -> bool:
        views = [view.get("name") for view in self.server.get_views()
                 if view.get("name")]
        return name in views

    def _add_job_to_view(self, job_name, view_name):
        new_job = """
        <string>%s</string>
        """, job_name
        config = self.server.get_view_config(view_name)
        tree = ET.ElementTree(ET.fromstring(config))
        old_jobs_node = tree.find(".//jobNames")
        # append job node
        new_job = ET.SubElement(old_jobs_node, 'string')
        new_job.text = job_name
        # get string from tree
        config_xml = ET.tostring(tree.getroot()).decode('utf-8')
        # update config
        self.server.reconfig_view(view_name, config_xml)
