## Helm command

```bash
helm upgrade --cleanup-on-fail --install tljh . --wait --set-file jupyterhub.hub.extraFiles.my_jupyterhub_config.stringData=./jupyterhub_config.py --set binderhub-service.buildPodsRegistryCredentials.password=xxx --set binderhub-service.buildPodsRegistryCredentials.username=xxx
```
