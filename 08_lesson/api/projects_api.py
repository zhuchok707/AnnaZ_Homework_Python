import requests


class ProjectsAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create_project(self, title):
        return requests.post(
            f"{self.base_url}/projects",
            headers=self.headers,
            json={
                "title": title
            },
        )

    def update_project(self, project_id, title):
        return requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            json={
                "title": title
            },
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
        )
