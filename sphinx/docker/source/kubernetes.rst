Kubernetes
==========

Installation
------------

To deploy to ``Kubernetes``, we need the following components installed. On Linux, ``kubectl`` and ``minikube`` are single binary executable files.

* Install `kubectl <https://kubernetes.io/docs/tasks/tools/install-kubectl>`_

   * `documentation <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands>`_
* Install `minikube <https://kubernetes.io/docs/tasks/tools/install-minikube>`_

   * `documentation <https://minikube.sigs.k8s.io/docs/>`_

* Install `VirtualBox <https://www.virtualbox.org>`_

Starting minikube cluster
-------------------------

Start minikube. This command effectively creates a virtual machine.

.. code:: bash

    minikube start

You should see an output like the following.

::

    😄  minikube v1.5.2 on Ubuntu 19.10
    ✨  Automatically selected the 'virtualbox' driver (alternates: [none])
    💿  Downloading VM boot image ...
        > minikube-v1.5.1.iso.sha256: 65 B / 65 B [--------------] 100.00% ? p/s 0s
        > minikube-v1.5.1.iso: 143.76 MiB / 143.76 MiB [] 100.00% 127.66 MiB p/s 2s
    🔥  Creating virtualbox VM (CPUs=2, Memory=2000MB, Disk=20000MB) ...
    🐳  Preparing Kubernetes v1.16.2 on Docker '18.09.9' ...
    💾  Downloading kubeadm v1.16.2
    💾  Downloading kubelet v1.16.2
    🚜  Pulling images ...
    🚀  Launching Kubernetes ... 
    ⌛  Waiting for: apiserver
    🏄  Done! kubectl is now configured to use "minikube"


Quicktest
---------

Deploy through an image
^^^^^^^^^^^^^^^^^^^^^^^

Type in the following to deploy a service through an image.

.. code:: bash

    # create deployment
    kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.10

    # expose deployment as a service
    kubectl expose deployment hello-minikube --type=NodePort --port=8080

    # get pod information
    kubectl get pods
    
    # get the service url
    minikube service hello-minikube --url
    
    # delete service
    kubectl delete services hello-minikube

    # delete deployment
    kubectl delete deployment hello-minikube

Deploy through YAML configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a file called ``pod.yaml``.

.. literalinclude:: _static/code/kubernetes/pod.yml
   :language: yaml
   :linenos:

Then type in the following.

.. code:: bash

    # create deployment
    kubectl apply -f pod.yml

    # get pod information
    kubectl get pods

    # get logs of pod
    kubectl logs demo

    ## delete service
    kubectl delete -f pod.yml

Pod creation
^^^^^^^^^^^^

Create a file called ``pod.yaml``.

.. literalinclude:: _static/code/kubernetes/student.yml
   :language: yaml
   :linenos:
   :emphasize-lines: 2

* `deployment <https://kubernetes.io/docs/concepts/workloads/controllers/deployment>`_
* `define evironment variables <https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/>`_
* `shell access <https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/>`_
* `mounting volumes <https://kubernetes.io/docs/concepts/storage/volumes>`_

.. code:: bash

    # create deployment
    kubectl apply -f student.yml

    # get pod information
    kubectl get pods
    kubectl describe pod student

    # get logs of pod
    kubectl logs student db
    kubectl logs student rest

    # shell access
    kubectl exec -it student --container db -- /bin/bash
    kubectl exec -it student --container rest -- /bin/bash

    ## delete service
    kubectl delete -f student.yml

Deployment creation
^^^^^^^^^^^^^^^^^^^

Build the docker images. 

.. code:: bash

    docker build --no-cache -t db-app:local .
    docker build --no-cache -t rest-app:local .
    docker build --no-cache -t ui-app:local .

Create ``student-deployment.yml`` with the following content.       

.. literalinclude:: _static/code/kubernetes/student-deployment.yml
   :language: yaml
   :linenos:
   :emphasize-lines: 2

.. code:: bash

    # create deployment
    kubectl create -f student-deployment.yml

    # get pod information
    kubectl get pods
    kubectl describe pod student-deployment-65944d97cd-x2x9j

    # shell access
    kubectl exec -it student-deployment-65944d97cd-x2x9j --container db -- /bin/bash
    kubectl exec -it student-deployment-65944d97cd-x2x9j --container rest -- /bin/bash

    # forward port
    kubectl port-forward student-deployment-65944d97cd-x2x9j 5000:5000

    ## delete service
    kubectl delete -f student-deployment.yml

Using local images
------------------

The following command enables us to reuse Minikube's built-in docker daemon. This feature is useful to avoid building a Docker registry and pushing images into it. When you issue ``docker ps`` you will see the containers running on Minikube.

.. code:: bash

    eval $(minikube docker-env)    

Useful notes and commands
-------------------------

* ``minikube dashboard`` brings up the Kubernetes dashboard
* ``minikube ssh`` will SSH into the virutal machine
* ``kubectl get deployment`` gets the deployments in the cluster
* ``kubectl get events`` gets the events in the cluster
* ``kubectl get svc`` checks the services created
* ``/home`` (local) is mounted ``/hosthome`` (virtual machine)
* addons in ``~/.minikube/addons`` (local) will be moved to the virtual machine on Minikube start/restart


Removing minikube cluster
-------------------------

Stop minikube. This command effectively halts the virtual machine.

.. code:: bash

    minikube stop

Delete minikube. This command effectively deletes the virtual machine.

.. code:: bash

    minikube delete