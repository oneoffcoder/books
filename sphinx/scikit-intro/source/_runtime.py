from __future__ import annotations

import importlib.metadata
import os
from pathlib import Path

import nltk
import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.datasets import (
    load_breast_cancer,
    load_diabetes,
    make_classification,
    make_multilabel_classification,
)
from sklearn.utils import Bunch


def _env_flag(name: str, default: str = "0") -> bool:
    return os.environ.get(name, default).strip().lower() in {"1", "true", "yes", "on"}


SCIKIT_INTRO_CHECK_MODE = _env_flag("SCIKIT_INTRO_CHECK_MODE", "0")
SCIKIT_INTRO_RUN_REMOTE_DATASETS = _env_flag("SCIKIT_INTRO_RUN_REMOTE_DATASETS", "0")


def data_dir() -> Path:
    root = os.environ.get("SCIKIT_INTRO_DATA_DIR")
    path = (
        Path(root)
        if root
        else Path(__file__).resolve().parents[1] / "build" / "notebook-cache" / "data"
    )
    path.mkdir(parents=True, exist_ok=True)
    return path


def should_run_remote_assets() -> bool:
    return not SCIKIT_INTRO_CHECK_MODE or SCIKIT_INTRO_RUN_REMOTE_DATASETS


def rpy2_version() -> str:
    return importlib.metadata.version("rpy2")


def ensure_nltk_data() -> None:
    downloads = {
        "punkt_tab": "tokenizers/punkt_tab",
        "stopwords": "corpora/stopwords",
        "wordnet": "corpora/wordnet",
        "omw-1.4": "corpora/omw-1.4",
        "averaged_perceptron_tagger_eng": "taggers/averaged_perceptron_tagger_eng",
        "tagsets": "help/tagsets/upenn_tagset.pickle",
        "tagsets_json": "help/tagsets_json/PY3_json/upenn_tagset.json",
    }
    nltk_cache = data_dir() / "nltk_data"
    nltk_cache.mkdir(parents=True, exist_ok=True)

    if str(nltk_cache) not in nltk.data.path:
        nltk.data.path.insert(0, str(nltk_cache))

    for package, resource in downloads.items():
        try:
            nltk.data.find(resource)
        except LookupError:
            nltk.download(package, download_dir=str(nltk_cache), quiet=True)


def get_mlflow_tracking_uri() -> str:
    return (data_dir() / "mlflow").resolve().as_uri()


def graph_layout(graph, layout: str = "dot", *, seed: int = 37):
    import networkx as nx

    requested = layout or "dot"

    try:
        return nx.nx_agraph.graphviz_layout(graph, prog=requested)
    except Exception:
        pass

    try:
        return nx.nx_pydot.graphviz_layout(graph, prog=requested)
    except Exception:
        pass

    fallback_layouts = {
        "circo": nx.circular_layout,
        "dot": nx.shell_layout,
        "fdp": nx.spring_layout,
        "neato": nx.kamada_kawai_layout,
        "osage": nx.shell_layout,
        "patchwork": nx.spectral_layout,
        "sfdp": nx.spring_layout,
        "twopi": nx.spiral_layout,
    }
    func = fallback_layouts.get(requested, nx.spring_layout)

    try:
        return func(graph, seed=seed)
    except TypeError:
        return func(graph)


def load_california_housing_data(*, return_X_y: bool = True, as_frame: bool = False):
    if should_run_remote_assets():
        from sklearn.datasets import fetch_california_housing

        return fetch_california_housing(return_X_y=return_X_y, as_frame=as_frame)

    feature_names = [
        "MedInc",
        "HouseAge",
        "AveRooms",
        "AveBedrms",
        "Population",
        "AveOccup",
        "Latitude",
        "Longitude",
    ]
    X_frame, y_series = load_diabetes(return_X_y=True, as_frame=True)
    X_frame = X_frame.iloc[:, : len(feature_names)].copy()
    X_frame.columns = feature_names
    y_series = y_series.rename("MedHouseVal")

    if return_X_y:
        if as_frame:
            return X_frame, y_series
        return X_frame.to_numpy(), y_series.to_numpy()

    if as_frame:
        frame = X_frame.copy()
        frame["MedHouseVal"] = y_series
        return Bunch(
            data=X_frame,
            target=y_series,
            frame=frame,
            feature_names=feature_names,
            target_names=["MedHouseVal"],
            DESCR="Fallback local dataset used in notebook check mode instead of the remote California housing dataset.",
        )

    return Bunch(
        data=X_frame.to_numpy(),
        target=y_series.to_numpy(),
        feature_names=feature_names,
        target_names=["MedHouseVal"],
        DESCR="Fallback local dataset used in notebook check mode instead of the remote California housing dataset.",
    )


def load_20newsgroups_vectorized_data(*, subset: str, return_X_y: bool = True):
    if should_run_remote_assets():
        from sklearn.datasets import fetch_20newsgroups_vectorized

        return fetch_20newsgroups_vectorized(subset=subset, return_X_y=return_X_y)

    n_samples = 256 if subset == "train" else 128
    rng = np.random.default_rng(37 if subset == "train" else 38)
    X = sparse.random(
        n_samples,
        512,
        density=0.04,
        random_state=rng,
        format="csr",
    )
    y = rng.integers(0, 20, size=n_samples)
    return (X, y) if return_X_y else Bunch(data=X, target=y)


def load_covtype_data(*, return_X_y: bool = True):
    if should_run_remote_assets():
        from sklearn.datasets import fetch_covtype

        return fetch_covtype(return_X_y=return_X_y)

    X, y = make_classification(
        n_samples=1024,
        n_features=54,
        n_informative=12,
        n_redundant=4,
        n_classes=7,
        n_clusters_per_class=1,
        random_state=37,
    )
    return (X, y) if return_X_y else Bunch(data=X, target=y)


def load_kddcup99_http_data(*, return_X_y: bool = True):
    if should_run_remote_assets():
        from sklearn.datasets import fetch_kddcup99

        return fetch_kddcup99(subset="http", return_X_y=return_X_y)

    X, y = make_classification(
        n_samples=2048,
        n_features=41,
        n_informative=10,
        n_redundant=5,
        random_state=37,
    )
    return (X, y) if return_X_y else Bunch(data=X, target=y)


def make_shap_classification_frame(*, n_samples: int = 100, random_state: int = 37):
    X, y = make_classification(
        n_samples=n_samples,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_repeated=0,
        n_classes=2,
        n_clusters_per_class=1,
        class_sep=1.5,
        random_state=random_state,
    )
    df = pd.DataFrame(X, columns=["x0", "x1"])
    df["y"] = y
    return df


def load_rcv1_data(*, subset: str, return_X_y: bool = True):
    if should_run_remote_assets():
        from sklearn.datasets import fetch_rcv1

        return fetch_rcv1(subset=subset, return_X_y=return_X_y)

    n_samples = 256 if subset == "train" else 128
    X, y = make_multilabel_classification(
        n_samples=n_samples,
        n_features=256,
        n_classes=40,
        n_labels=3,
        sparse=True,
        return_indicator="sparse",
        random_state=37 if subset == "train" else 38,
    )
    return (X, y) if return_X_y else Bunch(data=X, target=y)


def load_openml_miceprotein():
    if should_run_remote_assets():
        from sklearn.datasets import fetch_openml

        return fetch_openml(name="miceprotein", version=4)

    data = load_breast_cancer(as_frame=True)
    return Bunch(
        data=data.data,
        target=data.target.astype(str),
        DESCR="Fallback local dataset used in notebook check mode instead of the remote OpenML miceprotein dataset.",
    )
