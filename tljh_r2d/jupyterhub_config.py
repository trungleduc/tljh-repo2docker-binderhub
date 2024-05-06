"""
This file is only used for local development
and overrides some of the default values from the plugin.
"""

from pathlib import Path
from jupyterhub.auth import DummyAuthenticator
from tljh_repo2docker import TLJH_R2D_ADMIN_SCOPE
from binderhub.binderspawner_mixin import BinderSpawnerMixin
from kubespawner import KubeSpawner
import sys


class BinderSpawner(BinderSpawnerMixin, KubeSpawner):
    pass


HERE = Path(__file__).parent

c.JupyterHub.spawner_class = BinderSpawner

c.JupyterHub.authenticator_class = DummyAuthenticator

c.JupyterHub.allow_named_servers = True

c.Authenticator.admin_users = {"alice"}

c.JupyterHub.services.extend(
    [
        {"name": "binder", "url": "http://tljh-binderhub-service"},
        {
            "name": "tljhrepo2docker",
            "url": "http://r2d-svc:6789",
            "command": [
                sys.executable,
                "-m",
                "tljh_repo2docker",
                "--ip",
                "0.0.0.0",
                "--port",
                "6789",
                "--TljhRepo2Docker.binderhub_url",
                "http://tljh-binderhub-service/services/binder",
            ],
            "oauth_no_confirm": True,
            "oauth_client_allowed_scopes": [
                TLJH_R2D_ADMIN_SCOPE,
            ],
        },
    ]
)

c.JupyterHub.custom_scopes = {
    TLJH_R2D_ADMIN_SCOPE: {
        "description": "Admin access to myservice",
    },
}

c.JupyterHub.load_roles = [
    {
        "description": "Role for tljh_repo2docker service",
        "name": "tljh-repo2docker-service",
        "scopes": [
            "read:users",
            "read:roles:users",
            "admin:servers",
            "access:services!service=binder",
        ],
        "services": ["tljhrepo2docker"],
    },
    {
        "name": "tljh-repo2docker-service-admin",
        "users": ["alice"],
        "scopes": [TLJH_R2D_ADMIN_SCOPE],
    },
    {
        "name": "user",
        "scopes": [
            "self",
            # access to the env page
            "access:services!service=tljhrepo2docker",
        ],
    },
]
