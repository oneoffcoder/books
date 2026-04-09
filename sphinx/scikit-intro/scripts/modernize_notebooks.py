from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"


def replace_all(text: str) -> str:
    replacements = {
        "loss='log'": "loss='log_loss'",
        "np.NaN": "np.nan",
        "dtype=np.int": "dtype=int",
        "astype({k: np.float for k in df.columns if k != 'species'})": "astype({k: float for k in df.columns if k != 'species'})",
        ".get_feature_names()": ".get_feature_names_out()",
        "w2v_model.wv.index2word": "w2v_model.wv.index_to_key",
        "model.wv.index2word": "model.wv.index_to_key",
        "d2v_model.docvecs": "d2v_model.dv",
        "'size': 5": "'vector_size': 5",
        "'iter': 5000": "'epochs': 5000",
        "wm_model2.init_sims(replace=True)": "wm_model2.fill_norms(force=True)",
        "print(rpy2.__version__)": "from _runtime import rpy2_version\n\nprint(rpy2_version())",
        "OneHotEncoder(handle_unknown='ignore', sparse=False)": "OneHotEncoder(handle_unknown='ignore', sparse_output=False)",
        "stop_words=stop_words": "stop_words=sorted(stop_words)",
        "tsne = TSNE(n_components=num_dimensions, random_state=0)": "tsne = TSNE(n_components=num_dimensions, perplexity=max(5, min(30, len(vectors) - 1)), random_state=0)",
        ".todense()": ".toarray()",
        "{'newshape':-1}": "{'shape': (-1,)}",
        "docs = list(df.valid)\n": "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\ndocs = list(df.valid)[:6] if SCIKIT_INTRO_CHECK_MODE else list(df.valid)\n",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def replace_exact_source(nb_name: str, old: str, new: str) -> None:
    path = SOURCE / nb_name
    notebook = json.loads(path.read_text())
    changed = False
    for cell in notebook["cells"]:
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        normalized = source.strip()
        if normalized == new.strip():
            changed = True
            continue
        if normalized == old.strip():
            cell["source"] = [line for line in new.splitlines(keepends=True)]
            changed = True
    if not changed:
        raise RuntimeError(f"Did not find expected cell in {nb_name}")
    path.write_text(json.dumps(notebook, indent=1, ensure_ascii=True) + "\n")


def replace_cell_containing(nb_name: str, needle: str, new: str) -> None:
    path = SOURCE / nb_name
    notebook = json.loads(path.read_text())
    changed = False
    for cell in notebook["cells"]:
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        if source.strip() == new.strip():
            changed = True
            break
        if needle in source:
            cell["source"] = [line for line in new.splitlines(keepends=True)]
            changed = True
            break
    if not changed:
        raise RuntimeError(f"Did not find cell containing {needle!r} in {nb_name}")
    path.write_text(json.dumps(notebook, indent=1, ensure_ascii=True) + "\n")


def rewrite_notebook(path: Path) -> None:
    notebook = json.loads(path.read_text())
    changed = False
    for cell in notebook["cells"]:
        if cell.get("cell_type") != "code":
            continue
        original = "".join(cell.get("source", []))
        updated = replace_all(original)
        if updated != original:
            cell["source"] = [line for line in updated.splitlines(keepends=True)]
            changed = True
    if changed:
        path.write_text(json.dumps(notebook, indent=1, ensure_ascii=True) + "\n")


def main() -> None:
    for path in sorted(SOURCE.glob("*.ipynb")):
        if path.name.startswith("_"):
            continue
        rewrite_notebook(path)

    replace_exact_source(
        "autoviz.ipynb",
        "from sklearn.datasets import fetch_california_housing\n\nX, y = fetch_california_housing(return_X_y=True, as_frame=True)\nX['MedHouseVal'] = y\n",
        "from _runtime import load_california_housing_data\n\nX, y = load_california_housing_data(return_X_y=True, as_frame=True)\nX['MedHouseVal'] = y\n",
    )
    replace_exact_source(
        "plot-mosaic.ipynb",
        "from sklearn.datasets import fetch_california_housing\n\nX, y = fetch_california_housing(return_X_y=True, as_frame=True)\n",
        "from _runtime import load_california_housing_data\n\nX, y = load_california_housing_data(return_X_y=True, as_frame=True)\n",
    )
    replace_exact_source(
        "customized-estimators.ipynb",
        "from sklearn.datasets import fetch_california_housing\n\nX, y = fetch_california_housing(return_X_y=True, as_frame=True)\n",
        "from _runtime import load_california_housing_data\n\nX, y = load_california_housing_data(return_X_y=True, as_frame=True)\n",
    )
    replace_exact_source(
        "generate-samples.ipynb",
        "from sklearn.datasets import fetch_california_housing\n\nX, y = fetch_california_housing(return_X_y=True)\n",
        "from _runtime import load_california_housing_data\n\nX, y = load_california_housing_data(return_X_y=True)\n",
    )
    replace_exact_source(
        "generate-samples.ipynb",
        "from sklearn.datasets import fetch_20newsgroups_vectorized\n\nT_X, T_y = fetch_20newsgroups_vectorized(subset='train', return_X_y=True)\nV_X, V_y = fetch_20newsgroups_vectorized(subset='test', return_X_y=True)\n",
        "from _runtime import load_20newsgroups_vectorized_data\n\nT_X, T_y = load_20newsgroups_vectorized_data(subset='train', return_X_y=True)\nV_X, V_y = load_20newsgroups_vectorized_data(subset='test', return_X_y=True)\n",
    )
    replace_exact_source(
        "generate-samples.ipynb",
        "from sklearn.datasets import fetch_covtype\n\nX, y = fetch_covtype(return_X_y=True)\n",
        "from _runtime import load_covtype_data\n\nX, y = load_covtype_data(return_X_y=True)\n",
    )
    replace_exact_source(
        "generate-samples.ipynb",
        "from sklearn.datasets import fetch_kddcup99\n\nX, y = fetch_kddcup99(subset='http', return_X_y=True)\n",
        "from _runtime import load_kddcup99_http_data\n\nX, y = load_kddcup99_http_data(return_X_y=True)\n",
    )
    replace_exact_source(
        "generate-samples.ipynb",
        "from sklearn.datasets import fetch_rcv1\n\nT_X, T_y = fetch_rcv1(subset='train', return_X_y=True)\nV_X, V_y = fetch_rcv1(subset='test', return_X_y=True)\n",
        "from _runtime import load_rcv1_data\n\nT_X, T_y = load_rcv1_data(subset='train', return_X_y=True)\nV_X, V_y = load_rcv1_data(subset='test', return_X_y=True)\n",
    )
    replace_exact_source(
        "generate-samples.ipynb",
        "from sklearn.datasets import fetch_openml\n\nmice = fetch_openml(name='miceprotein', version=4)\nX, y = mice.data, mice.target\n\nprint(mice.DESCR)\n",
        "from _runtime import load_openml_miceprotein\n\nmice = load_openml_miceprotein()\nX, y = mice.data, mice.target\n\nprint(mice.DESCR)\n",
    )
    replace_exact_source(
        "gensim.ipynb",
        "import string\nfrom nltk import word_tokenize\nfrom nltk.corpus import stopwords\nfrom nltk.stem import WordNetLemmatizer \n  \nlemmatizer = WordNetLemmatizer() \nstop_words = set(stopwords.words('english') + list(string.punctuation))\n\nis_valid = lambda t: t not in stop_words\ntokenize = lambda t: word_tokenize(t.lower())\nlemmatize = lambda t: lemmatizer.lemmatize(t)\n\ndf['normalized'] = df.text.apply(lambda text: [lemmatize(t) for t in tokenize(text) if is_valid(t)])\ndf.shape\n",
        "import string\nfrom nltk import word_tokenize\nfrom nltk.corpus import stopwords\nfrom nltk.stem import WordNetLemmatizer \nfrom _runtime import ensure_nltk_data\n  \nensure_nltk_data()\nlemmatizer = WordNetLemmatizer() \nstop_words = set(stopwords.words('english') + list(string.punctuation))\n\nis_valid = lambda t: t not in stop_words\ntokenize = lambda t: word_tokenize(t.lower())\nlemmatize = lambda t: lemmatizer.lemmatize(t)\n\ndf['normalized'] = df.text.apply(lambda text: [lemmatize(t) for t in tokenize(text) if is_valid(t)])\ndf.shape\n",
    )
    replace_exact_source(
        "gensim.ipynb",
        "import gensim.downloader as api\n\nwm_model1 = api.load('word2vec-google-news-300')\n\nwm_model2 = api.load('word2vec-google-news-300')\nwm_model2.fill_norms(force=True)\n",
        "from copy import deepcopy\nfrom _runtime import should_run_remote_assets\n\nif should_run_remote_assets():\n    import gensim.downloader as api\n\n    wm_model1 = api.load('word2vec-google-news-300')\n    wm_model2 = api.load('word2vec-google-news-300')\nelse:\n    wm_model1 = w2v_model.wv\n    wm_model2 = deepcopy(w2v_model.wv)\n\nwm_model2.fill_norms(force=True)\n",
    )
    replace_exact_source(
        "gensim.ipynb",
        "from gensim.models import Word2Vec\n\nw2v_model = Word2Vec(**{\n    'sentences': BookTitleCorpus(), \n    'vector_size': 5, \n    'window': 1, \n    'min_count': 1, \n    'negative': 1,\n    'epochs': 5000,\n    'compute_loss': True,\n    'hs': 0,\n    'sg': 1,\n    'seed': 37\n})\n",
        "from gensim.models import Word2Vec\nfrom _runtime import SCIKIT_INTRO_CHECK_MODE\n\nw2v_model = Word2Vec(**{\n    'sentences': BookTitleCorpus(), \n    'vector_size': 5, \n    'window': 1, \n    'min_count': 1, \n    'negative': 1,\n    'epochs': 250 if SCIKIT_INTRO_CHECK_MODE else 5000,\n    'compute_loss': True,\n    'hs': 0,\n    'sg': 1,\n    'seed': 37\n})\n",
    )
    replace_exact_source(
        "gensim.ipynb",
        "from gensim.models.doc2vec import TaggedDocument, Doc2Vec\n\ndef read_corpus(tokens_only=False):\n    for i, tokens in enumerate(df.valid):\n        if tokens_only:\n            yield tokens\n        else:\n            yield TaggedDocument(tokens, [i])\n                \ntr_corpus = list(read_corpus())\nte_corpus = list(read_corpus(True))\n\nd2v_model = Doc2Vec(vector_size=5, min_count=1, epochs=8000)\nd2v_model.build_vocab(tr_corpus)\nd2v_model.train(tr_corpus, total_examples=d2v_model.corpus_count, epochs=d2v_model.epochs)\n",
        "from gensim.models.doc2vec import TaggedDocument, Doc2Vec\nfrom _runtime import SCIKIT_INTRO_CHECK_MODE\n\ndef read_corpus(tokens_only=False):\n    for i, tokens in enumerate(df.valid):\n        if tokens_only:\n            yield tokens\n        else:\n            yield TaggedDocument(tokens, [i])\n                \ntr_corpus = list(read_corpus())\nte_corpus = list(read_corpus(True))\n\nd2v_model = Doc2Vec(vector_size=5, min_count=1, epochs=500 if SCIKIT_INTRO_CHECK_MODE else 8000)\nd2v_model.build_vocab(tr_corpus)\nd2v_model.train(tr_corpus, total_examples=d2v_model.corpus_count, epochs=d2v_model.epochs)\n",
    )
    replace_cell_containing(
        "nltk.ipynb",
        "from nltk.corpus import stopwords",
        "from nltk.corpus import stopwords\nfrom sklearn.feature_extraction.text import CountVectorizer\nimport pandas as pd\nfrom _runtime import ensure_nltk_data\n\nensure_nltk_data()\nstop_words = set(stopwords.words('english'))\n\nvectorizer = CountVectorizer(binary=True, stop_words=sorted(stop_words))\nX = vectorizer.fit_transform(text).todense()\n\nbool_df = pd.DataFrame(X, columns=vectorizer.get_feature_names_out())\n\nprint(bool_df.shape)\nbool_df.columns\n",
    )
    replace_cell_containing(
        "mlflow.ipynb",
        "tracking_uri = 'http://localhost:5001'",
        "import mlflow\nfrom mlflow.exceptions import MlflowException\nfrom mlflow.models.signature import infer_signature\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom _runtime import get_mlflow_tracking_uri\n\nplt.style.use('ggplot')\n\nexperiment_name = 'test1'\ntracking_uri = get_mlflow_tracking_uri()\nmlflow.set_tracking_uri(tracking_uri)\n\nif not mlflow.get_experiment_by_name(experiment_name):\n    try:\n        mlflow.create_experiment(experiment_name)\n    except MlflowException as ex:\n        print(f'{ex}')\n\nmlflow.set_experiment(experiment_name)\n\nwith mlflow.start_run() as run:\n    model = get_model()\n    model.fit(X_tr, y_tr)\n    \n    signature = infer_signature(X_tr, model.predict_proba(X_tr))\n    mlflow.sklearn.log_model(model, 'model', signature=signature)\n    mlflow.log_params(model.best_params_)\n    \n    perf_metrics = get_performances(X_tr, y_tr, X_te, y_te, model)\n    mlflow.log_metrics(perf_metrics)\n    \n    pd.DataFrame({k: model.cv_results_[k] for k in model.cv_results_ if k not in {'params'}}) \\\n        .to_csv('./_temp/cv-results.csv', index=False)\n    mlflow.log_artifact('./_temp/cv-results.csv', 'artifact')\n    \n    temp = pd.concat([\n        pd.DataFrame({'y': y_tr}).assign(fold='tr'),\n        pd.DataFrame({'y': y_te}).assign(fold='te')\n    ]).assign(n=1).groupby(['fold', 'y'])['n'].sum().to_frame().reset_index()\n    fig, ax = plt.subplots()\n    sns.barplot(x='fold', hue='y', y='n', data=temp, ax=ax)\n    ax.set_title('Class Distributions')\n    mlflow.log_figure(fig, 'fig/00-class-distributions.png')\n    \n    fig, ax = plt.subplots(1, 2, figsize=(10, 3.5))\n    X_tr.plot(kind='kde', ax=ax[0], title='Feature Distributions, TR')\n    X_te.plot(kind='kde', ax=ax[1], title='Feature Distributions, TE')\n    plt.tight_layout()\n    mlflow.log_figure(fig, 'fig/01-feature-distributions.png')\n    \n    fig, ax = plt.subplots(1, 2, figsize=(10, 3.5))\n    sns.heatmap(X_tr.corr(), ax=ax[0])\n    sns.heatmap(X_te.corr(), ax=ax[1])\n    ax[0].set_title('Correlogram, TR')\n    ax[1].set_title('Correlogram, TE')\n    plt.tight_layout()\n    mlflow.log_figure(fig, 'fig/02-correlograms.png')\n    \n    fig = sns.pairplot(X_tr.assign(y=y_tr), hue='y').fig\n    mlflow.log_figure(fig, 'fig/03-00-tr-pairplot.png')\n    \n    fig = sns.pairplot(X_te.assign(y=y_te), hue='y').fig\n    mlflow.log_figure(fig, 'fig/03-01-te-pairplot.png')\n    \n    fig, ax = plt.subplots(2, 1, figsize=(15, 5.5))\n    pd.plotting.parallel_coordinates(X_tr.assign(y=y_tr), 'y', X_tr.columns, color=['#2e8ad8', '#cd3785'], sort_labels=True, ax=ax[0])\n    pd.plotting.parallel_coordinates(X_te.assign(y=y_te), 'y', X_te.columns, color=['#2e8ad8', '#cd3785'], sort_labels=True, ax=ax[1])\n    ax[0].set_title('Parallel Coordinates, TR')\n    ax[1].set_title('Parallel Coordinates, TE')\n    plt.tight_layout()\n    mlflow.log_figure(fig, 'fig/04-parallel-coordinate.png')\n    \n    run_id = mlflow.active_run().info.run_id\n",
    )
    replace_cell_containing(
        "mlflow.ipynb",
        "tracking_uri='http://localhost:5001'",
        "from joblib import Parallel, delayed\nfrom _runtime import get_mlflow_tracking_uri\n\ndef do_learn(penalty, C, path_tr, path_te, tracking_uri=None, experiment_name='test2'):\n    def get_Xy(path):\n        df = pd.read_csv(path)\n        y_col = 'y'\n        X_cols = [c for c in df.columns if c != y_col]\n        \n        X, y = df[X_cols], df[y_col]\n        return X, y\n    \n    X_tr, y_tr = get_Xy(path_tr)\n    X_te, y_te = get_Xy(path_te)\n    tracking_uri = tracking_uri or get_mlflow_tracking_uri()\n    \n    model_params = {\n        'solver': 'saga',\n        'penalty': penalty,\n        'C': C,\n        'random_state': 37,\n        'max_iter': 1_000\n    }\n    model = LogisticRegression(**model_params)\n\n    mlflow.set_tracking_uri(tracking_uri)\n\n    if not mlflow.get_experiment_by_name(experiment_name):\n        try:\n            mlflow.create_experiment(experiment_name)\n        except MlflowException as ex:\n            print(f'{ex}')\n\n    mlflow.set_experiment(experiment_name)\n\n    with mlflow.start_run() as run:\n        model.fit(X_tr, y_tr)\n\n        signature = infer_signature(X_tr, model.predict_proba(X_tr))\n        mlflow.sklearn.log_model(model, 'model', signature=signature)\n        mlflow.log_params(model_params)\n\n        perf_metrics = get_performances(X_tr, y_tr, X_te, y_te, model)\n        mlflow.log_metrics(perf_metrics)\n    \n        run_id = mlflow.active_run().info.run_id\n        \n    return run_id\n\n\nsize = 100\nC = np.random.uniform(size=size)\nP = np.random.uniform(size=size)\nP = np.select([P < 0.5, P >= 0.5], ['l1', 'l2'])\n\nrun_ids = Parallel(n_jobs=-1)(delayed(do_learn)(p, c, path_tr, path_te) for p, c in zip(P, C))\nprint(run_ids)\n",
    )
    replace_exact_source(
        "hyperparam-tuning.ipynb",
        "from tune_sklearn import TuneGridSearchCV\n\ndef get_model():\n    scaler = MinMaxScaler()\n    pca = PCA()\n    rf = RandomForestClassifier(**{\n        'random_state': 37\n    })\n    pipeline = Pipeline(steps=[('scaler', scaler), ('pca', pca), ('rf', rf)])\n\n    cv = StratifiedKFold(**{\n        'n_splits': 5,\n        'shuffle': True,\n        'random_state': 37\n    })\n    \n    auc_scorer = make_scorer(\n        roc_auc_score, \n        greater_is_better=True, \n        needs_proba=True, \n        multi_class='ovo')\n    apr_scorer_macro = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        needs_proba=True, \n        average='macro')\n    apr_scorer_micro = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        needs_proba=True, \n        average='micro')\n    apr_scorer_weighted = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        needs_proba=True, \n        average='weighted')\n\n    model = TuneGridSearchCV(**{\n        'estimator': pipeline,\n        'cv': cv,\n        'param_grid': {\n            'scaler__feature_range': [(0, 1)],\n            'pca__n_components': [2, 3, 4, 5],\n            'rf__criterion': ['gini', 'entropy']\n        },\n        'scoring': {\n            'auc': auc_scorer,\n            'apr_scorer_macro': apr_scorer_macro,\n            'apr_scorer_micro': apr_scorer_micro,\n            'apr_scorer_weighted': apr_scorer_weighted\n        },\n        'verbose': 1,\n        'refit': 'apr_scorer_micro',\n        'error_score': np.nan,\n        'n_jobs': -1,\n        'early_stopping': 'MedianStoppingRule',\n        'max_iters': 10\n    })\n    return model\n",
        "try:\n    from tune_sklearn import TuneGridSearchCV\nexcept Exception:\n    TuneGridSearchCV = None\n\ndef get_model():\n    scaler = MinMaxScaler()\n    pca = PCA()\n    rf = RandomForestClassifier(**{\n        'random_state': 37\n    })\n    pipeline = Pipeline(steps=[('scaler', scaler), ('pca', pca), ('rf', rf)])\n\n    cv = StratifiedKFold(**{\n        'n_splits': 5,\n        'shuffle': True,\n        'random_state': 37\n    })\n    \n    auc_scorer = make_scorer(\n        roc_auc_score, \n        greater_is_better=True, \n        needs_proba=True, \n        multi_class='ovo')\n    apr_scorer_macro = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        needs_proba=True, \n        average='macro')\n    apr_scorer_micro = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        needs_proba=True, \n        average='micro')\n    apr_scorer_weighted = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        needs_proba=True, \n        average='weighted')\n\n    model_cls = TuneGridSearchCV or GridSearchCV\n    model_kwargs = {\n        'estimator': pipeline,\n        'cv': cv,\n        'param_grid': {\n            'scaler__feature_range': [(0, 1)],\n            'pca__n_components': [2, 3, 4, 5],\n            'rf__criterion': ['gini', 'entropy']\n        },\n        'scoring': {\n            'auc': auc_scorer,\n            'apr_scorer_macro': apr_scorer_macro,\n            'apr_scorer_micro': apr_scorer_micro,\n            'apr_scorer_weighted': apr_scorer_weighted\n        },\n        'verbose': 1,\n        'refit': 'apr_scorer_micro',\n        'error_score': np.nan,\n        'n_jobs': -1,\n    }\n    if TuneGridSearchCV is not None:\n        model_kwargs.update({\n            'early_stopping': 'MedianStoppingRule',\n            'max_iters': 10,\n        })\n    model = model_cls(**model_kwargs)\n    return model\n",
    )


if __name__ == "__main__":
    main()
