Kubernetes
==========

Kubernetes schedules containers across a cluster and keeps the declared state running. Docker builds and publishes the images; Kubernetes pulls those images and manages Pods, Deployments, Services, ConfigMaps, Secrets, storage, rollout history, and health checks.

Install tools
-------------

Install ``kubectl`` and choose a local cluster.

* `kubectl <https://kubernetes.io/docs/tasks/tools/>`_
* `minikube <https://minikube.sigs.k8s.io/docs/start/>`_
* `kind <https://kind.sigs.k8s.io/>`_
* Docker Desktop Kubernetes

Start a local minikube cluster with the Docker driver.

.. code-block:: bash
    :linenos:

    minikube start --driver=docker

Check the cluster.

.. code-block:: bash
    :linenos:

    kubectl version --client
    kubectl cluster-info
    kubectl get nodes

Build and load local images
---------------------------

For local Kubernetes, either push images to a registry or load local images into the cluster.

.. code-block:: bash
    :linenos:

    docker build -t student-rest:local ./flask
    minikube image load student-rest:local

With kind, load the image into the named cluster.

.. code-block:: bash
    :linenos:

    kind load docker-image student-rest:local --name kind

Deployment and Service
----------------------

A ``Deployment`` manages replicated Pods. A ``Service`` gives those Pods a stable network name and virtual IP.

.. code-block:: yaml
    :linenos:

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: student-rest
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: student-rest
      template:
        metadata:
          labels:
            app: student-rest
        spec:
          containers:
            - name: rest
              image: student-rest:local
              imagePullPolicy: IfNotPresent
              ports:
                - containerPort: 5000
              readinessProbe:
                httpGet:
                  path: /
                  port: 5000
              livenessProbe:
                httpGet:
                  path: /
                  port: 5000
              resources:
                requests:
                  cpu: 100m
                  memory: 128Mi
                limits:
                  cpu: 500m
                  memory: 512Mi
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: student-rest
    spec:
      selector:
        app: student-rest
      ports:
        - port: 80
          targetPort: 5000

Apply the manifest and inspect the workload.

.. code-block:: bash
    :linenos:

    kubectl apply -f student-rest.yaml
    kubectl get deployments
    kubectl get pods
    kubectl get services
    kubectl rollout status deployment/student-rest

Forward the Service to the local machine.

.. code-block:: bash
    :linenos:

    kubectl port-forward service/student-rest 8080:80

Open `http://localhost:8080 <http://localhost:8080>`_.

Rollouts
--------

Deploy a new image by changing the image in the Deployment.

.. code-block:: bash
    :linenos:

    kubectl set image deployment/student-rest rest=student-rest:next
    kubectl rollout status deployment/student-rest
    kubectl rollout history deployment/student-rest
    kubectl rollout undo deployment/student-rest

Configuration and secrets
-------------------------

Use ConfigMaps for non-secret configuration.

.. code-block:: bash
    :linenos:

    kubectl create configmap student-config \
        --from-literal=APP_ENV=local \
        --dry-run=client -o yaml > configmap.yaml

Use Secrets for sensitive values, then mount or expose them to Pods through Kubernetes. Production clusters should integrate with the cloud provider's secret manager when available.

.. code-block:: bash
    :linenos:

    kubectl create secret generic db-credentials \
        --from-literal=username=student \
        --from-literal=password='change-me' \
        --dry-run=client -o yaml > secret.yaml

Pods and sidecars
-----------------

A Pod is the smallest Kubernetes scheduling unit. Put multiple containers in one Pod only when they must share lifecycle, network namespace, and storage. A frontend, API, and database should usually be separate Deployments and Services. Sidecars, log shippers, and local proxies are better examples of multi-container Pods.

Operations
----------

These commands are used constantly.

.. code-block:: bash
    :linenos:

    kubectl config get-contexts
    kubectl config use-context minikube
    kubectl create namespace docker-book
    kubectl get all -n docker-book
    kubectl describe pod <pod-name> -n docker-book
    kubectl logs deployment/student-rest -n docker-book
    kubectl exec -it deployment/student-rest -n docker-book -- sh
    kubectl delete -f student-rest.yaml

Using local images
------------------

The older ``eval $(minikube docker-env)`` workflow points the local Docker CLI at the minikube Docker daemon. Prefer ``minikube image load`` for new local workflows because it is explicit and works naturally with Buildx-built images.

.. code-block:: bash
    :linenos:

    minikube image load student-rest:local

Useful minikube commands:

* ``minikube dashboard`` opens the Kubernetes dashboard.
* ``minikube ssh`` opens a shell on the minikube node.
* ``minikube service <service-name>`` opens a Service exposed through minikube.
* ``kubectl get events --sort-by=.metadata.creationTimestamp`` shows recent cluster events.

Removing minikube cluster
-------------------------

Stop minikube. This command effectively halts the virtual machine.

.. code-block:: bash
    :linenos:

    minikube stop

Delete minikube. This command effectively deletes the virtual machine.

.. code-block:: bash
    :linenos:

    minikube delete

References
----------

* `Kubernetes Deployments <https://kubernetes.io/docs/concepts/workloads/controllers/deployment/>`_
* `Kubernetes Services <https://kubernetes.io/docs/concepts/services-networking/service/>`_
* `kubectl reference <https://kubernetes.io/docs/reference/kubectl/>`_
* `minikube image load <https://minikube.sigs.k8s.io/docs/commands/image/>`_
