FROM quay.io/jupyterhub/k8s-hub:3.3.7

USER root
RUN curl -fsSL https://deb.nodesource.com/setup_current.x | bash - && \
    apt-get install -y nodejs
RUN python3 -m pip install https://api.github.com/repos/plasmabio/tljh-repo2docker/zipball/pull/83/head

USER ${NB_USER}