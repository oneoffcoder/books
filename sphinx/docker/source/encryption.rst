Encryption
==========

Although container encryption technology is still in its infancy, you can encrypt your containers at rest. As of 9/2021, Docker Hub does not support encrypted containers being published to it, but, IBM's Container Registry does. Container encryption requires tools from different projects to make the encryption work; the procedure is not a fluid process like with building and publishing normal, non-encrypted containers.

Here are the tools that you will need, and the versions tested and used are also listed.

.. list-table:: Container Encryption Tools
    :widths: 20 20 60
    :header-rows: 1

    * - Name
      - Version
      - Purpose
    * - `docker <https://www.docker.com/>`_
      - 20.10.8
      - Docker containerization tools.
    * - `go <https://golang.org/>`_
      - 1.17.1
      - Programming language to compile/build ``imgcrypt``.
    * - `imgcrypt <https://github.com/containerd/imgcrypt>`_
      - 1.1.1-17-g967ee1f
      - CLI drop-in replacement for ``ctr`` to interact with ``containerd``.
    * - `nerdctl <https://github.com/containerd/nerdctl>`_
      - 0.11.2
      - CLI drop-in replacement for ``docker`` CLI.
    * - `cni <https://github.com/containernetworking/plugins>`_
      - 1.0.1
      - Additional networking plugin components.

Setup tools
-----------

go
^^

The ``go`` runtime is really only needed to compile ``imgcrypt``. First, download go and extract the contents to ``/usr/local``.

.. code:: bash

    wget -c https://golang.org/dl/go1.17.1.linux-amd64.tar.gz -O - | sudo tar -xz -C /usr/local

Then, modify your path to include the go binaries. For example, modify your ``.bashrc`` as follows.

.. code:: bash

    GO_HOME=/usr/local/go
    PATH="$GO_HOME/bin:$PATH"

imgcrypt
^^^^^^^^

Clone the imgcrypt repository.

.. code:: bash

    git clone https://github.com/containerd/imgcrypt.git

Then, go into the imgcrypt directory, and then build and install it.

.. code:: bash

    make && sudo make install

Two binaries should be placed in your ``/usr/local/bin`` folder.

- ``ctr-enc``: CLI drop-in replacement for ``ctr`` to interact with ``containerd``.
- ``ctd-decoder``: Tool to decrypt the encrypted container layers.

nerdctl
^^^^^^^

Now, download the binary release of nerdctl and extract its content to ``/usr/local/bin``.

.. code:: bash

    wget https://github.com/containerd/nerdctl/releases/download/v0.11.2/nerdctl-0.11.2-linux-amd64.tar.gz
    tar Cxzvvf /usr/local/bin nerdctl-0.11.2-linux-amd64.tar.gz


cni
^^^

Download the cni tools and extract them to ``/opt/cni/bin``. These tools support nerdctl to work properly.

.. code:: bash

    sudo mkdir /opt/cni/bin
    wget https://github.com/containernetworking/plugins/releases/download/v1.0.1/cni-plugins-linux-amd64-v1.0.1.tgz
    sudo tar -xzvf cni-plugins-linux-amd64-v1.0.1.tgz /opt/cni/bin

Configuration
-------------

There is one configuration you need to make for ``containerd``. Modify ``/etc/containerd/config.toml`` to look like the following.

.. code:: toml

    disabled_plugins = ["cri"]

    [grpc]
    uid = 0
    gid = 0

    [stream_processors]
        [stream_processors."io.containerd.ocicrypt.decoder.v1.tar.gzip"]
            accepts = ["application/vnd.oci.image.layer.v1.tar+gzip+encrypted"]
            returns = "application/vnd.oci.image.layer.v1.tar+gzip"
            path = "/usr/local/bin/ctd-decoder"
        [stream_processors."io.containerd.ocicrypt.decoder.v1.tar"]
            accepts = ["application/vnd.oci.image.layer.v1.tar+encrypted"]
            returns = "application/vnd.oci.image.layer.v1.tar"
            path = "/usr/local/bin/ctd-decoder"

After you modify this file, restart the ``containerd`` daemon.

.. code:: bash

    sudo containerd -c /etc/containerd/config.toml

Encryption keys
---------------

You will need to generate a private and public key pair to decrypt/encrypt your container (layers), respectively.

.. code:: bash

    openssl genrsa --out private.pem
    openssl rsa -in private.pem -pubout -out public.pem

Local registry
--------------
We will be publishing our encrypted images to a local registry. For this purpose, we will need to pull the registry image and run it.

.. code:: bash

    docker pull registry:latest
    docker run -d -p 5000:5000 --restart=always --name registry registry

Note that this registry instance is ``localhost:5000``. 

Use Case
--------

The fun finally begins. Let's explain the use case. We have 2 containers that we want to encrypt.

- ``rest``: is a FastAPI REST-ful application
- ``www``: is an Angular application

The rest application has one endpoint ``/num`` and it generates random number. The www application consumes the rest application's endpoint and display the numbers. This separation of backend and frontend applications is typical in deployment settings. Download the project files below.

- :download:`rest <_static/downloads/encryption/rest.zip>`
- :download:`www <_static/downloads/encryption/www.zip>`

Each of these projects have their own ``Dockerfile``. Let's encrypt the rest container. Notice the process: build, tag, push, encrypt. Also, notice the mix and match of tools: docker and ctr-enc.

.. code:: bash

    # go into the rest application's folder
    cd rest

    # build the docker container
    docker build -t rest:local .

    # tag the docker container
    docker tag rest:local localhost:5000/rest:latest

    # push the docker container
    docker image push localhost:5000/rest:latest

    # encrypt the docker container
    sudo ctr-enc images encrypt \
        --recipient jwe:public.pem \
        --platform linux/amd64 \
        localhost:5000/rest:latest \
        localhost:5000/rest.enc:latest

Let's encrypt the www container.

.. code:: bash

    # go into the www application's folder
    cd www

    # build the docker container
    docker build -t www:local .

    # tag the docker container
    docker tag www:local localhost:5000/www:latest

    # push the docker container
    docker image push localhost:5000/www:latest

    # encrypt the docker container
    sudo ctr-enc images encrypt \
        --recipient jwe:public.pem \
        --platform linux/amd64 \
        localhost:5000/www:latest \
        localhost:5000/www.enc:latest

To run these containers, do **NOT** use ``ctr-enc`` as this CLI does not support things like port mapping. You have to use ``nerdctl``, but, as mentioned above, ``nerdctl`` requires the ``cni`` plugins. Fun, right? Have you been noticing the use of ``sudo`` at times too?

.. code:: bash

    sudo nerdctl run --rm -p 8000:80 localhost:5000/rest.enc:latest
    sudo nerdctl run --rm -p 4200:80 localhost:5000/www.enc:latest

Life is easier to bring up dependent containers together with a tool like ``docker-compose``. Well, ``nerdctl`` can do the same. Just define your ``docker-compose.yml`` file as normal.

- :download:`docker-compose.yml <_static/downloads/encryption/docker-compose.yml>`

You may then bring up and down your containers together as follows.

.. code:: bash

    # bring up in the foreground
    sudo nerdctl compose up

    # bring up in the background
    sudo nerdctl compose up -d

    # bring down
    sudo nerdctl compose down

Did you want to transfer your images somewhere else?

.. code:: bash

    sudo nerdctl save localhost:5000/rest.enc:latest > rest.enc.tar
    sudo nerdctl save localhost:5000/www.enc:latest > www.enc.tar

And how do you load these images back up?

.. code:: bash

    sudo nerdctl load < rest.enc.tar
    sudo nerdctl load < www.enc.tar

If you want to inspect the layer information, try doing so for the non-encrypted and encrypted containers.

.. code:: bash

    sudo ctr-enc images layerinfo --platform linux/amd64 localhost:5000/rest:latest

Your output may look like the following::

    #                                                                    DIGEST      PLATFORM        SIZE   ENCRYPTION   RECIPIENTS
    0   sha256:955615a668ce169f8a1443fc6b6e6215f43fe0babfb4790712a2d3171f34d366   linux/amd64    54926871                          
    1   sha256:2756ef5f69a5190f4308619e0f446d95f5515eef4a814dbad0bcebbbbc7b25a8   linux/amd64     5153100                          
    2   sha256:911ea9f2bd51e53a455297e0631e18a72a86d7e2c8e1807176e80f991bde5d64   linux/amd64    10871687                          
    3   sha256:27b0a22ee906271a6ce9ddd1754fdd7d3b59078e0b57b6cc054c7ed7ac301587   linux/amd64    54566834                          
    4   sha256:8584d51a9262f9a3a436dea09ba40fa50f85802018f9bd299eee1bf538481077   linux/amd64   196447011                          
    5   sha256:524774b7d3638702fe9ae0ea3fcfb81b027dfd75cc2fc14f0119e764b9543d58   linux/amd64     6290533                          
    6   sha256:9460f6b75036e38367e2f27bb15e85777c5d6cd52ad168741c9566186415aa26   linux/amd64    16814102                          
    7   sha256:9bc548096c181514aa1253966a330134d939496027f92f57ab376cd236eb280b   linux/amd64         232                          
    8   sha256:1d87379b86b89fd3b8bb1621128f00c8f962756e6aaaed264ec38db733273543   linux/amd64     2349255                          
    9   sha256:1d595206926df4317096d6dbe25db896fd62a9d2c5fc2857de846ce3eda0cdae   linux/amd64         180                          
    10   sha256:3e56765aa5f38be6f6861f23b77d2bd5bc459fe9eaecb1a602cbf74a913862c6   linux/amd64     8854882                          
    11   sha256:9fc979a63c0f09457b5f36602a0c5a29a42bf9e935ad043916bc0aab22f40256   linux/amd64         540                          
    12   sha256:fabab7cf6ac12220f071581ad0a0e2277f052bf1753e00448e1eaa81a4c76a63   linux/amd64         539                          
    13   sha256:8af0214b23936c14b5df3460ba98e9463f8d6ba12c3e5c25bbdd8250ff4d056b   linux/amd64         832                          
    14   sha256:06b69d64c29176f1de6364e1e37ae7a53cd43a58b22c3111595839cd36ae7e5a   linux/amd64         528                          
    15   sha256:2ecccbe80ac56fbc69d0d700eedf61aedf69433ed6df2492bd635e05c5a7ff62   linux/amd64         526                          
    16   sha256:c87ac1122ebeb3d8d12b6a4ea11990d10cdb6548fbceed36bc00bb5a4e1f03c3   linux/amd64         604                          
    17   sha256:3431253c3b0c56355db666a6da035633d7cf06e10a9d57799fa541cb5019af1c   linux/amd64         191                          
    18   sha256:f94fdcc81cced84cdd04867689bc925ac599f1e90cfa7fbc2304f9b2c8755619   linux/amd64    14298306                          
    19   sha256:4ec7208dcd647dc34720a28106c64d21ccbc616687df1ad1421e2397394f7e26   linux/amd64         322                          
    20   sha256:52c6d80960651f438a50c8841373a1f787e0ebbb85450db9b40043792596a18e   linux/amd64         536

And for the encrypted image.

.. code:: bash

    sudo ctr-enc images layerinfo --platform linux/amd64 localhost:5000/rest.enc:latest

Your output may look like the following::

    #                                                                    DIGEST      PLATFORM        SIZE   ENCRYPTION   RECIPIENTS
    0   sha256:cb96ebf5075d177fe16c28941cd77587bbe0315176fe15facae0b85ab02f1e8a   linux/amd64    54926871          jwe        [jwe]
    1   sha256:81a6ed1fb734a65639134f1d0a7f6602d517b82aa60d2b81fba8d8e3af3e683b   linux/amd64     5153100          jwe        [jwe]
    2   sha256:da24335a67b6359f6d1cc42fcc93e3ab20232fec7d80244951f9960396148c53   linux/amd64    10871687          jwe        [jwe]
    3   sha256:9a81845908d957c9fd7803a3c06f576cf45499c87d5fba742a2d033f94df3116   linux/amd64    54566834          jwe        [jwe]
    4   sha256:8557fe23793b2d0326ca0dad82c8e38cd16d29cf69a48db40e6614728c2bcd8d   linux/amd64   196447011          jwe        [jwe]
    5   sha256:2e7430e1490679a367604507627ce4c4c8c8f0c5dcda8c78fb4716f4f0713ead   linux/amd64     6290533          jwe        [jwe]
    6   sha256:71f0584ec7068ff8ec3d8f143d5b4c3abc8eaaf4e3ac23c5f8305dc5360674c3   linux/amd64    16814102          jwe        [jwe]
    7   sha256:6549170b2dbe9e6922b8871295c186eba273cd283b4a49ec4ad4134ea5d7bfc9   linux/amd64         232          jwe        [jwe]
    8   sha256:002998a908a9eeda0cc308fb04dd62124b87d7a0e090a4fe61ce3d38cf88123a   linux/amd64     2349255          jwe        [jwe]
    9   sha256:733922c8d437833c7282020725c555938d07e5201516e44bd8daa504a38bc316   linux/amd64         180          jwe        [jwe]
    10   sha256:228074b98ea26918afc8872e0bd72521660bd5ea2a0493a3696a8525234019e7   linux/amd64     8854882          jwe        [jwe]
    11   sha256:d79d1e81e9c4820a0f007a628b9f203ce201fe709721e779f6da194819481968   linux/amd64         540          jwe        [jwe]
    12   sha256:96899b9a2f1985f92b9bb955c057d850337f301ce457e413039d6e0a049a090e   linux/amd64         539          jwe        [jwe]
    13   sha256:df315b7b1322f54d3d9ad36a5151231db942f49f95ce1140a4fc6e591c78c2f5   linux/amd64         832          jwe        [jwe]
    14   sha256:1d19625ba4e04e502cbe9ad3daf75612e0f89e764b24a2867d5d317ee82d6e3d   linux/amd64         528          jwe        [jwe]
    15   sha256:b51c1939737b2e8ea219c389322fc6586d8ec2d2dc36ca3bd6a547834cbc1282   linux/amd64         526          jwe        [jwe]
    16   sha256:4bb16b8369e2fd3b31bfffb94192e81f8285e5542aebfe876e22ffe1f1e5d105   linux/amd64         604          jwe        [jwe]
    17   sha256:174b809acd599c61bcfada6b911bc1092bce5863baeb9df19050fb546156748b   linux/amd64         191          jwe        [jwe]
    18   sha256:61a4a82c7382d50349b84570bf9095e113a6e68135edf4185c38ea2d3f560bf4   linux/amd64    14298306          jwe        [jwe]
    19   sha256:85cc8ff75ea43abb871585b38a872aa1d2a78bbe42f0f83a2caaf1f3926487ba   linux/amd64         322          jwe        [jwe]
    20   sha256:6cc9de7b0dba162976a6505356db2e10681cf3618faae574a491a6931d555b27   linux/amd64         536          jwe        [jwe]

This stuff is magical!