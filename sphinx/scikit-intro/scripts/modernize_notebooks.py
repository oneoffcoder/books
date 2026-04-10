from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"


def replace_all(text: str) -> str:
    replacements = {
        "loss='log'": "loss='log_loss'",
        "plt.style.use('seaborn')": "plt.style.use('seaborn-v0_8')",
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
        "from sklearn.neighbors import DistanceMetric": "from sklearn.metrics import DistanceMetric",
        "needs_proba=True": "response_method='predict_proba'",
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


def prepend_to_cells_containing(nb_name: str, needle: str, prefix: str) -> None:
    path = SOURCE / nb_name
    notebook = json.loads(path.read_text())
    changed = False
    for cell in notebook["cells"]:
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        if needle in source and prefix.strip() not in source:
            updated = prefix + source
            cell["source"] = [line for line in updated.splitlines(keepends=True)]
            changed = True
    if not changed:
        return
    path.write_text(json.dumps(notebook, indent=1, ensure_ascii=True) + "\n")


def replace_text_in_notebook(nb_name: str, old: str, new: str) -> None:
    path = SOURCE / nb_name
    notebook = json.loads(path.read_text())
    changed = False
    for cell in notebook["cells"]:
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        updated = source.replace(old, new)
        if updated != source:
            cell["source"] = [line for line in updated.splitlines(keepends=True)]
            changed = True
    if changed:
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
    replace_cell_containing(
        "customized-estimators.ipynb",
        "class SpecialEstimator(BaseEstimator):",
        "from sklearn.utils.estimator_checks import check_estimator\nfrom sklearn.base import BaseEstimator, RegressorMixin, ClassifierMixin, TransformerMixin\nfrom sklearn.utils.validation import check_is_fitted, validate_data\nfrom sklearn.utils.multiclass import unique_labels\nfrom sklearn.metrics import euclidean_distances\nimport numpy as np\n\nclass SpecialEstimator(BaseEstimator):\n    def __init__(self):\n        pass\n    \n    def fit(self, X, y, **kwargs):\n        if y is None:\n            raise ValueError('requires y to be passed, but the target y is None')\n            \n        X, y = validate_data(self, X, y)\n        self.is_fitted_ = True\n        \n        return self\n    \n    def predict(self, X):\n        check_is_fitted(self, 'is_fitted_')\n        X = validate_data(self, X, reset=False)\n        return np.ones(X.shape[0], dtype=np.int64)\n\ncheck_estimator(SpecialEstimator())\n",
    )
    replace_cell_containing(
        "customized-estimators.ipynb",
        "class SpecialRegressor(RegressorMixin, BaseEstimator):",
        "class SpecialRegressor(RegressorMixin, BaseEstimator):\n    def __init__(self):\n        pass\n    \n    def fit(self, X, y, **kwargs):\n        if y is None:\n            raise ValueError('requires y to be passed, but the target y is None')\n            \n        X, y = validate_data(self, X, y)\n        self.is_fitted_ = True\n        \n        return self\n    \n    def predict(self, X):\n        check_is_fitted(self, 'is_fitted_')\n        X = validate_data(self, X, reset=False)\n        return np.ones(X.shape[0], dtype=np.int64)\n\n    def _more_tags(self):\n        return {\n            'poor_score': True\n        }\n\n    def __sklearn_tags__(self):\n        tags = super().__sklearn_tags__()\n        tags.regressor_tags.poor_score = True\n        return tags\n    \ncheck_estimator(SpecialRegressor())\n",
    )
    replace_cell_containing(
        "customized-estimators.ipynb",
        "class SpecialClassifier(ClassifierMixin, BaseEstimator):",
        "from random import choice\n\nclass SpecialClassifier(ClassifierMixin, BaseEstimator):\n    def __init__(self):\n        pass\n    \n    def fit(self, X, y, **kwargs):\n        if y is None:\n            raise ValueError('requires y to be passed, but the target y is None')\n        \n        X, y = validate_data(self, X, y)\n        sample_weight = kwargs.get('sample_weight')\n        if sample_weight is not None:\n            sample_weight = np.asarray(sample_weight)\n            mask = sample_weight > 0\n            if np.any(mask):\n                y = y[mask]\n        self.classes_ = unique_labels(y)\n        self.is_fitted_ = True\n        self.constant_ = self.classes_[0]\n        \n        return self\n    \n    def predict(self, X):\n        check_is_fitted(self, ['is_fitted_', 'constant_'])\n        X = validate_data(self, X, reset=False)\n        return np.full(X.shape[0], self.constant_, dtype=self.classes_.dtype)\n\n    def __sklearn_tags__(self):\n        tags = super().__sklearn_tags__()\n        tags.classifier_tags.poor_score = True\n        return tags\n    \ncheck_estimator(SpecialClassifier())\n",
    )
    replace_cell_containing(
        "customized-estimators.ipynb",
        "class SpecialTransformer(TransformerMixin, BaseEstimator):",
        "class SpecialTransformer(TransformerMixin, BaseEstimator):\n    def __init__(self):\n        pass\n    \n    def fit(self, X, y=None):\n        X = validate_data(self, X, y=None)\n        self.n_features_ = X.shape[1]\n        self.is_fitted_ = True\n                \n        return self\n    \n    def transform(self, X):\n        check_is_fitted(self, ['is_fitted_'])\n        X = validate_data(self, X, reset=False)\n        return np.sqrt(X)\n    \ncheck_estimator(SpecialTransformer())\n",
    )
    replace_cell_containing(
        "customized-estimators.ipynb",
        "class AwesomeEstimator(RegressorMixin, BaseEstimator):",
        "from sklearn.pipeline import Pipeline\nfrom sklearn.decomposition import PCA\nfrom sklearn.preprocessing import MinMaxScaler\nfrom sklearn.ensemble import RandomForestRegressor\nfrom sklearn.model_selection import GridSearchCV, StratifiedKFold\n\nclass AwesomeEstimator(RegressorMixin, BaseEstimator):\n    def __init__(self):\n        pass\n    \n    def __get_pipeline(self):\n        scaler = MinMaxScaler()\n        regressor = RandomForestRegressor(**{\n            'random_state': 37\n        })\n        \n        steps=[\n            ('scaler', scaler), \n            ('regressor', regressor)]\n        \n        pipeline = Pipeline(steps=steps)\n        return pipeline\n    \n    def __get_model(self, feature_range, n_estimators):\n        model = GridSearchCV(**{\n            'estimator': self.__get_pipeline(),\n            'cv': 5,\n            'param_grid': {\n                'scaler__feature_range': feature_range,\n                'regressor__n_estimators': n_estimators\n            },\n            'scoring': 'neg_mean_absolute_error',\n            'verbose': 5,\n            'refit': 'neg_mean_absolute_error',\n            'error_score': np.nan,\n            'n_jobs': -1\n        })\n        return model\n\n    \n    def fit(self, X, y, feature_range=[(0, 1)], n_estimators=[100]):\n        if y is None:\n            raise ValueError('requires y to be passed, but the target y is None')\n            \n        X, y = validate_data(self, X, y)\n        self.is_fitted_ = True\n        \n        self.model_ = self.__get_model(feature_range, n_estimators)\n        self.model_.fit(X, y)\n        \n        return self\n    \n    def predict(self, X):\n        check_is_fitted(self, ['is_fitted_', 'model_'])\n        X = validate_data(self, X, reset=False)\n        return self.model_.predict(X)\n\ncheck_estimator(AwesomeEstimator())\n",
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
        "dask.ipynb",
        "from dask_ml.linear_model import LogisticRegression",
        "%%time\n\ntry:\n    from dask_ml.linear_model import LogisticRegression\n    fit_X, fit_y = X, y\n    solver = 'admm'\nexcept Exception:\n    from sklearn.linear_model import LogisticRegression\n    fit_X, fit_y = X.compute(), y.compute()\n    solver = 'liblinear'\n\nif not getattr(LogisticRegression, '__module__', '').startswith('dask_ml'):\n    fit_X, fit_y = X.compute(), y.compute()\n    solver = 'liblinear'\n\nmodel = LogisticRegression(penalty='l2', C=0.01, random_state=37, solver=solver, max_iter=1000)\nmodel.fit(fit_X, fit_y)\n[('intercept', model.intercept_)] + [(f, c) for f, c in zip(range(len(model.coef_.ravel())), model.coef_.ravel())]\n",
    )
    replace_cell_containing(
        "dask.ipynb",
        "model = LogisticRegression(penalty='l1', C=0.5, random_state=37, solver='admm')",
        "%%time\n\nfit_X, fit_y = X, y\nsolver = 'admm'\nif not getattr(LogisticRegression, '__module__', '').startswith('dask_ml'):\n    fit_X, fit_y = X.compute(), y.compute()\n    solver = 'liblinear'\n\nmodel = LogisticRegression(penalty='l1', C=0.5, random_state=37, solver=solver, max_iter=1000)\nmodel.fit(fit_X, fit_y)\n[('intercept', model.intercept_)] + [(f, c) for f, c in zip(range(len(model.coef_.ravel())), model.coef_.ravel())]\n",
    )
    replace_cell_containing(
        "nltk.ipynb",
        "from nltk.corpus import stopwords",
        "from nltk.corpus import stopwords\nfrom sklearn.feature_extraction.text import CountVectorizer\nimport pandas as pd\nfrom _runtime import ensure_nltk_data\n\nensure_nltk_data()\nstop_words = set(stopwords.words('english'))\n\nvectorizer = CountVectorizer(binary=True, stop_words=sorted(stop_words))\nX = vectorizer.fit_transform(text).todense()\n\nbool_df = pd.DataFrame(X, columns=vectorizer.get_feature_names_out())\n\nprint(bool_df.shape)\nbool_df.columns\n",
    )
    replace_cell_containing(
        "nltk.ipynb",
        "from nltk.stem import WordNetLemmatizer",
        "from nltk.stem import WordNetLemmatizer\n"
        "from _runtime import ensure_nltk_data\n"
        "  \n"
        "ensure_nltk_data()\n"
        "lemmatizer = WordNetLemmatizer()\n\n"
        "def safe_lemmatize(token):\n"
        "    try:\n"
        "        return lemmatizer.lemmatize(token)\n"
        "    except KeyError:\n"
        "        return token\n\n"
        "for title in text:\n"
        "    print([safe_lemmatize(token) for token in nltk.word_tokenize(title)])\n",
    )
    replace_text_in_notebook(
        "nltk.ipynb",
        "lemmatize = lambda t: lemmatizer.lemmatize(t)",
        "lemmatize = safe_lemmatize",
    )
    replace_cell_containing(
        "mlflow.ipynb",
        "tracking_uri = 'http://localhost:5001'",
        "import mlflow\nfrom mlflow.exceptions import MlflowException\nfrom mlflow.models.signature import infer_signature\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom _runtime import get_mlflow_tracking_uri\n\nplt.style.use('ggplot')\n\nexperiment_name = 'test1'\ntracking_uri = get_mlflow_tracking_uri()\nmlflow.set_tracking_uri(tracking_uri)\n\nif not mlflow.get_experiment_by_name(experiment_name):\n    try:\n        mlflow.create_experiment(experiment_name)\n    except MlflowException as ex:\n        print(f'{ex}')\n\nmlflow.set_experiment(experiment_name)\n\nwith mlflow.start_run() as run:\n    model = get_model()\n    model.fit(X_tr, y_tr)\n    \n    signature = infer_signature(X_tr, model.predict_proba(X_tr))\n    mlflow.sklearn.log_model(model, 'model', signature=signature)\n    mlflow.log_params(model.best_params_)\n    \n    perf_metrics = get_performances(X_tr, y_tr, X_te, y_te, model)\n    mlflow.log_metrics(perf_metrics)\n    \n    pd.DataFrame({k: model.cv_results_[k] for k in model.cv_results_ if k not in {'params'}}) \\\n        .to_csv('./_temp/cv-results.csv', index=False)\n    mlflow.log_artifact('./_temp/cv-results.csv', 'artifact')\n    \n    temp = pd.concat([\n        pd.DataFrame({'y': y_tr}).assign(fold='tr'),\n        pd.DataFrame({'y': y_te}).assign(fold='te')\n    ]).assign(n=1).groupby(['fold', 'y'])['n'].sum().to_frame().reset_index()\n    fig, ax = plt.subplots()\n    sns.barplot(x='fold', hue='y', y='n', data=temp, ax=ax)\n    ax.set_title('Class Distributions')\n    mlflow.log_figure(fig, 'fig/00-class-distributions.png')\n    \n    fig, ax = plt.subplots(1, 2, figsize=(10, 3.5))\n    X_tr.plot(kind='kde', ax=ax[0], title='Feature Distributions, TR')\n    X_te.plot(kind='kde', ax=ax[1], title='Feature Distributions, TE')\n    plt.tight_layout()\n    mlflow.log_figure(fig, 'fig/01-feature-distributions.png')\n    \n    fig, ax = plt.subplots(1, 2, figsize=(10, 3.5))\n    sns.heatmap(X_tr.corr(), ax=ax[0])\n    sns.heatmap(X_te.corr(), ax=ax[1])\n    ax[0].set_title('Correlogram, TR')\n    ax[1].set_title('Correlogram, TE')\n    plt.tight_layout()\n    mlflow.log_figure(fig, 'fig/02-correlograms.png')\n    \n    fig = sns.pairplot(X_tr.assign(y=y_tr), hue='y').fig\n    mlflow.log_figure(fig, 'fig/03-00-tr-pairplot.png')\n    \n    fig = sns.pairplot(X_te.assign(y=y_te), hue='y').fig\n    mlflow.log_figure(fig, 'fig/03-01-te-pairplot.png')\n    \n    fig, ax = plt.subplots(2, 1, figsize=(15, 5.5))\n    pd.plotting.parallel_coordinates(X_tr.assign(y=y_tr), 'y', X_tr.columns, color=['#2e8ad8', '#cd3785'], sort_labels=True, ax=ax[0])\n    pd.plotting.parallel_coordinates(X_te.assign(y=y_te), 'y', X_te.columns, color=['#2e8ad8', '#cd3785'], sort_labels=True, ax=ax[1])\n    ax[0].set_title('Parallel Coordinates, TR')\n    ax[1].set_title('Parallel Coordinates, TE')\n    plt.tight_layout()\n    mlflow.log_figure(fig, 'fig/04-parallel-coordinate.png')\n    \n    run_id = mlflow.active_run().info.run_id\n",
    )
    replace_cell_containing(
        "mlflow.ipynb",
        "from joblib import Parallel, delayed",
        "from joblib import Parallel, delayed\nfrom _runtime import SCIKIT_INTRO_CHECK_MODE, get_mlflow_tracking_uri\n\ndef do_learn(penalty, C, path_tr, path_te, tracking_uri=None, experiment_name='test2'):\n    def get_Xy(path):\n        df = pd.read_csv(path)\n        y_col = 'y'\n        X_cols = [c for c in df.columns if c != y_col]\n        \n        X, y = df[X_cols], df[y_col]\n        return X, y\n    \n    X_tr, y_tr = get_Xy(path_tr)\n    X_te, y_te = get_Xy(path_te)\n    tracking_uri = tracking_uri or get_mlflow_tracking_uri()\n    \n    model_params = {\n        'solver': 'saga',\n        'penalty': penalty,\n        'C': C,\n        'random_state': 37,\n        'max_iter': 1_000\n    }\n    model = LogisticRegression(**model_params)\n\n    mlflow.set_tracking_uri(tracking_uri)\n\n    if not mlflow.get_experiment_by_name(experiment_name):\n        try:\n            mlflow.create_experiment(experiment_name)\n        except MlflowException as ex:\n            print(f'{ex}')\n\n    mlflow.set_experiment(experiment_name)\n\n    with mlflow.start_run() as run:\n        model.fit(X_tr, y_tr)\n\n        signature = infer_signature(X_tr, model.predict_proba(X_tr))\n        mlflow.sklearn.log_model(model, 'model', signature=signature)\n        mlflow.log_params(model_params)\n\n        perf_metrics = get_performances(X_tr, y_tr, X_te, y_te, model)\n        mlflow.log_metrics(perf_metrics)\n    \n        run_id = mlflow.active_run().info.run_id\n        \n    return run_id\n\n\nsize = 4 if SCIKIT_INTRO_CHECK_MODE else 100\nC = np.random.uniform(size=size)\nP = np.random.uniform(size=size)\nP = np.where(P < 0.5, 'l1', 'l2')\n\nparallel_jobs = 1 if SCIKIT_INTRO_CHECK_MODE else -1\nrun_ids = Parallel(n_jobs=parallel_jobs)(delayed(do_learn)(p, c, path_tr, path_te) for p, c in zip(P, C))\nprint(run_ids)\n",
    )
    replace_cell_containing(
        "hyperparam-tuning.ipynb",
        "try:\n    from tune_sklearn import TuneGridSearchCV",
        "try:\n    from tune_sklearn import TuneGridSearchCV\nexcept Exception:\n    TuneGridSearchCV = None\n\nfrom _runtime import SCIKIT_INTRO_CHECK_MODE\n\ndef get_model():\n    scaler = MinMaxScaler()\n    pca = PCA()\n    rf = RandomForestClassifier(**{\n        'random_state': 37\n    })\n    pipeline = Pipeline(steps=[('scaler', scaler), ('pca', pca), ('rf', rf)])\n\n    cv = StratifiedKFold(**{\n        'n_splits': 2 if SCIKIT_INTRO_CHECK_MODE else 5,\n        'shuffle': True,\n        'random_state': 37\n    })\n    \n    auc_scorer = make_scorer(\n        roc_auc_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        multi_class='ovo')\n    apr_scorer_macro = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        average='macro')\n    apr_scorer_micro = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        average='micro')\n    apr_scorer_weighted = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        average='weighted')\n\n    model_cls = TuneGridSearchCV or GridSearchCV\n    model_kwargs = {\n        'estimator': pipeline,\n        'cv': cv,\n        'param_grid': {\n            'scaler__feature_range': [(0, 1)],\n            'pca__n_components': [2, 3] if SCIKIT_INTRO_CHECK_MODE else [2, 3, 4, 5],\n            'rf__criterion': ['gini'] if SCIKIT_INTRO_CHECK_MODE else ['gini', 'entropy']\n        },\n        'scoring': {\n            'auc': auc_scorer,\n            'apr_scorer_macro': apr_scorer_macro,\n            'apr_scorer_micro': apr_scorer_micro,\n            'apr_scorer_weighted': apr_scorer_weighted\n        },\n        'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 1,\n        'refit': 'apr_scorer_micro',\n        'error_score': np.nan,\n        'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1,\n    }\n    if TuneGridSearchCV is not None:\n        model_kwargs.update({\n            'early_stopping': 'MedianStoppingRule',\n            'max_iters': 3 if SCIKIT_INTRO_CHECK_MODE else 10,\n        })\n    model = model_cls(**model_kwargs)\n    return model\n",
    )
    replace_cell_containing(
        "hyperparam-tuning.ipynb",
        "fields = t_fields + h_fields + g_fields + o_fields",
        "preprocess = m.named_steps['preprocess'] if hasattr(m, 'named_steps') else m.best_estimator_.named_steps['preprocess']\n\n"
        "t_fields = list(preprocess.named_transformers_['text'].named_steps['vectorize'].get_feature_names_out())\n"
        "h_fields = list(preprocess.named_transformers_['hand'].named_steps['ohe'].get_feature_names_out())\n"
        "g_fields = list(preprocess.named_transformers_['gender'].named_steps['ohe'].get_feature_names_out())\n"
        "o_fields = ['age']\n\n"
        "fields = t_fields + h_fields + g_fields + o_fields\n"
        "fields",
    )
    replace_cell_containing(
        "hyperparam-tuning.ipynb",
        "regressor__l1_ratio': regressor__l1_ratio_dist",
        "from sklearn.model_selection import RandomizedSearchCV\n"
        "from scipy.stats import uniform, randint\n\n"
        "p0 = Pipeline(steps=[\n"
        "    ('impute', SimpleImputer(strategy='constant', fill_value='')), \n"
        "    ('reshape', FunctionTransformer(np.reshape, kw_args={'shape': (-1,)})),\n"
        "    ('vectorize', CountVectorizer())\n"
        "])\n"
        "p1 = Pipeline(steps=[\n"
        "    ('impute', SimpleImputer(strategy='most_frequent')), \n"
        "    ('ohe', OneHotEncoder(drop=['left']))\n"
        "])\n"
        "p2 = Pipeline(steps=[('ohe', OneHotEncoder(drop=['f']))])\n"
        "p4 = Pipeline(steps=[\n"
        "    ('impute', SimpleImputer()),\n"
        "    ('scale', StandardScaler())\n"
        "])\n\n"
        "t = ColumnTransformer([\n"
        "    ('text', p0, [0]),\n"
        "    ('hand', p1, [1]), \n"
        "    ('gender', p2, [2]),\n"
        "    ('age', p4, [3])\n"
        "], remainder='drop')\n\n"
        "e = Pipeline(steps=[\n"
        "    ('preprocess', t),\n"
        "    ('regressor', LogisticRegression(penalty='elasticnet', solver='saga', max_iter=1000))\n"
        "])\n\n"
        "cv = StratifiedKFold(**{\n"
        "    'n_splits': 5,\n"
        "    'shuffle': True,\n"
        "    'random_state': 37\n"
        "})\n\n"
        "uniform.random_state = 37\n"
        "randint.random_state = 37\n\n"
        "regressor__C_dist = uniform()\n"
        "regressor__l1_ratio_dist = uniform() \n"
        "regressor__random_state_dist = randint(5, 40)\n\n"
        "regressor__C_dist.random_state = 37\n"
        "regressor__l1_ratio_dist.random_state = 37\n"
        "regressor__random_state_dist.random_state = 37\n\n"
        "m = RandomizedSearchCV(**{\n"
        "    'estimator': e,\n"
        "    'cv': cv,\n"
        "    'param_distributions': {\n"
        "        'regressor__random_state': regressor__random_state_dist,\n"
        "        'regressor__C': regressor__C_dist,\n"
        "        'regressor__l1_ratio': regressor__l1_ratio_dist\n"
        "    },\n"
        "    'scoring': {\n"
        "        'auc': 'roc_auc',\n"
        "        'apr': 'average_precision'\n"
        "    },\n"
        "    'verbose': 5,\n"
        "    'refit': 'auc',\n"
        "    'error_score': np.nan,\n"
        "    'n_jobs': -1\n"
        "})\n\n"
        "m.fit(X, y)\n"
        "m.best_params_",
    )
    replace_cell_containing(
        "combo.ipynb",
        "def get_logistic_regression_model():",
        "from sklearn.linear_model import LogisticRegression\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import MinMaxScaler\nfrom sklearn.model_selection import GridSearchCV, StratifiedKFold\nfrom combo.models.classifier_stacking import Stacking\nfrom _runtime import SCIKIT_INTRO_CHECK_MODE\n\nStacking.__sklearn_tags__ = lambda self: LogisticRegression().__sklearn_tags__()\nStacking.__sklearn_is_fitted__ = lambda self: hasattr(self, 'fitted_')\n\ndef get_logistic_regression_model():\n    pipeline = Pipeline(steps=[('classifier', LogisticRegression(random_state=37, solver='liblinear', max_iter=1000))])\n    \n    cv = StratifiedKFold(**{\n        'n_splits': 2 if SCIKIT_INTRO_CHECK_MODE else 3,\n        'shuffle': True,\n        'random_state': 37\n    })\n    \n    param_grid = {\n        'classifier__penalty': ['l2'] if SCIKIT_INTRO_CHECK_MODE else ['l1', 'l2']\n    }\n    \n    model = GridSearchCV(**{\n        'estimator': pipeline,\n        'cv': cv,\n        'param_grid': param_grid,\n        'scoring': {\n            'accuracy': 'accuracy',\n            'f1': 'f1'\n        },\n        'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 5,\n        'refit': 'f1',\n        'error_score': 0.0,\n        'n_jobs': 1\n    })\n    \n    return model\n    \ndef get_stacking_model():\n    scaler = MinMaxScaler()\n    classifier = Stacking(\n        base_estimators=[DecisionTreeClassifier(), LogisticRegression()], \n        random_state=37\n    )\n    pipeline = Pipeline(steps=[\n        ('scaler', scaler), \n        ('classifier', classifier)\n    ])\n\n    cv = StratifiedKFold(**{\n        'n_splits': 2 if SCIKIT_INTRO_CHECK_MODE else 5,\n        'shuffle': True,\n        'random_state': 37\n    })\n\n    # combo's stacking implementation currently assumes a fixed number of\n    # stacked features, so keep the search space to two base estimators.\n    param_grid = {\n        'scaler__feature_range': [(0, 1)] if SCIKIT_INTRO_CHECK_MODE else [(0, 1), (0, 2)],\n        'classifier__base_estimators': [\n            [\n                DecisionTreeClassifier(), \n                get_logistic_regression_model(),\n            ],\n        ] if SCIKIT_INTRO_CHECK_MODE else [\n            [\n                DecisionTreeClassifier(), \n                get_logistic_regression_model(),\n            ],\n            [\n                RandomForestClassifier(), \n                GradientBoostingClassifier(),\n            ],\n            [\n                KNeighborsClassifier(),\n                get_logistic_regression_model(),\n            ]\n        ],\n        'classifier__n_folds': [2] if SCIKIT_INTRO_CHECK_MODE else [2, 5],\n        'classifier__use_proba': [False] if SCIKIT_INTRO_CHECK_MODE else [False, True]\n    }\n\n    model = GridSearchCV(**{\n        'estimator': pipeline,\n        'cv': cv,\n        'param_grid': param_grid,\n        'scoring': {\n            'accuracy': 'accuracy',\n            'f1': 'f1'\n        },\n        'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 5,\n        'refit': 'f1',\n        'error_score': 0.0,\n        'n_jobs': 1\n    })\n    \n    return model\n",
    )
    replace_cell_containing(
        "combo.ipynb",
        "for tr_index, te_index in StratifiedKFold(n_splits=5, shuffle=True, random_state=37).split(X, y):",
        "import pandas as pd\n\nr_df = []\n\nfor tr_index, te_index in StratifiedKFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 5, shuffle=True, random_state=37).split(X, y):\n    X_tr, y_tr = X[tr_index,:], y[tr_index]\n    X_te, y_te = X[te_index,:], y[te_index]\n    \n    print(X_tr.shape, y_tr.shape, X_te.shape, y_te.shape)\n    \n    model = get_stacking_model()\n    model.fit(X_tr, y_tr)\n    \n    y_pred = combo_predict(model.best_estimator_, X_te)\n    \n    accuracy = accuracy_score(y_te, y_pred)\n    f1 = f1_score(y_te, y_pred)\n    \n    r_df.append({'accuracy': accuracy, 'f1': f1})\n    \nr_df = pd.DataFrame(r_df)\nr_df\n",
    )
    replace_cell_containing(
        "hyperparam-tuning.ipynb",
        "from sklearn.linear_model import LogisticRegression",
        "from sklearn.linear_model import LogisticRegression\nfrom sklearn.model_selection import GridSearchCV, StratifiedKFold\nfrom _runtime import SCIKIT_INTRO_CHECK_MODE\n\np = {\n    'solver': 'sag',\n    'penalty': 'l2',\n    'random_state': 37,\n    'max_iter': 100\n}\nestimator = LogisticRegression(**p)\n\np = {\n    'n_splits': 2 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'shuffle': True,\n    'random_state': 37\n}\ncv = StratifiedKFold(**p)\n\np = {\n    'estimator': estimator,\n    'cv': cv,\n    'param_grid': {\n        'C': [0.1, 1.0] if SCIKIT_INTRO_CHECK_MODE else [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]\n    },\n    'scoring': {\n        'auc': 'roc_auc',\n        'apr': 'average_precision'\n    },\n    'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'refit': 'auc',\n    'error_score': np.nan,\n    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1\n}\nmodel = GridSearchCV(**p)\n\nmodel.fit(X, y)\n",
    )
    replace_cell_containing(
        "hyperparam-tuning.ipynb",
        "from sklearn.ensemble import RandomForestClassifier",
        "from sklearn.ensemble import RandomForestClassifier\nfrom _runtime import SCIKIT_INTRO_CHECK_MODE\n\np = {\n    'random_state': 37\n}\nestimator = RandomForestClassifier(**p)\n\np = {\n    'n_splits': 2 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'shuffle': True,\n    'random_state': 37\n}\ncv = StratifiedKFold(**p)\n\np = {\n    'estimator': estimator,\n    'cv': cv,\n    'param_grid': {\n        'n_estimators': [10, 20] if SCIKIT_INTRO_CHECK_MODE else [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],\n        'criterion': ['gini'] if SCIKIT_INTRO_CHECK_MODE else ['gini', 'entropy']\n    },\n    'scoring': {\n        'auc': 'roc_auc',\n        'apr': 'average_precision'\n    },\n    'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'refit': 'auc',\n    'error_score': np.nan,\n    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1\n}\nmodel = GridSearchCV(**p)\n\nmodel.fit(X, y)\n",
    )
    replace_cell_containing(
        "hyperparam-tuning.ipynb",
        "from sklearn.pipeline import Pipeline",
        "from sklearn.pipeline import Pipeline\nfrom sklearn.decomposition import PCA\nfrom sklearn.preprocessing import MinMaxScaler\nfrom _runtime import SCIKIT_INTRO_CHECK_MODE\n\nscaler = MinMaxScaler()\npca = PCA()\nrf = RandomForestClassifier(**{\n    'random_state': 37\n})\npipeline = Pipeline(steps=[('scaler', scaler), ('pca', pca), ('rf', rf)])\n\ncv = StratifiedKFold(**{\n    'n_splits': 2 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'shuffle': True,\n    'random_state': 37\n})\n\nmodel = GridSearchCV(**{\n    'estimator': pipeline,\n    'cv': cv,\n    'param_grid': {\n        'scaler__feature_range': [(0, 1)] if SCIKIT_INTRO_CHECK_MODE else [(0, 1), (0, 2)],\n        'pca__n_components': [2, 3] if SCIKIT_INTRO_CHECK_MODE else [2, 3, 4, 5, 10, 11, 12, 15],\n        'rf__n_estimators': [10, 20] if SCIKIT_INTRO_CHECK_MODE else [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],\n        'rf__criterion': ['gini'] if SCIKIT_INTRO_CHECK_MODE else ['gini', 'entropy']\n    },\n    'scoring': {\n        'auc': 'roc_auc',\n        'apr': 'average_precision'\n    },\n    'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'refit': 'auc',\n    'error_score': np.nan,\n    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1\n})\n\nmodel.fit(X, y)\n",
    )
    replace_cell_containing(
        "hyperparam-tuning.ipynb",
        "def apr_score(y_true, y_pred, average='micro'):",
        "from sklearn.metrics import roc_auc_score, average_precision_score, make_scorer\nfrom sklearn.preprocessing import OneHotEncoder\nfrom _runtime import SCIKIT_INTRO_CHECK_MODE\n\ndef apr_score(y_true, y_pred, average='micro'):\n    encoder = OneHotEncoder()\n    Y = encoder.fit_transform(y_true.reshape(-1, 1)).toarray()\n    \n    return average_precision_score(Y, y_pred, average=average)\n\ndef get_model():\n    scaler = MinMaxScaler()\n    pca = PCA()\n    rf = RandomForestClassifier(**{\n        'random_state': 37\n    })\n    pipeline = Pipeline(steps=[('scaler', scaler), ('pca', pca), ('rf', rf)])\n\n    cv = StratifiedKFold(**{\n        'n_splits': 2 if SCIKIT_INTRO_CHECK_MODE else 5,\n        'shuffle': True,\n        'random_state': 37\n    })\n    \n    auc_scorer = make_scorer(\n        roc_auc_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        multi_class='ovo')\n    apr_scorer_macro = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        average='macro')\n    apr_scorer_micro = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        average='micro')\n    apr_scorer_weighted = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        average='weighted')\n\n    model = GridSearchCV(**{\n        'estimator': pipeline,\n        'cv': cv,\n        'param_grid': {\n            'scaler__feature_range': [(0, 1)] if SCIKIT_INTRO_CHECK_MODE else [(0, 1), (0, 2)],\n            'pca__n_components': [2, 3] if SCIKIT_INTRO_CHECK_MODE else [2, 3, 4, 5, 10, 11, 12, 15],\n            'rf__n_estimators': [2, 3, 4] if SCIKIT_INTRO_CHECK_MODE else [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],\n            'rf__criterion': ['gini'] if SCIKIT_INTRO_CHECK_MODE else ['gini', 'entropy']\n        },\n        'scoring': {\n            'auc': auc_scorer,\n            'apr_scorer_macro': apr_scorer_macro,\n            'apr_scorer_micro': apr_scorer_micro,\n            'apr_scorer_weighted': apr_scorer_weighted\n        },\n        'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 5,\n        'refit': 'apr_scorer_micro',\n        'error_score': np.nan,\n        'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1\n    })\n    return model\n",
    )
    replace_cell_containing(
        "hyperparam-tuning.ipynb",
        "try:\n    from tune_sklearn import TuneGridSearchCV",
        "try:\n    from tune_sklearn import TuneGridSearchCV\nexcept Exception:\n    TuneGridSearchCV = None\n\nfrom _runtime import SCIKIT_INTRO_CHECK_MODE\n\ndef get_model():\n    scaler = MinMaxScaler()\n    pca = PCA()\n    rf = RandomForestClassifier(**{\n        'random_state': 37\n    })\n    pipeline = Pipeline(steps=[('scaler', scaler), ('pca', pca), ('rf', rf)])\n\n    cv = StratifiedKFold(**{\n        'n_splits': 2 if SCIKIT_INTRO_CHECK_MODE else 5,\n        'shuffle': True,\n        'random_state': 37\n    })\n    \n    auc_scorer = make_scorer(\n        roc_auc_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        multi_class='ovo')\n    apr_scorer_macro = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        average='macro')\n    apr_scorer_micro = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        average='micro')\n    apr_scorer_weighted = make_scorer(\n        apr_score, \n        greater_is_better=True, \n        response_method='predict_proba', \n        average='weighted')\n\n    model_cls = TuneGridSearchCV or GridSearchCV\n    model_kwargs = {\n        'estimator': pipeline,\n        'cv': cv,\n        'param_grid': {\n            'scaler__feature_range': [(0, 1)],\n            'pca__n_components': [2, 3] if SCIKIT_INTRO_CHECK_MODE else [2, 3, 4, 5],\n            'rf__criterion': ['gini'] if SCIKIT_INTRO_CHECK_MODE else ['gini', 'entropy']\n        },\n        'scoring': {\n            'auc': auc_scorer,\n            'apr_scorer_macro': apr_scorer_macro,\n            'apr_scorer_micro': apr_scorer_micro,\n            'apr_scorer_weighted': apr_scorer_weighted\n        },\n        'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 1,\n        'refit': 'apr_scorer_micro',\n        'error_score': np.nan,\n        'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1,\n    }\n    if TuneGridSearchCV is not None:\n        model_kwargs.update({\n            'early_stopping': 'MedianStoppingRule',\n            'max_iters': 3 if SCIKIT_INTRO_CHECK_MODE else 10,\n        })\n    model = model_cls(**model_kwargs)\n    return model\n",
    )
    replace_cell_containing(
        "hyperparam-tuning.ipynb",
        "p0 = Pipeline(steps=[",
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\np0 = Pipeline(steps=[\n    ('impute', SimpleImputer(strategy='constant', fill_value='')), \n    ('reshape', FunctionTransformer(np.reshape, kw_args={'shape': (-1,)})),\n    ('vectorize', CountVectorizer())\n])\np1 = Pipeline(steps=[\n    ('impute', SimpleImputer(strategy='most_frequent')), \n    ('ohe', OneHotEncoder(drop=['left']))\n])\np2 = Pipeline(steps=[('ohe', OneHotEncoder(drop=['f']))])\np4 = Pipeline(steps=[\n    ('impute', SimpleImputer()),\n    ('scale', StandardScaler())\n])\n\nt = ColumnTransformer([\n    ('text', p0, [0]),\n    ('hand', p1, [1]), \n    ('gender', p2, [2]),\n    ('age', p4, [3])\n], remainder='drop')\n\ne = Pipeline(steps=[\n    ('preprocess', t),\n    ('regressor', LogisticRegression(penalty='elasticnet', solver='saga', max_iter=1000))\n])\n\ncv = StratifiedKFold(**{\n    'n_splits': 2 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'shuffle': True,\n    'random_state': 37\n})\n\nm = GridSearchCV(**{\n    'estimator': e,\n    'cv': cv,\n    'param_grid': {\n        'regressor__random_state': [29] if SCIKIT_INTRO_CHECK_MODE else [29, 37]\n    },\n    'scoring': {\n        'auc': 'roc_auc',\n        'apr': 'average_precision'\n    },\n    'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'refit': 'auc',\n    'error_score': np.nan,\n    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1\n})\n\nm.fit(X, y)\nm.best_params_\n",
    )
    replace_cell_containing(
        "hyperparam-tuning.ipynb",
        "from sklearn.model_selection import RandomizedSearchCV",
        "from sklearn.model_selection import RandomizedSearchCV\nfrom scipy.stats import uniform, randint\nfrom _runtime import SCIKIT_INTRO_CHECK_MODE\n\np0 = Pipeline(steps=[\n    ('impute', SimpleImputer(strategy='constant', fill_value='')), \n    ('reshape', FunctionTransformer(np.reshape, kw_args={'shape': (-1,)})),\n    ('vectorize', CountVectorizer())\n])\np1 = Pipeline(steps=[\n    ('impute', SimpleImputer(strategy='most_frequent')), \n    ('ohe', OneHotEncoder(drop=['left']))\n])\np2 = Pipeline(steps=[('ohe', OneHotEncoder(drop=['f']))])\np4 = Pipeline(steps=[\n    ('impute', SimpleImputer()),\n    ('scale', StandardScaler())\n])\n\nt = ColumnTransformer([\n    ('text', p0, [0]),\n    ('hand', p1, [1]), \n    ('gender', p2, [2]),\n    ('age', p4, [3])\n], remainder='drop')\n\ne = Pipeline(steps=[\n    ('preprocess', t),\n    ('regressor', LogisticRegression(penalty='elasticnet', solver='saga', max_iter=1000))\n])\n\ncv = StratifiedKFold(**{\n    'n_splits': 2 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'shuffle': True,\n    'random_state': 37\n})\n\nuniform.random_state = 37\nrandint.random_state = 37\n\nregressor__C_dist = uniform()\nregressor__l1_ratio_dist = uniform() \nregressor__random_state_dist = randint(5, 40)\n\nregressor__C_dist.random_state = 37\nregressor__l1_ratio_dist.random_state = 37\nregressor__random_state_dist.random_state = 37\n\nm = RandomizedSearchCV(**{\n    'estimator': e,\n    'cv': cv,\n    'param_distributions': {\n        'regressor__random_state': regressor__random_state_dist,\n        'regressor__C': regressor__C_dist,\n        'regressor__l1_ratio': regressor__l1_ratio_dist\n    },\n    'scoring': {\n        'auc': 'roc_auc',\n        'apr': 'average_precision'\n    },\n    'n_iter': 5 if SCIKIT_INTRO_CHECK_MODE else 10,\n    'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'refit': 'auc',\n    'error_score': np.nan,\n    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1\n})\n\nm.fit(X, y)\nm.best_params_\n",
    )
    replace_cell_containing(
        "hyperparam-tuning.ipynb",
        "'regressor__random_state': [29, 37]",
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\np0 = Pipeline(steps=[\n    ('impute', SimpleImputer(strategy='constant', fill_value='')), \n    ('reshape', FunctionTransformer(np.reshape, kw_args={'shape': (-1,)})),\n    ('vectorize', CountVectorizer())\n])\np1 = Pipeline(steps=[\n    ('impute', SimpleImputer(strategy='most_frequent')), \n    ('ohe', OneHotEncoder(drop=['left']))\n])\np2 = Pipeline(steps=[('ohe', OneHotEncoder(drop=['f']))])\np4 = Pipeline(steps=[\n    ('impute', SimpleImputer()),\n    ('scale', StandardScaler())\n])\n\nt = ColumnTransformer([\n    ('text', p0, [0]),\n    ('hand', p1, [1]), \n    ('gender', p2, [2]),\n    ('age', p4, [3])\n], remainder='drop')\n\ne = Pipeline(steps=[\n    ('preprocess', t),\n    ('regressor', LogisticRegression(penalty='elasticnet', solver='saga', max_iter=1000))\n])\n\ncv = StratifiedKFold(**{\n    'n_splits': 2 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'shuffle': True,\n    'random_state': 37\n})\n\nm = GridSearchCV(**{\n    'estimator': e,\n    'cv': cv,\n    'param_grid': {\n        'regressor__random_state': [29] if SCIKIT_INTRO_CHECK_MODE else [29, 37]\n    },\n    'scoring': {\n        'auc': 'roc_auc',\n        'apr': 'average_precision'\n    },\n    'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 5,\n    'refit': 'auc',\n    'error_score': np.nan,\n    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1\n})\n\nm.fit(X, y)\nm.best_params_\n",
    )
    prepend_to_cells_containing(
        "hyperparam-tuning.ipynb",
        "p0 = Pipeline(steps=[",
        "import numpy as np\n"
        "from sklearn.compose import ColumnTransformer\n"
        "from sklearn.feature_extraction.text import CountVectorizer\n"
        "from sklearn.impute import SimpleImputer\n"
        "from sklearn.linear_model import LogisticRegression\n"
        "from sklearn.model_selection import GridSearchCV, StratifiedKFold\n"
        "from sklearn.pipeline import Pipeline\n"
        "from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler\n\n",
    )
    replace_text_in_notebook(
        "hyperparam-tuning.ipynb",
        "p0 = Pipeline(steps=[\n    ('impute', SimpleImputer(strategy='constant', fill_value='')), \n    ('reshape', FunctionTransformer(np.reshape, kw_args={'shape': (-1,)})),\n    ('vectorize', CountVectorizer())\n])",
        "p0 = Pipeline(steps=[\n    ('reshape', FunctionTransformer(lambda x: np.asarray(x).reshape(-1).astype(str), validate=False)),\n    ('vectorize', CountVectorizer())\n])",
    )
    replace_text_in_notebook(
        "hyperparam-tuning.ipynb",
        "('ohe', OneHotEncoder(drop=['left']))",
        "('ohe', OneHotEncoder(drop='if_binary'))",
    )
    replace_text_in_notebook(
        "hyperparam-tuning.ipynb",
        "('ohe', OneHotEncoder(drop=['f']))",
        "('ohe', OneHotEncoder(drop='if_binary'))",
    )
    replace_cell_containing(
        "combo.ipynb",
        "best_model = model.best_estimator_",
        "from sklearn.metrics import accuracy_score, f1_score\n\ndef combo_predict(best_model, X):\n    classifier = best_model.named_steps['classifier']\n    classifier_cls = type(classifier)\n    classifier_cls.__sklearn_tags__ = lambda self: LogisticRegression().__sklearn_tags__()\n    classifier_cls.__sklearn_is_fitted__ = lambda self: hasattr(self, 'fitted_')\n    X_scaled = best_model.named_steps['scaler'].transform(X)\n    return classifier.predict(X_scaled)\n\nbest_model = model.best_estimator_\ny_pred = combo_predict(best_model, X)\naccuracy_score(y, y_pred), f1_score(y, y_pred)\n",
    )
    replace_cell_containing(
        "combo.ipynb",
        "model.best_estimator_[1].base_estimators[2]",
        "model.best_estimator_[1].base_estimators\n",
    )
    replace_cell_containing(
        "combo.ipynb",
        "for tr_index, te_index in StratifiedKFold(",
        "import pandas as pd\n\nr_df = []\n\nfor tr_index, te_index in StratifiedKFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 5, shuffle=True, random_state=37).split(X, y):\n    X_tr, y_tr = X[tr_index,:], y[tr_index]\n    X_te, y_te = X[te_index,:], y[te_index]\n    \n    print(X_tr.shape, y_tr.shape, X_te.shape, y_te.shape)\n    \n    model = get_stacking_model()\n    model.fit(X_tr, y_tr)\n    \n    y_pred = combo_predict(model.best_estimator_, X_te)\n    \n    accuracy = accuracy_score(y_te, y_pred)\n    f1 = f1_score(y_te, y_pred)\n    \n    r_df.append({'accuracy': accuracy, 'f1': f1})\n    \nr_df = pd.DataFrame(r_df)\nr_df\n",
    )
    replace_cell_containing(
        "imbalanced-learn.ipynb",
        "def get_oversampler(sampler):",
        "from imblearn.over_sampling import RandomOverSampler, SMOTE, ADASYN, BorderlineSMOTE, SVMSMOTE, KMeansSMOTE\n"
        "from sklearn.cluster import KMeans\n"
        "from collections import Counter\n"
        "from itertools import chain\n\n"
        "def get_oversampler(sampler):\n"
        "    if 'adasyn' == sampler:\n"
        "        p = {\n"
        "            'random_state': 37,\n"
        "            'n_neighbors': 5\n"
        "        }\n"
        "        return ADASYN(**p)\n"
        "    elif 'borderlinesmote' == sampler:\n"
        "        p = {\n"
        "            'random_state': 37,\n"
        "            'k_neighbors': 5,\n"
        "            'm_neighbors': 10\n"
        "        }\n"
        "        return BorderlineSMOTE(**p)\n"
        "    elif 'svmsmote' == sampler:\n"
        "        p = {\n"
        "            'random_state': 37,\n"
        "            'k_neighbors': 5,\n"
        "            'm_neighbors': 10\n"
        "        }\n"
        "        return SVMSMOTE(**p)\n"
        "    elif 'kmeanssmote' == sampler:\n"
        "        kmeans = KMeans(n_clusters=5, random_state=37)\n"
        "        p = {\n"
        "            'random_state': 37,\n"
        "            'k_neighbors': 5,\n"
        "            'kmeans_estimator': kmeans\n"
        "        }\n"
        "        return KMeansSMOTE(**p)\n"
        "    elif 'random' == sampler:\n"
        "        p = {\n"
        "            'random_state': 37\n"
        "        }\n"
        "        return RandomOverSampler(**p)\n"
        "    else:\n"
        "        p = {\n"
        "            'random_state': 37,\n"
        "            'k_neighbors': 5\n"
        "        }\n"
        "        return SMOTE(**p)\n\n"
        "def get_results(sampler, f):\n"
        "    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=37)\n\n"
        "    results = []\n"
        "    for fold, (tr, te) in enumerate(skf.split(X, y)):\n"
        "        X_tr, X_te = X.iloc[tr], X.iloc[te]\n"
        "        y_tr, y_te = y.iloc[tr], y.iloc[te]\n\n"
        "        counts = sorted(Counter(y_tr).items())\n"
        "        n_0, n_1 = counts[0][1], counts[1][1]\n\n"
        "        if sampler != 'none':\n"
        "            sampling_approach = f(sampler)\n"
        "            X_tr, y_tr = sampling_approach.fit_resample(X_tr, y_tr)\n\n"
        "        model = RandomForestClassifier(n_jobs=-1, random_state=37)\n"
        "        model.fit(X_tr, y_tr)\n"
        "        y_pr = model.predict_proba(X_te)[:,1]\n\n"
        "        auc = roc_auc_score(y_te, y_pr)\n"
        "        aps = average_precision_score(y_te, y_pr)\n\n"
        "        counts = sorted(Counter(y_tr).items())\n"
        "        r_0, r_1 = counts[0][1], counts[1][1]\n\n"
        "        results.append({\n"
        "            'sampler': sampler,\n"
        "            'auc': auc, \n"
        "            'aps': aps, \n"
        "            'n_maj': n_0, \n"
        "            'r_maj': r_0, \n"
        "            'n_min': n_1, \n"
        "            'r_min': r_1\n"
        "        })\n"
        "        \n"
        "    return results\n",
    )
    replace_cell_containing(
        "imbalanced-learn.ipynb",
        "def get_undersampler(sampler):",
        "from imblearn.under_sampling import RandomUnderSampler, NearMiss, EditedNearestNeighbours, RepeatedEditedNearestNeighbours, CondensedNearestNeighbour, OneSidedSelection, NeighbourhoodCleaningRule, InstanceHardnessThreshold\n\n"
        "def get_undersampler(sampler):\n"
        "    if 'random' == sampler:\n"
        "        p = {\n"
        "            'random_state': 37\n"
        "        }\n"
        "        return RandomUnderSampler(**p)\n"
        "    elif 'nearmiss1' == sampler:\n"
        "        p = {\n"
        "            'version': 1\n"
        "        }\n"
        "        return NearMiss(**p)\n"
        "    elif 'nearmiss2' == sampler:\n"
        "        p = {\n"
        "            'version': 2\n"
        "        }\n"
        "        return NearMiss(**p)\n"
        "    elif 'nearmiss3' == sampler:\n"
        "        p = {\n"
        "            'version': 3\n"
        "        }\n"
        "        return NearMiss(**p)\n"
        "    elif 'editednn' == sampler:\n"
        "        return EditedNearestNeighbours()\n"
        "    elif 'reditednn' == sampler:\n"
        "        return RepeatedEditedNearestNeighbours()\n"
        "    elif 'condensednn' == sampler:\n"
        "        p = {\n"
        "            'random_state': 37\n"
        "        }\n"
        "        return CondensedNearestNeighbour(**p)\n"
        "    elif 'onesided' == sampler:\n"
        "        p = {\n"
        "            'random_state': 37\n"
        "        }\n"
        "        return OneSidedSelection(**p)\n"
        "    elif 'neighcleanrule' == sampler:\n"
        "        return NeighbourhoodCleaningRule()\n"
        "    elif 'instancehardthresh' == sampler:\n"
        "        estimator = LogisticRegression(solver='lbfgs', multi_class='auto')\n"
        "        p = {\n"
        "            'estimator': estimator,\n"
        "            'random_state': 37\n"
        "        }\n"
        "        return InstanceHardnessThreshold(**p)\n",
    )
    replace_cell_containing(
        "imbalanced-learn.ipynb",
        "def get_combine(sampler):",
        "from imblearn.combine import SMOTEENN, SMOTETomek\n\n"
        "def get_combine(sampler):\n"
        "    if 'smoteenn' == sampler:\n"
        "        p = {\n"
        "            'random_state': 37,\n"
        "            'k_neighbors': 5\n"
        "        }\n"
        "        smote = SMOTE(**p)\n"
        "    \n"
        "        enn = EditedNearestNeighbours()\n"
        "        \n"
        "        p = {\n"
        "            'smote': smote,\n"
        "            'enn': enn,\n"
        "            'random_state': 37\n"
        "        }\n"
        "        return SMOTEENN(**p)\n"
        "    elif 'smotetomek' == sampler:\n"
        "        p = {\n"
        "            'random_state': 37,\n"
        "            'k_neighbors': 5\n"
        "        }\n"
        "        smote = SMOTE(**p)\n"
        "        \n"
        "        p = {\n"
        "            'smote': smote,\n"
        "            'random_state': 37\n"
        "        }\n"
        "        return SMOTETomek(**p)\n",
    )
    replace_cell_containing(
        "imbalanced-learn.ipynb",
        "def get_model(n_splits=5):",
        "from imblearn.pipeline import Pipeline\n"
        "from sklearn.ensemble import RandomForestClassifier\n"
        "from sklearn.metrics import roc_auc_score, average_precision_score, make_scorer\n"
        "from sklearn.model_selection import StratifiedKFold, GridSearchCV\n"
        "from sklearn.preprocessing import MinMaxScaler\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "def get_model(n_splits=None):\n"
        "    n_splits = n_splits or (2 if SCIKIT_INTRO_CHECK_MODE else 5)\n"
        "    cv = StratifiedKFold(**{\n"
        "        'n_splits': n_splits,\n"
        "        'shuffle': True,\n"
        "        'random_state': 37\n"
        "    })\n\n"
        "    auc_scorer = make_scorer(\n"
        "        roc_auc_score, \n"
        "        greater_is_better=True, \n"
        "        response_method='predict_proba', \n"
        "        multi_class='ovo')\n\n"
        "    scoring = {\n"
        "      'auc': auc_scorer\n"
        "    }\n\n"
        "    scaler = MinMaxScaler()\n"
        "    sampler = ADASYN(**{\n"
        "        'random_state': 37\n"
        "    })\n"
        "    classifier = RandomForestClassifier(**{\n"
        "        'random_state': 37,\n"
        "        'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1,\n"
        "        'verbose': 0\n"
        "    })\n\n"
        "    pipeline = Pipeline([\n"
        "        ('scaler', scaler),\n"
        "        ('sampler', sampler),\n"
        "        ('classifier', classifier)\n"
        "    ])\n\n"
        "    param_grid = {\n"
        "      'sampler__sampling_strategy': ['auto'] if SCIKIT_INTRO_CHECK_MODE else ['all', 'auto'],\n"
        "      'sampler__n_neighbors': [3] if SCIKIT_INTRO_CHECK_MODE else [3, 5],\n"
        "      'classifier__n_estimators': [25] if SCIKIT_INTRO_CHECK_MODE else [50, 100]\n"
        "    }\n\n"
        "    model = GridSearchCV(**{\n"
        "        'estimator': pipeline,\n"
        "        'cv': cv,\n"
        "        'param_grid': param_grid,\n"
        "        'verbose': 0 if SCIKIT_INTRO_CHECK_MODE else 1,\n"
        "        'scoring': scoring,\n"
        "        'refit': 'auc',\n"
        "        'error_score': np.nan,\n"
        "        'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1\n"
        "    })\n"
        "    return model\n",
    )
    replace_cell_containing(
        "lightgbm.ipynb",
        "from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error",
        "from sklearn.pipeline import Pipeline\n"
        "from sklearn.impute import SimpleImputer\n"
        "from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error\n"
        "import lightgbm as lgbm\n"
        "import numpy as np\n"
        "import optuna\n\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "np.random.seed(37)\n"
        "optuna.logging.set_verbosity(optuna.logging.WARNING)\n\n"
        "def get_model(imputer_params={}, regressor_params={}):\n"
        "    model = Pipeline([\n"
        "        ('imputer', SimpleImputer(**imputer_params)),\n"
        "        ('regressor', lgbm.LGBMRegressor(**regressor_params))\n"
        "    ])\n"
        "    \n"
        "    return model\n\n"
        "def objective(trial):\n"
        "    i_params = {\n"
        "        'strategy': trial.suggest_categorical('strategy', ['mean', 'median', 'most_frequent'])\n"
        "    }\n"
        "    \n"
        "    r_params = {\n"
        "        'boosting_type': 'gbdt',\n"
        "        'num_leaves': trial.suggest_int('num_leaves', 10, 20) if SCIKIT_INTRO_CHECK_MODE else trial.suggest_int('num_leaves', 30, 50),\n"
        "        'max_depth': trial.suggest_int('max_depth', 3, 12) if SCIKIT_INTRO_CHECK_MODE else trial.suggest_int('max_depth', 0, 100),\n"
        "        'n_estimators': trial.suggest_int('n_estimators', 10, 30) if SCIKIT_INTRO_CHECK_MODE else trial.suggest_int('n_estimators', 80, 200),\n"
        "        'class_weight': 'balanced',\n"
        "        'random_state': 37,\n"
        "        'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1\n"
        "    }\n"
        "    \n"
        "    model = get_model(i_params, r_params)\n"
        "    model.fit(X_tr, y_tr)\n"
        "    \n"
        "    y_pred = model.predict(X_te)\n"
        "    \n"
        "    mae = mean_absolute_error(y_te, y_pred)\n"
        "    rmse = root_mean_squared_error(y_te, y_pred)\n"
        "    r2s = r2_score(y_te, y_pred)\n"
        "    \n"
        "    trial.set_user_attr('mae', mae)\n"
        "    trial.set_user_attr('rmse', rmse)\n"
        "    trial.set_user_attr('r2s', r2s)\n"
        "    \n"
        "    return mae\n",
    )
    replace_cell_containing(
        "lightgbm.ipynb",
        "study = optuna.create_study(**{",
        "study = optuna.create_study(**{\n"
        "    'study_name': 'lightgbm-study',\n"
        "    'storage': 'sqlite:///_temp/lightgbm-study.db',\n"
        "    'load_if_exists': True,\n"
        "    'direction': 'minimize',\n"
        "    'sampler': optuna.samplers.TPESampler(seed=37),\n"
        "    'pruner': optuna.pruners.MedianPruner(n_warmup_steps=10)\n"
        "})\n\n"
        "study.optimize(**{\n"
        "    'func': objective, \n"
        "    'n_trials': 2 if SCIKIT_INTRO_CHECK_MODE else 100,\n"
        "    'n_jobs': 1,\n"
        "    'show_progress_bar': False\n"
        "})\n",
    )
    replace_cell_containing(
        "lightgbm.ipynb",
        "from optuna.visualization import plot_optimization_history",
        "from optuna.visualization import plot_optimization_history\n\n"
        "if SCIKIT_INTRO_CHECK_MODE:\n"
        "    print('Skipping Optuna optimization history plot in check mode')\n"
        "else:\n"
        "    try:\n"
        "        plot_optimization_history(**{\n"
        "            'study': study\n"
        "        })\n"
        "    except ImportError:\n"
        "        print('plotly is not installed; skipping Optuna optimization history plot')\n",
    )
    replace_cell_containing(
        "lightgbm.ipynb",
        "from optuna.visualization import plot_parallel_coordinate",
        "from optuna.visualization import plot_parallel_coordinate\n\n"
        "if SCIKIT_INTRO_CHECK_MODE:\n"
        "    print('Skipping Optuna parallel coordinate plot in check mode')\n"
        "else:\n"
        "    try:\n"
        "        plot_parallel_coordinate(**{\n"
        "            'study': study\n"
        "        })\n"
        "    except ImportError:\n"
        "        print('plotly is not installed; skipping Optuna parallel coordinate plot')\n",
    )
    replace_cell_containing(
        "lightgbm.ipynb",
        "from optuna.visualization import plot_param_importances",
        "from optuna.visualization import plot_param_importances\n\n"
        "if SCIKIT_INTRO_CHECK_MODE:\n"
        "    print('Skipping Optuna parameter importance plot in check mode')\n"
        "else:\n"
        "    try:\n"
        "        plot_param_importances(**{\n"
        "            'study': study\n"
        "        })\n"
        "    except ImportError:\n"
        "        print('plotly is not installed; skipping Optuna parameter importance plot')\n",
    )
    replace_cell_containing(
        "lightgbm.ipynb",
        "from optuna.visualization import plot_slice",
        "from optuna.visualization import plot_slice\n\n"
        "if SCIKIT_INTRO_CHECK_MODE:\n"
        "    print('Skipping Optuna slice plot in check mode')\n"
        "else:\n"
        "    try:\n"
        "        plot_slice(**{\n"
        "            'study': study,\n"
        "            'params': ['num_leaves', 'max_depth', 'n_estimators']\n"
        "        })\n"
        "    except ImportError:\n"
        "        print('plotly is not installed; skipping Optuna slice plot')\n",
    )
    replace_cell_containing(
        "lightgbm.ipynb",
        "from optuna.visualization import plot_contour",
        "from optuna.visualization import plot_contour\n\n"
        "if SCIKIT_INTRO_CHECK_MODE:\n"
        "    print('Skipping Optuna contour plot in check mode')\n"
        "else:\n"
        "    try:\n"
        "        plot_contour(**{\n"
        "            'study': study,\n"
        "            'params': ['num_leaves', 'max_depth', 'n_estimators']\n"
        "        })\n"
        "    except ImportError:\n"
        "        print('plotly is not installed; skipping Optuna contour plot')\n",
    )
    replace_cell_containing(
        "lightgbm.ipynb",
        "from optuna.visualization import plot_edf",
        "from optuna.visualization import plot_edf\n\n"
        "if SCIKIT_INTRO_CHECK_MODE:\n"
        "    print('Skipping Optuna EDF plot in check mode')\n"
        "else:\n"
        "    try:\n"
        "        plot_edf(study)\n"
        "    except ImportError:\n"
        "        print('plotly is not installed; skipping Optuna EDF plot')\n",
    )
    replace_cell_containing(
        "optuna.ipynb",
        "from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error",
        "from sklearn.pipeline import Pipeline\n"
        "from sklearn.ensemble import RandomForestRegressor\n"
        "from sklearn.impute import SimpleImputer\n"
        "from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error\n"
        "import numpy as np\n"
        "import optuna\n\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "np.random.seed(37)\n"
        "optuna.logging.set_verbosity(optuna.logging.WARNING)\n\n"
        "def get_model(imputer_params={}, regressor_params={}):\n"
        "    model = Pipeline([\n"
        "        ('imputer', SimpleImputer(**imputer_params)),\n"
        "        ('regressor', RandomForestRegressor(**regressor_params))\n"
        "    ])\n"
        "    \n"
        "    return model\n\n"
        "def objective(trial):\n"
        "    i_params = {\n"
        "        'strategy': trial.suggest_categorical('strategy', ['mean', 'median', 'most_frequent'])\n"
        "    }\n"
        "    \n"
        "    r_params = {\n"
        "        'n_estimators': trial.suggest_int('n_estimators', 100, 200),\n"
        "        'min_samples_split': trial.suggest_int('min_samples_split', 2, 10),\n"
        "        'min_samples_leaf': trial.suggest_int('min_samples_leaf', 1, 10),\n"
        "        'criterion': trial.suggest_categorical('criterion', ['squared_error', 'absolute_error', 'poisson']),\n"
        "        'max_features': trial.suggest_categorical('max_features', [1.0, 'sqrt', 'log2']),\n"
        "        'bootstrap': False,\n"
        "        'oob_score': False,\n"
        "        'warm_start': trial.suggest_categorical('warm_start', [True, False]),\n"
        "        'ccp_alpha': trial.suggest_float('ccp_alpha', 0, 1),\n"
        "        'max_depth': trial.suggest_int('max_depth', 1, 100),\n"
        "        'random_state': 37\n"
        "    }\n"
        "    \n"
        "    model = get_model(i_params, r_params)\n"
        "    model.fit(X_tr, y_tr)\n"
        "    \n"
        "    y_pred = model.predict(X_te)\n"
        "    \n"
        "    mae = mean_absolute_error(y_te, y_pred)\n"
        "    rmse = root_mean_squared_error(y_te, y_pred)\n"
        "    r2s = r2_score(y_te, y_pred)\n"
        "    \n"
        "    trial.set_user_attr('mae', mae)\n"
        "    trial.set_user_attr('rmse', rmse)\n"
        "    trial.set_user_attr('r2s', r2s)\n"
        "    \n"
        "    return mae\n",
    )
    replace_cell_containing(
        "optuna.ipynb",
        "study = optuna.create_study(**{",
        "study = optuna.create_study(**{\n"
        "    'study_name': 'optuna-rf-study',\n"
        "    'storage': 'sqlite:///_temp/optuna-rf-study.db',\n"
        "    'load_if_exists': True,\n"
        "    'direction': 'minimize',\n"
        "    'sampler': optuna.samplers.TPESampler(seed=37),\n"
        "    'pruner': optuna.pruners.MedianPruner(n_warmup_steps=10)\n"
        "})\n\n"
        "study.optimize(**{\n"
        "    'func': objective, \n"
        "    'n_trials': 5 if SCIKIT_INTRO_CHECK_MODE else 100,\n"
        "    'n_jobs': 1,\n"
        "    'show_progress_bar': False\n"
        "})\n",
    )
    replace_cell_containing(
        "optuna.ipynb",
        "_study = optuna.create_study(**{",
        "_study = optuna.create_study(**{\n"
        "    'study_name': 'optuna-rf-study',\n"
        "    'storage': 'sqlite:///_temp/optuna-rf-study.db',\n"
        "    'load_if_exists': True,\n"
        "    'direction': 'minimize',\n"
        "    'sampler': optuna.samplers.TPESampler(seed=37),\n"
        "    'pruner': optuna.pruners.MedianPruner(n_warmup_steps=10)\n"
        "})\n\n"
        "_study.optimize(**{\n"
        "    'func': objective, \n"
        "    'n_trials': 3 if SCIKIT_INTRO_CHECK_MODE else 10,\n"
        "    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else 5,\n"
        "    'show_progress_bar': False\n"
        "})\n",
    )
    replace_cell_containing(
        "optuna.ipynb",
        "from optuna.visualization import plot_optimization_history",
        "from optuna.visualization import plot_optimization_history\n\n"
        "try:\n"
        "    plot_optimization_history(**{\n"
        "        'study': _study\n"
        "    })\n"
        "except ImportError:\n"
        "    print('plotly is not installed; skipping Optuna optimization history plot')\n",
    )
    replace_cell_containing(
        "optuna.ipynb",
        "from optuna.visualization import plot_parallel_coordinate",
        "from optuna.visualization import plot_parallel_coordinate\n\n"
        "try:\n"
        "    plot_parallel_coordinate(**{\n"
        "        'study': _study\n"
        "    })\n"
        "except ImportError:\n"
        "    print('plotly is not installed; skipping Optuna parallel coordinate plot')\n",
    )
    replace_cell_containing(
        "optuna.ipynb",
        "from optuna.visualization import plot_param_importances",
        "from optuna.visualization import plot_param_importances\n\n"
        "try:\n"
        "    plot_param_importances(**{\n"
        "        'study': _study\n"
        "    })\n"
        "except ImportError:\n"
        "    print('plotly is not installed; skipping Optuna parameter importance plot')\n",
    )
    replace_cell_containing(
        "optuna.ipynb",
        "from optuna.visualization import plot_slice",
        "from optuna.visualization import plot_slice\n\n"
        "try:\n"
        "    plot_slice(**{\n"
        "        'study': _study,\n"
        "        'params': ['criterion', 'ccp_alpha', 'warm_start']\n"
        "    })\n"
        "except ImportError:\n"
        "    print('plotly is not installed; skipping Optuna slice plot')\n",
    )
    replace_cell_containing(
        "optuna.ipynb",
        "from optuna.visualization import plot_contour",
        "from optuna.visualization import plot_contour\n\n"
        "try:\n"
        "    plot_contour(**{\n"
        "        'study': _study,\n"
        "        'params': ['criterion', 'min_samples_leaf', 'max_depth']\n"
        "    })\n"
        "except ImportError:\n"
        "    print('plotly is not installed; skipping Optuna contour plot')\n",
    )
    replace_cell_containing(
        "optuna.ipynb",
        "from optuna.visualization import plot_edf",
        "from optuna.visualization import plot_edf\n\n"
        "try:\n"
        "    plot_edf(_study)\n"
        "except ImportError:\n"
        "    print('plotly is not installed; skipping Optuna EDF plot')\n",
    )
    replace_cell_containing(
        "pygam.ipynb",
        "from scipy.stats import norm",
        "import numpy as np\n"
        "import pandas as pd\n"
        "import random\n"
        "import bisect\n"
        "from scipy import sparse\n"
        "from scipy.stats import norm\n"
        "import matplotlib.pyplot as plt\n"
        "from sklearn.preprocessing import MinMaxScaler\n\n"
        "if not hasattr(sparse.spmatrix, 'A'):\n"
        "    sparse.spmatrix.A = property(lambda self: self.toarray())\n\n"
        "plt.style.use('ggplot')\n"
        "np.random.seed(37)\n"
        "random.seed(37)\n\n"
        "def mix(gaussians, n_samples=1_000, sample_delta=5, max_time=5):\n"
        "    def sample(items):\n"
        "        first = np.array([items[0]])\n"
        "        mid = items[np.arange(1, len(items), sample_delta)]\n"
        "        last = np.array([items[-1]])\n"
        "        \n"
        "        sample = np.concatenate([first, mid, last])\n"
        "        return sample\n"
        "        \n"
        "    s = pd.concat([pd.Series(g.rvs(size=n_samples)) for g in gaussians]).reset_index(drop=True)\n"
        "    c = (s.value_counts().sort_index() / len(s)).cumsum()\n"
        "    \n"
        "    i = MinMaxScaler((0, max_time)).fit_transform(c.index.values.reshape(-1, 1)).reshape(1, -1)[0]\n"
        "    i = sample(i)\n"
        "    v = sample(c.values)\n"
        "    n = pd.Series(v, index=i, dtype=np.float64)\n"
        "    \n"
        "    return s, c, n\n\n"
        "s, c, n = mix([norm(loc=10, scale=1), norm(loc=3.7, scale=2)])",
    )
    replace_cell_containing(
        "pyod.ipynb",
        "knn = KNN(contamination=0.30, n_jobs=-1)",
        "from pyod.models.knn import KNN\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "knn = KNN(contamination=0.30, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)\n"
        "knn.fit(X)\n\n"
        "y_pred = knn.predict(X)\n",
    )
    replace_cell_containing(
        "pyod.ipynb",
        "for c in np.arange(0.1, 0.5+0.01, 0.01):",
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "r_df = []\n"
        "contaminations = np.arange(0.1, 0.31, 0.1) if SCIKIT_INTRO_CHECK_MODE else np.arange(0.1, 0.5+0.01, 0.01)\n\n"
        "for c in contaminations:\n"
        "    knn = KNN(contamination=c, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)\n"
        "    knn.fit(X)\n\n"
        "    y_p = knn.predict(X)\n"
        "    \n"
        "    r = {\n"
        "        'contamination': c,\n"
        "        'acc': accuracy_score(y, y_p),\n"
        "        'f1': f1_score(y, y_p),\n"
        "        'aps': average_precision_score(y, y_p),\n"
        "        'roc': roc_auc_score(y, y_p)\n"
        "    }\n"
        "    r_df.append(r)\n"
        "    \n"
        "r_df = pd.DataFrame(r_df)\n"
        "r_df.index = r_df.contamination\n",
    )
    replace_cell_containing(
        "pyod.ipynb",
        "import itertools",
        "import itertools\n"
        "from pyod.utils.utility import standardizer\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "def do_learn(n, c):\n"
        "    knn = KNN(contamination=c, n_neighbors=n, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)\n"
        "    knn.fit(X)\n"
        "    return knn.predict(X)\n\n"
        "def get_key(n, c):\n"
        "    return f'n_{n:03}_c={c:.2f}'\n"
        "    \n"
        "n_neighbors = [10, 30, 50] if SCIKIT_INTRO_CHECK_MODE else list(np.arange(10, 210, 10))\n"
        "contaminations = [0.1, 0.2, 0.3] if SCIKIT_INTRO_CHECK_MODE else list(np.arange(0.1, 0.5 + 0.01, 0.01))\n\n"
        "r_df = pd.DataFrame({get_key(n, c): do_learn(n, c) \n"
        "                     for n, c in itertools.product(n_neighbors, contaminations)})\n"
        "r_mat = standardizer(r_df)\n",
    )
    replace_cell_containing(
        "pyod.ipynb",
        "from pyod.models.combination import aom, moa, average, maximization",
        "from pyod.models.combination import aom, moa, average, maximization\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "def apply_combiner(f, scores):\n"
        "    if SCIKIT_INTRO_CHECK_MODE and f in {aom, moa}:\n"
        "        return f(scores, n_buckets=3)\n"
        "    return f(scores)\n\n"
        "pd.DataFrame([{'score': f.__name__, 'roc': roc_auc_score(y, apply_combiner(f, r_mat)), 'aps': average_precision_score(y, apply_combiner(f, r_mat))} \n"
        "              for f in [average, moa, average, maximization]])\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "import shap",
        "import shap\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE, make_shap_classification_frame\n\n"
        "def shap_select_class(values, class_index=1):\n"
        "    if isinstance(values, list):\n"
        "        return values[class_index]\n"
        "    arr = np.asarray(values)\n"
        "    if arr.ndim >= 3:\n"
        "        return arr[..., class_index]\n"
        "    return arr\n\n"
        "def shap_select_expected_value(values, class_index=1):\n"
        "    if isinstance(values, list):\n"
        "        return values[class_index]\n"
        "    arr = np.asarray(values)\n"
        "    if arr.ndim == 0:\n"
        "        return values\n"
        "    return arr[class_index]\n\n"
        "def shap_row(values, index):\n"
        "    idx = min(index, len(values) - 1)\n"
        "    return values[idx, :], idx\n\n"
        "shap.initjs()\n",
    )
    replace_exact_source(
        "shap.ipynb",
        "df = make_classification(n=20 if SCIKIT_INTRO_CHECK_MODE else 100)\nX = df[['x0', 'x1']]\ny = df.y\n",
        "df = make_shap_classification_frame(n_samples=20 if SCIKIT_INTRO_CHECK_MODE else 100)\nX = df[['x0', 'x1']]\ny = df.y\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "df = make_classification(n=20 if SCIKIT_INTRO_CHECK_MODE else 100)",
        "df = make_shap_classification_frame(n_samples=20 if SCIKIT_INTRO_CHECK_MODE else 100)\n"
        "X = df[['x0', 'x1']]\n"
        "y = df.y\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "model = RandomForestClassifier(n_estimators=100, random_state=37)",
        "from sklearn.ensemble import RandomForestClassifier\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "model = RandomForestClassifier(n_estimators=20 if SCIKIT_INTRO_CHECK_MODE else 100, random_state=37)\n"
        "model.fit(X, y.values.reshape(1, -1)[0])\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "explainer = shap.TreeExplainer(model)",
        "explainer = shap.TreeExplainer(model)\n"
        "shap_values = explainer.shap_values(X)\n"
        "shap_interaction_values = explainer.shap_interaction_values(X)\n"
        "tree_expected_value = shap_select_expected_value(explainer.expected_value, 1)\n"
        "tree_shap_values = shap_select_class(shap_values, 1)\n"
        "tree_shap_interaction_values = shap_select_class(shap_interaction_values, 1)\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.force_plot(explainer.expected_value[1], shap_values[1][0,:], X.iloc[0,:])",
        "tree_row, tree_idx = shap_row(tree_shap_values, 0)\n"
        "shap.force_plot(tree_expected_value, tree_row, X.iloc[tree_idx,:])\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.force_plot(explainer.expected_value[1], shap_values[1][1,:], X.iloc[1,:])",
        "tree_row, tree_idx = shap_row(tree_shap_values, 1)\n"
        "shap.force_plot(tree_expected_value, tree_row, X.iloc[tree_idx,:])\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.force_plot(explainer.expected_value[1], shap_values[1][95,:], X.iloc[95,:])",
        "tree_row, tree_idx = shap_row(tree_shap_values, 95)\n"
        "shap.force_plot(tree_expected_value, tree_row, X.iloc[tree_idx,:])\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.force_plot(explainer.expected_value[1], shap_values[1], X)",
        "shap.force_plot(tree_expected_value, tree_shap_values, X)\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.summary_plot(shap_values[1], X)",
        "shap.summary_plot(tree_shap_values, X)\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.dependence_plot('x0', shap_values[1], X)",
        "shap.dependence_plot('x0', tree_shap_values, X)\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.dependence_plot('x1', shap_values[1], X)",
        "shap.dependence_plot('x1', tree_shap_values, X)\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.dependence_plot(('x0', 'x0'), shap_interaction_values[1], X)",
        "shap.dependence_plot(('x0', 'x0'), tree_shap_interaction_values, X)\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.dependence_plot(('x0', 'x1'), shap_interaction_values[1], X)",
        "shap.dependence_plot(('x0', 'x1'), tree_shap_interaction_values, X)\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.dependence_plot(('x1', 'x1'), shap_interaction_values[1], X)",
        "shap.dependence_plot(('x1', 'x1'), tree_shap_interaction_values, X)\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.summary_plot(shap_interaction_values[1], X)",
        "shap.summary_plot(tree_shap_interaction_values, X)\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "model = LogisticRegression(fit_intercept=True, solver='saga', random_state=37)",
        "from sklearn.linear_model import LogisticRegression\n\n"
        "df = make_shap_classification_frame(n_samples=1000 if SCIKIT_INTRO_CHECK_MODE else 10000)\n"
        "X = df[['x0', 'x1']]\n"
        "y = df.y\n\n"
        "model = LogisticRegression(fit_intercept=True, solver='saga', random_state=37)\n"
        "model.fit(X, y.values.reshape(1, -1)[0])\n",
    )
    replace_exact_source(
        "shap.ipynb",
        "df = make_classification(n=1000 if SCIKIT_INTRO_CHECK_MODE else 10000)\nX = df[['x0', 'x1']]\ny = df.y\n\nmodel = LogisticRegression(fit_intercept=True, solver='saga', random_state=37)\nmodel.fit(X, y.values.reshape(1, -1)[0])\n",
        "from sklearn.linear_model import LogisticRegression\n\n"
        "df = make_shap_classification_frame(n_samples=1000 if SCIKIT_INTRO_CHECK_MODE else 10000)\n"
        "X = df[['x0', 'x1']]\n"
        "y = df.y\n\n"
        "model = LogisticRegression(fit_intercept=True, solver='saga', random_state=37)\n"
        "model.fit(X, y.values.reshape(1, -1)[0])\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "df = make_classification()",
        "df = make_shap_classification_frame(n_samples=20 if SCIKIT_INTRO_CHECK_MODE else 100)\n"
        "X = df[['x0', 'x1']]\n"
        "y = df.y\n",
    )
    replace_exact_source(
        "shap.ipynb",
        "df = make_classification()\nX = df[['x0', 'x1']]\ny = df.y",
        "df = make_shap_classification_frame(n_samples=20 if SCIKIT_INTRO_CHECK_MODE else 100)\nX = df[['x0', 'x1']]\ny = df.y\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "explainer = shap.KernelExplainer(model.predict_proba, link='logit', data=X)",
        "explainer = shap.KernelExplainer(model.predict_proba, link='logit', data=X)\n"
        "shap_values = explainer.shap_values(X)\n"
        "kernel_expected_value = shap_select_expected_value(explainer.expected_value, 1)\n"
        "kernel_shap_values = shap_select_class(shap_values, 1)\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.force_plot(explainer.expected_value[1], shap_values[1][0,:], X.iloc[0,:], link='logit')",
        "kernel_row, kernel_idx = shap_row(kernel_shap_values, 0)\n"
        "shap.force_plot(kernel_expected_value, kernel_row, X.iloc[kernel_idx,:], link='logit')\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.force_plot(explainer.expected_value[1], shap_values[1][1,:], X.iloc[1,:], link='logit')",
        "kernel_row, kernel_idx = shap_row(kernel_shap_values, 1)\n"
        "shap.force_plot(kernel_expected_value, kernel_row, X.iloc[kernel_idx,:], link='logit')\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.force_plot(explainer.expected_value[1], shap_values[1][99,:], X.iloc[99,:], link='logit')",
        "kernel_row, kernel_idx = shap_row(kernel_shap_values, 99)\n"
        "shap.force_plot(kernel_expected_value, kernel_row, X.iloc[kernel_idx,:], link='logit')\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.force_plot(explainer.expected_value[1], shap_values[1], X, link='logit')",
        "shap.force_plot(kernel_expected_value, kernel_shap_values, X, link='logit')\n",
    )
    replace_cell_containing(
        "shap.ipynb",
        "shap.summary_plot(shap_values[1], X)",
        "shap.summary_plot(kernel_shap_values, X)\n",
    )
    replace_cell_containing(
        "tips.ipynb",
        "transformer = ColumnTransformer(transformers=[('cat', cat_pipeline, ['pet', 'color'])])",
        "from sklearn.impute import SimpleImputer\n"
        "from imblearn.pipeline import Pipeline\n"
        "from sklearn.preprocessing import OneHotEncoder\n"
        "from sklearn.compose import ColumnTransformer\n\n"
        "MISSING_TOKEN = '__missing__'\n\n"
        "cat_pipeline = Pipeline(steps=[\n"
        "    ('imputer', SimpleImputer(strategy='constant', fill_value=MISSING_TOKEN)),\n"
        "    ('ohe', OneHotEncoder(handle_unknown='ignore', sparse_output=False))\n"
        "])\n"
        "transformer = ColumnTransformer(transformers=[('cat', cat_pipeline, ['pet', 'color'])])\n\n"
        "pipeline = Pipeline(steps=[\n"
        "    ('preprocessing', transformer)\n"
        "])\n\n"
        "pipeline.fit_transform(df)\n",
    )
    replace_cell_containing(
        "tips.ipynb",
        "class OheAdjustmentTransformer:",
        "MISSING_TOKEN = '__missing__'\n\n"
        "class OheAdjustmentTransformer:\n"
        "    def __init__(self, transformer, num_columns, cat_columns, missing_suffix=MISSING_TOKEN):\n"
        "        self.transformer = transformer\n"
        "        self.num_columns = num_columns\n"
        "        self.cat_columns = cat_columns\n"
        "        self.missing_suffix = missing_suffix\n"
        "        \n"
        "    def adjust(self, df):\n"
        "        def make_null(d, cat_field, nan_field):\n"
        "            n_df = pd.DataFrame()\n"
        "            for field in d.columns:\n"
        "                if field == nan_field:\n"
        "                    continue\n"
        "                u_index = field.find('_')\n"
        "                val = field[u_index+1:]\n"
        "                n_field = f'{cat_field}_{val}'\n"
        "                n_df[n_field] = np.select([d[nan_field]==1], [np.nan], default=d[field])\n"
        "            \n"
        "            n_df.index = d.index\n"
        "            return n_df\n"
        "                \n"
        "        prefixes = [f'x{i}_' for i in range(len(self.cat_columns))]\n"
        "        c2n = {c: f'{p}{self.missing_suffix}' for c, p in zip(self.cat_columns, prefixes)}\n"
        "        df_cols = {c: [f for f in df.columns if f.startswith(p)] \n"
        "                   for c, p in zip(self.cat_columns, prefixes)}\n"
        "        dfs = {c: df[df_cols[c]] for c in df_cols}\n"
        "        n_dfs = {c: make_null(d, c, c2n[c]) for c, d in dfs.items()}\n"
        "        f_df = pd.concat([d for d in n_dfs.values()], axis=1)\n"
        "        \n"
        "        return f_df\n"
        "        \n"
        "    def fit(self, X=None, y=None):\n"
        "        return self\n"
        "    \n"
        "    def transform(self, X):\n"
        "        cat_columns = self.transformer.named_transformers_['cat'] \\\n"
        "            .named_steps['ohe'] \\\n"
        "            .get_feature_names_out()\n"
        "        cat_columns = list(cat_columns)\n"
        "        num_columns = self.num_columns\n"
        "        \n"
        "        if X.shape[1] == len(cat_columns):\n"
        "            columns = cat_columns\n"
        "        else:\n"
        "            columns = cat_columns + num_columns\n"
        "            \n"
        "        df = pd.DataFrame(X, columns=columns)\n"
        "        \n"
        "        if X.shape[1] == len(cat_columns):\n"
        "            return self.adjust(df)\n"
        "        else:\n"
        "            return self.adjust(df).join(df[num_columns])\n\n"
        "cat_columns = ['pet', 'color']\n"
        "num_columns = [c for c in df.columns if c not in cat_columns]\n\n"
        "cat_pipeline = Pipeline(steps=[\n"
        "    ('imputer', SimpleImputer(strategy='constant', fill_value=MISSING_TOKEN)),\n"
        "    ('ohe', OneHotEncoder(handle_unknown='ignore', sparse_output=False))\n"
        "])\n\n"
        "transformer = ColumnTransformer(\n"
        "    transformers=[('cat', cat_pipeline, cat_columns)], \n"
        "    remainder='passthrough')\n\n"
        "df_pipeline = Pipeline(steps=[\n"
        "    ('df', OheAdjustmentTransformer(transformer, num_columns, cat_columns))\n"
        "])\n\n"
        "pipeline = Pipeline(steps=[\n"
        "    ('preprocessing', transformer),\n"
        "    ('postprocessing', df_pipeline)\n"
        "])\n\n"
        "pipeline.fit_transform(df)\n",
    )
    replace_cell_containing(
        "visualizing.ipynb",
        "sns.distplot(X[:,i], ax=ax, color=next(colors), kde=True, norm_hist=True, hist=True)",
        "%matplotlib inline\n\n"
        "import matplotlib.pyplot as plt\n"
        "import seaborn as sns\n"
        "from itertools import cycle\n\n"
        "colors = cycle(['r', 'g', 'b', 'm'])\n"
        "columns=['sepal_width', 'sepal_height', 'petal_width', 'petal_height']\n"
        "n_vars = len(columns)\n\n"
        "n_cols = 4\n"
        "n_rows = (n_vars + n_cols - 1) // n_cols\n"
        "n_plots = n_cols * n_rows\n\n"
        "fig = plt.figure(figsize=(20, 3))\n\n"
        "for i in range(n_plots):\n"
        "    ax = fig.add_subplot(n_rows, n_cols, i + 1)\n"
        "    \n"
        "    if i < n_vars:\n"
        "        sns.histplot(X[:,i], ax=ax, color=next(colors), stat='density', kde=True)\n"
        "        ax.set_title(columns[i])\n"
        "        ax.set_xlabel('value')\n"
        "        ax.set_ylabel('probability')\n"
        "    else:\n"
        "        ax.axis('off')\n"
        "        \n"
        "plt.tight_layout()\n",
    )
    replace_cell_containing(
        "visualizing.ipynb",
        "sns.boxplot(X[:,i], ax=ax, color=next(colors))",
        "colors = cycle(['r', 'g', 'b', 'm'])\n"
        "n_cols = 4\n"
        "n_rows = (n_vars + n_cols - 1) // n_cols\n"
        "n_plots = n_cols * n_rows\n\n"
        "fig = plt.figure(figsize=(20, 3))\n\n"
        "for i in range(n_plots):\n"
        "    ax = fig.add_subplot(n_rows, n_cols, i + 1)\n"
        "    \n"
        "    if i < n_vars:\n"
        "        sns.boxplot(x=X[:,i], ax=ax, color=next(colors))\n"
        "        ax.set_title(columns[i])\n"
        "        ax.set_xlabel('value')\n"
        "    else:\n"
        "        ax.axis('off')\n"
        "        \n"
        "plt.tight_layout()\n",
    )
    replace_cell_containing(
        "visualizing.ipynb",
        "sns.kdeplot(x, y, shade=True, cmap=next(colors))",
        "from itertools import combinations\n\n"
        "colors = cycle(['Reds', 'Greens', 'Blues', 'Purples'])\n"
        "columns=['sepal_width', 'sepal_height', 'petal_width', 'petal_height']\n"
        "pairs = [comb for comb in combinations(columns, 2) if comb[0] != comb[1]]\n"
        "n_pairs = len(pairs)\n\n"
        "n_cols = 6\n"
        "n_rows = (n_pairs + n_cols - 1) // n_cols\n"
        "n_plots = n_cols * n_rows\n\n"
        "fig = plt.figure(figsize=(20, 3))\n\n"
        "for i in range(n_plots):\n"
        "    ax = fig.add_subplot(n_rows, n_cols, i + 1)\n"
        "    \n"
        "    if i < n_pairs:\n"
        "        label_x = pairs[i][0]\n"
        "        label_y = pairs[i][1]\n"
        "        \n"
        "        x = df[label_x]\n"
        "        y = df[label_y]\n"
        "        sns.kdeplot(x=x, y=y, fill=True, cmap=next(colors), ax=ax)\n"
        "    else:\n"
        "        ax.axis('off')\n"
        "        \n"
        "plt.tight_layout()\n",
    )
    replace_cell_containing(
        "visualizing.ipynb",
        "sns.regplot(x, y, color=next(colors))",
        "colors = cycle(['r', 'g', 'b', 'm'])\n"
        "columns=['sepal_width', 'sepal_height', 'petal_width', 'petal_height']\n"
        "pairs = [comb for comb in combinations(columns, 2) if comb[0] != comb[1]]\n"
        "n_pairs = len(pairs)\n\n"
        "n_cols = 6\n"
        "n_rows = (n_pairs + n_cols - 1) // n_cols\n"
        "n_plots = n_cols * n_rows\n\n"
        "fig = plt.figure(figsize=(20, 3))\n\n"
        "for i in range(n_plots):\n"
        "    ax = fig.add_subplot(n_rows, n_cols, i + 1)\n"
        "    \n"
        "    if i < n_pairs:\n"
        "        label_x = pairs[i][0]\n"
        "        label_y = pairs[i][1]\n"
        "        \n"
        "        x = df[label_x]\n"
        "        y = df[label_y]\n"
        "        sns.regplot(x=x, y=y, ax=ax, color=next(colors))\n"
        "    else:\n"
        "        ax.axis('off')\n"
        "        \n"
        "plt.tight_layout()\n",
    )
    replace_cell_containing(
        "xgboost.ipynb",
        "from sklearn.datasets import make_regression",
        "import numpy as np\n"
        "import random \n"
        "from sklearn.datasets import make_regression\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "random.seed(37)\n"
        "np.random.seed(37)\n\n"
        "X, y = make_regression(**{\n"
        "    'n_samples': 300 if SCIKIT_INTRO_CHECK_MODE else 1000,\n"
        "    'n_features': 10,\n"
        "    'n_targets': 1,\n"
        "    'bias': 5.3,\n"
        "    'random_state': 37\n"
        "})\n\n"
        "print(f'X shape = {X.shape}, y shape {y.shape}')\n",
    )
    replace_cell_containing(
        "xgboost.ipynb",
        "model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=10, seed=37)",
        "import xgboost as xgb\n\n"
        "model = xgb.XGBRegressor(\n"
        "    objective='reg:squarederror',\n"
        "    n_estimators=5 if SCIKIT_INTRO_CHECK_MODE else 10,\n"
        "    n_jobs=1,\n"
        "    seed=37,\n"
        ") \n"
        "model.fit(X_train, y_train)\n",
    )
    replace_cell_containing(
        "xgboost.ipynb",
        "def get_performance(n_estimators):",
        "import pandas as pd\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "def get_performance(n_estimators):\n"
        "    model = xgb.XGBRegressor(\n"
        "        objective='reg:squarederror',\n"
        "        n_estimators=n_estimators,\n"
        "        n_jobs=1,\n"
        "        seed=37,\n"
        "    ) \n"
        "    model.fit(X_train, y_train)\n\n"
        "    y_pred = model.predict(X_test)\n\n"
        "    mae = mean_absolute_error(y_test, y_pred)\n"
        "    rmse = np.sqrt(mean_squared_error(y_test, y_pred))\n"
        "    return {'mae': mae, 'rmse': rmse}\n\n"
        "n_estimators = [5, 10, 20] if SCIKIT_INTRO_CHECK_MODE else list(range(10, 101, 1))\n"
        "results = pd.DataFrame([get_performance(n) for n in n_estimators], index=n_estimators)\n",
    )
    replace_cell_containing(
        "xgboost.ipynb",
        "from sklearn.datasets import make_classification",
        "from sklearn.datasets import make_classification\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "X, y = make_classification(**{\n"
        "    'n_samples': 500 if SCIKIT_INTRO_CHECK_MODE else 2000,\n"
        "    'n_features': 20,\n"
        "    'n_informative': 10,\n"
        "    'n_redundant': 0,\n"
        "    'n_repeated': 0,\n"
        "    'n_classes': 2,\n"
        "    'random_state': 37\n"
        "})\n\n"
        "print(f'X shape = {X.shape}, y shape {y.shape}')\n",
    )
    replace_cell_containing(
        "xgboost.ipynb",
        "coef = np.array([2.0, -1.0, 3.5, 4.4])",
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "X, y = make_regression(**{\n"
        "    'n_samples': 300 if SCIKIT_INTRO_CHECK_MODE else 1000,\n"
        "    'n_features': 4,\n"
        "    'n_targets': 1,\n"
        "    'random_state': 37\n"
        "})\n\n"
        "coef = np.array([2.0, -1.0, 3.5, 4.4])\n"
        "baseline = np.e / np.power(1 + np.e, 2.0)\n"
        "y = np.exp(-X.dot(coef)) * baseline\n\n"
        "print(f'X shape = {X.shape}, y shape {y.shape}, coef shape = {coef.shape}')\n",
    )
    replace_cell_containing(
        "xgboost.ipynb",
        "model = xgb.train(params, dtrain, num_boost_round=40, evals=[(dtrain, 'train')])",
        "params = {\n"
        "    'objective': 'survival:aft',\n"
        "    'eval_metric': 'aft-nloglik',\n"
        "    'aft_loss_distribution': 'logistic',\n"
        "    'aft_loss_distribution_scale': 1.0,\n"
        "    'tree_method': 'hist' if SCIKIT_INTRO_CHECK_MODE else 'exact', \n"
        "    'learning_rate': 0.05, \n"
        "    'max_depth': 3 if SCIKIT_INTRO_CHECK_MODE else 5\n"
        "}\n"
        "model = xgb.train(\n"
        "    params,\n"
        "    dtrain,\n"
        "    num_boost_round=10 if SCIKIT_INTRO_CHECK_MODE else 40,\n"
        "    evals=[(dtrain, 'train')],\n"
        ")\n",
    )
    replace_cell_containing(
        "feature-selection.ipynb",
        "rf = RandomForestClassifier(max_depth=10, random_state=37, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)",
        "from sklearn.feature_selection import GenericUnivariateSelect\n"
        "from sklearn.feature_selection import chi2, mutual_info_classif\n"
        "from sklearn.model_selection import StratifiedKFold\n"
        "from sklearn.ensemble import RandomForestClassifier\n"
        "from sklearn.metrics import roc_auc_score\n"
        "from sklearn.pipeline import Pipeline\n"
        "from _runtime import SCIKIT_INTRO_CHECK_MODE\n\n"
        "def get_best_indexes(scores, max_index, reverse=True):\n"
        "    tups = sorted([(i, s) for i, s in enumerate(scores)], key=lambda tup: tup[1], reverse=reverse)\n"
        "    tups = tups[:max_index]\n"
        "    return [t[0] for t in tups]\n\n"
        "def get_classification_performance(tr_index, te_index, X, y, selector):\n"
        "    X_tr, X_te = X[tr_index], X[te_index]\n"
        "    y_tr, y_te = y[tr_index], y[te_index]\n"
        "    \n"
        "    rf = RandomForestClassifier(\n"
        "        n_estimators=10 if SCIKIT_INTRO_CHECK_MODE else 100,\n"
        "        max_depth=10,\n"
        "        random_state=37,\n"
        "        n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1,\n"
        "    )\n"
        "    \n"
        "    model = Pipeline([\n"
        "        ('selector', selector),\n"
        "        ('rf', rf)\n"
        "    ])\n"
        "    \n"
        "    model.fit(X_tr, y_tr)\n"
        "    y_pr = model.predict_proba(X_te)[:, 1]\n"
        "    \n"
        "    return roc_auc_score(y_te, y_pr)\n\n"
        "p_selector = GenericUnivariateSelect(**{\n"
        "    'score_func': mutual_info_classif, \n"
        "    'mode': 'percentile', \n"
        "    'param': 15\n"
        "})\n\n"
        "k_selector = GenericUnivariateSelect(**{\n"
        "    'score_func': mutual_info_classif, \n"
        "    'mode': 'k_best', \n"
        "    'param': 2\n"
        "})\n\n"
        "tr_index, te_index = next(StratifiedKFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 10, shuffle=True, random_state=37).split(C, d))\n\n"
        "print(get_classification_performance(tr_index, te_index, C, d, p_selector))\n"
        "print(get_classification_performance(tr_index, te_index, C, d, k_selector))\n",
    )
    replace_cell_containing(
        "feature-selection.ipynb",
        "rf = RandomForestRegressor(max_depth=10, random_state=37, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)",
        "from sklearn.feature_selection import f_regression, mutual_info_regression\n"
        "from sklearn.ensemble import RandomForestRegressor\n"
        "from sklearn.metrics import mean_absolute_error\n"
        "from sklearn.model_selection import KFold\n\n"
        "def get_regression_performance(tr_index, te_index, X, y, selector):\n"
        "    X_tr, X_te = X[tr_index], X[te_index]\n"
        "    y_tr, y_te = y[tr_index], y[te_index]\n"
        "    \n"
        "    rf = RandomForestRegressor(\n"
        "        n_estimators=10 if SCIKIT_INTRO_CHECK_MODE else 100,\n"
        "        max_depth=10,\n"
        "        random_state=37,\n"
        "        n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1,\n"
        "    )\n"
        "    \n"
        "    model = Pipeline([\n"
        "        ('selector', selector),\n"
        "        ('rf', rf)\n"
        "    ])\n"
        "    \n"
        "    model.fit(X_tr, y_tr)\n"
        "    y_pr = model.predict(X_te)\n"
        "    \n"
        "    return mean_absolute_error(y_te, y_pr)\n\n"
        "fp_selector = GenericUnivariateSelect(**{\n"
        "    'score_func': f_regression, \n"
        "    'mode': 'percentile', \n"
        "    'param': 15\n"
        "})\n\n"
        "mp_selector = GenericUnivariateSelect(**{\n"
        "    'score_func': mutual_info_regression, \n"
        "    'mode': 'percentile', \n"
        "    'param': 15\n"
        "})\n\n"
        "fk_selector = GenericUnivariateSelect(**{\n"
        "    'score_func': f_regression, \n"
        "    'mode': 'k_best', \n"
        "    'param': 2\n"
        "})\n\n"
        "mk_selector = GenericUnivariateSelect(**{\n"
        "    'score_func': mutual_info_regression, \n"
        "    'mode': 'k_best', \n"
        "    'param': 2\n"
        "})\n\n"
        "tr_index, te_index = next(KFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 10, shuffle=True, random_state=37).split(A, b))\n\n"
        "print(get_regression_performance(tr_index, te_index, A, b, fp_selector))\n"
        "print(get_regression_performance(tr_index, te_index, A, b, fk_selector))\n"
        "print(get_regression_performance(tr_index, te_index, A, b, mp_selector))\n"
        "print(get_regression_performance(tr_index, te_index, A, b, mk_selector))\n",
    )
    replace_cell_containing(
        "feature-selection.ipynb",
        "rf_selector = SelectFromModel(**{\n    'estimator': RandomForestClassifier(max_depth=10, random_state=37, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1),",
        "from sklearn.feature_selection import SelectFromModel\n"
        "from sklearn.linear_model import LogisticRegression\n\n"
        "lr_selector = SelectFromModel(**{\n"
        "    'estimator': LogisticRegression(),\n"
        "    'max_features': 5\n"
        "})\n\n"
        "rf_selector = SelectFromModel(**{\n"
        "    'estimator': RandomForestClassifier(n_estimators=10 if SCIKIT_INTRO_CHECK_MODE else 100, max_depth=10, random_state=37, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1),\n"
        "    'max_features': 5\n"
        "})\n\n"
        "tr_index, te_index = next(StratifiedKFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 10, shuffle=True, random_state=37).split(C, d))\n\n"
        "print(get_classification_performance(tr_index, te_index, C, d, lr_selector))\n"
        "print(get_classification_performance(tr_index, te_index, C, d, rf_selector))\n",
    )
    replace_cell_containing(
        "feature-selection.ipynb",
        "rf_selector = SelectFromModel(**{\n    'estimator': RandomForestRegressor(max_depth=10, random_state=37, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1),",
        "from sklearn.linear_model import LinearRegression\n\n"
        "lr_selector = SelectFromModel(**{\n"
        "    'estimator': LinearRegression(n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1),\n"
        "    'max_features': 5\n"
        "})\n\n"
        "rf_selector = SelectFromModel(**{\n"
        "    'estimator': RandomForestRegressor(n_estimators=10 if SCIKIT_INTRO_CHECK_MODE else 100, max_depth=10, random_state=37, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1),\n"
        "    'max_features': 5\n"
        "})\n\n"
        "tr_index, te_index = next(KFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 10, shuffle=True, random_state=37).split(A, b))\n\n"
        "print(get_regression_performance(tr_index, te_index, A, b, lr_selector))\n"
        "print(get_regression_performance(tr_index, te_index, A, b, rf_selector))\n",
    )
    replace_cell_containing(
        "feature-selection.ipynb",
        "n_features_to_select': 3 if SCIKIT_INTRO_CHECK_MODE else 5,",
        "from sklearn.feature_selection import SequentialFeatureSelector\n\n"
        "lr_selector = SequentialFeatureSelector(**{\n"
        "    'estimator': LogisticRegression(), \n"
        "    'n_features_to_select': 2 if SCIKIT_INTRO_CHECK_MODE else 5, \n"
        "    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1, \n"
        "    'scoring': 'roc_auc'})\n\n"
        "rf_selector = SequentialFeatureSelector(**{\n"
        "    'estimator': RandomForestClassifier(n_estimators=10 if SCIKIT_INTRO_CHECK_MODE else 100, max_depth=10, random_state=37, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1), \n"
        "    'n_features_to_select': 2 if SCIKIT_INTRO_CHECK_MODE else 5, \n"
        "    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1, \n"
        "    'scoring': 'roc_auc'})\n\n"
        "tr_index, te_index = next(StratifiedKFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 10, shuffle=True, random_state=37).split(C, d))\n\n"
        "print(get_classification_performance(tr_index, te_index, C, d, lr_selector))\n"
        "print(get_classification_performance(tr_index, te_index, C, d, rf_selector))\n",
    )
    replace_cell_containing(
        "feature-selection.ipynb",
        "n_features_to_select': 3 if SCIKIT_INTRO_CHECK_MODE else 5, \n    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1, \n    'scoring': 'neg_mean_absolute_error'})",
        "lr_selector = SequentialFeatureSelector(**{\n"
        "    'estimator': LinearRegression(n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1), \n"
        "    'n_features_to_select': 2 if SCIKIT_INTRO_CHECK_MODE else 5, \n"
        "    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1, \n"
        "    'scoring': 'neg_mean_absolute_error'})\n\n"
        "rf_selector = SequentialFeatureSelector(**{\n"
        "    'estimator': RandomForestRegressor(n_estimators=10 if SCIKIT_INTRO_CHECK_MODE else 100, max_depth=10, random_state=37, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1), \n"
        "    'n_features_to_select': 2 if SCIKIT_INTRO_CHECK_MODE else 5, \n"
        "    'n_jobs': 1 if SCIKIT_INTRO_CHECK_MODE else -1, \n"
        "    'scoring': 'neg_mean_absolute_error'})\n\n"
        "tr_index, te_index = next(KFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 10, shuffle=True, random_state=37).split(A, b))\n\n"
        "print(get_regression_performance(tr_index, te_index, A, b, lr_selector))\n"
        "print(get_regression_performance(tr_index, te_index, A, b, rf_selector))\n",
    )
    replace_cell_containing(
        "feature-selection.ipynb",
        "lr_selector = RFECV(LogisticRegression(), step=2 if SCIKIT_INTRO_CHECK_MODE else 1, cv=2 if SCIKIT_INTRO_CHECK_MODE else 5, scoring='roc_auc', n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)",
        "from sklearn.feature_selection import RFECV\n\n"
        "lr_selector = RFECV(LogisticRegression(), step=4 if SCIKIT_INTRO_CHECK_MODE else 1, cv=2 if SCIKIT_INTRO_CHECK_MODE else 5, scoring='roc_auc', n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)\n"
        "rf_selector = RFECV(RandomForestClassifier(n_estimators=10 if SCIKIT_INTRO_CHECK_MODE else 100, max_depth=10, random_state=37, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1), step=4 if SCIKIT_INTRO_CHECK_MODE else 1, cv=2 if SCIKIT_INTRO_CHECK_MODE else 5, scoring='roc_auc', n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)\n\n"
        "tr_index, te_index = next(StratifiedKFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 10, shuffle=True, random_state=37).split(C, d))\n\n"
        "print(get_classification_performance(tr_index, te_index, C, d, lr_selector))\n"
        "print(get_classification_performance(tr_index, te_index, C, d, rf_selector))\n",
    )
    replace_cell_containing(
        "feature-selection.ipynb",
        "lr_selector = RFECV(LinearRegression(n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1), step=2 if SCIKIT_INTRO_CHECK_MODE else 1, cv=2 if SCIKIT_INTRO_CHECK_MODE else 5, scoring='neg_mean_absolute_error', n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)",
        "lr_selector = RFECV(LinearRegression(n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1), step=4 if SCIKIT_INTRO_CHECK_MODE else 1, cv=2 if SCIKIT_INTRO_CHECK_MODE else 5, scoring='neg_mean_absolute_error', n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)\n"
        "rf_selector = RFECV(RandomForestRegressor(n_estimators=10 if SCIKIT_INTRO_CHECK_MODE else 100, max_depth=10, random_state=37, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1), step=4 if SCIKIT_INTRO_CHECK_MODE else 1, cv=2 if SCIKIT_INTRO_CHECK_MODE else 5, scoring='neg_mean_absolute_error', n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)\n\n"
        "tr_index, te_index = next(KFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 10, shuffle=True, random_state=37).split(A, b))\n\n"
        "print(get_regression_performance(tr_index, te_index, A, b, lr_selector))\n"
        "print(get_regression_performance(tr_index, te_index, A, b, rf_selector))\n",
    )
    replace_cell_containing(
        "feature-selection.ipynb",
        "selector = RFECV(RandomForestClassifier(n_estimators=10 if SCIKIT_INTRO_CHECK_MODE else 20, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1, random_state=37), ",
        "from sklearn.feature_extraction.text import CountVectorizer\n"
        "from sklearn.pipeline import Pipeline\n"
        "from sklearn.metrics import roc_auc_score\n"
        "from sklearn.linear_model import LogisticRegression\n"
        "from sklearn.ensemble import RandomForestClassifier\n\n"
        "text = [\n"
        "    'Data Science from Scratch: First Principles with Python',\n"
        "    'Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking',\n"
        "    'Practical Statistics for Data Scientists',\n"
        "    'Build a Career in Data Science',\n"
        "    'Python Data Science Handbook',\n"
        "    'Storytelling with Data: A Data Visualization Guide for Business Professionals',\n"
        "    'R for Data Science: Import, Tidy, Transform, Visualize, and Model Data',\n"
        "    'Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control',\n"
        "    'A Hands-On Introduction to Data Science',\n"
        "    'Intro to Python for Computer Science and Data Science: Learning to Program with AI, Big Data and The Cloud',\n"
        "    'How Finance Works: The HBR Guide to Thinking Smart About the Numbers',\n"
        "    'The Intelligent Investor: The Definitive Book on Value Investing. A Book of Practical Counsel',\n"
        "    'Introduction to Finance: Markets, Investments, and Financial Management',\n"
        "    'Python for Finance: Mastering Data-Driven Finance',\n"
        "    'The Infographic Guide to Personal Finance: A Visual Reference for Everything You Need to Know',\n"
        "    'Personal Finance For Dummies',\n"
        "    'Corporate Finance For Dummies',\n"
        "    'Lords of Finance: The Bankers Who Broke the World',\n"
        "    'Real Estate Finance & Investments',\n"
        "    'Real Estate Finance and Investments Risks and Opportunities'\n"
        "]\n\n"
        "clazz = [1 for _ in range(10)] + [0 for _ in range(10)]\n\n"
        "with open('stop-words.txt', 'r') as f:\n"
        "    stop_words = set([word.strip() for word in f if len(word.strip()) > 0])\n\n"
        "vectorizer = CountVectorizer(binary=True, stop_words=sorted(stop_words), \n"
        "                             ngram_range=(1, 2))\n"
        "selector = RFECV(RandomForestClassifier(n_estimators=5 if SCIKIT_INTRO_CHECK_MODE else 20, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1, random_state=37), \n"
        "                 step=4 if SCIKIT_INTRO_CHECK_MODE else 1, cv=2 if SCIKIT_INTRO_CHECK_MODE else 5, scoring='roc_auc', n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)\n"
        "regressor = LogisticRegression(penalty='l2', solver='liblinear', \n"
        "                               fit_intercept=False, C=0.01, random_state=37)\n"
        "pipeline = Pipeline([\n"
        "    ('vectorizer', vectorizer),\n"
        "    ('selector', selector),\n"
        "    ('regressor', regressor)\n"
        "])\n\n"
        "pipeline.fit(text, clazz)\n"
        "y_pred = pipeline.predict(text)\n"
        "roc_auc_score(clazz, y_pred)\n",
    )
    replace_cell_containing(
        "feature-selection.ipynb",
        "for fold, (tr, te) in enumerate(StratifiedKFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 5, shuffle=True, random_state=37).split(text, clazz)):",
        "def get_model():\n"
        "    vectorizer = CountVectorizer(binary=True, stop_words=sorted(stop_words), \n"
        "                             ngram_range=(1, 2))\n"
        "    selector = RFECV(RandomForestClassifier(n_estimators=5 if SCIKIT_INTRO_CHECK_MODE else 20, n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1, random_state=37), \n"
        "                     step=4 if SCIKIT_INTRO_CHECK_MODE else 1, cv=2 if SCIKIT_INTRO_CHECK_MODE else 5, scoring='roc_auc', n_jobs=1 if SCIKIT_INTRO_CHECK_MODE else -1)\n"
        "    regressor = LogisticRegression(penalty='l2', solver='liblinear', \n"
        "                                   fit_intercept=False, C=0.01, random_state=37)\n"
        "    pipeline = Pipeline([\n"
        "        ('vectorizer', vectorizer),\n"
        "        ('selector', selector),\n"
        "        ('regressor', regressor)\n"
        "    ])\n"
        "    \n"
        "    return pipeline\n\n"
        "results = []\n\n"
        "folds = list(StratifiedKFold(n_splits=2 if SCIKIT_INTRO_CHECK_MODE else 5, shuffle=True, random_state=37).split(text, clazz))\n"
        "if SCIKIT_INTRO_CHECK_MODE:\n"
        "    folds = folds[:1]\n\n"
        "for fold, (tr, te) in enumerate(folds):\n"
        "    X = np.array(text)\n"
        "    y = np.array(clazz)\n"
        "    \n"
        "    X_tr, X_te = X[tr], X[te]\n"
        "    y_tr, y_te = y[tr], y[te]\n"
        "    \n"
        "    model = get_model()\n"
        "    model.fit(X_tr, y_tr)\n"
        "    y_pred = model.predict_proba(X_te)[:, 1]\n"
        "    \n"
        "    score = roc_auc_score(y_te, y_pred)\n"
        "    \n"
        "    vectorizer = model['vectorizer']\n"
        "    selector = model['selector']\n"
        "    \n"
        "    features = vectorizer.get_feature_names_out()\n"
        "    rankings = selector.ranking_\n"
        "    \n"
        "    features_selected = sorted([(n, r) for n, r in zip(features, rankings)], \n"
        "                               key=lambda tup: tup[1])[0:selector.n_features_]\n"
        "    features_selected = [tup[0] for tup in features_selected]\n"
        "    \n"
        "    regressor = model['regressor']\n"
        "    coefs = regressor.coef_[0]\n"
        "    \n"
        "    features = {}\n"
        "    for i, (f, c) in enumerate(zip(features_selected, coefs)):\n"
        "        fname = f'x{i}'\n"
        "        cname = f'c{i}'\n"
        "        features[fname] = f\n"
        "        features[cname] = c\n"
        "        \n"
        "    result = {**{'fold': fold, 'auc': score}, **features}\n"
        "    results.append(result)\n",
    )
    replace_cell_containing(
        "plot-graph.ipynb",
        "import networkx as nx",
        "%matplotlib inline\n"
        "import matplotlib.pyplot as plt\n"
        "import numpy as np\n"
        "import pandas as pd\n"
        "import seaborn as sns\n"
        "import networkx as nx\n"
        "import warnings\n"
        "from _runtime import graph_layout\n\n"
        "plt.style.use('ggplot')\n"
        "np.random.seed(37)\n"
        "warnings.filterwarnings('ignore')\n",
    )
    replace_cell_containing(
        "plot-graph.ipynb",
        "nx.nx_agraph.graphviz_layout(g, prog='dot'",
        "g = nx.DiGraph()\n\n"
        "g.add_node('a')\n"
        "g.add_node('b')\n"
        "g.add_node('c')\n"
        "g.add_node('d')\n\n"
        "g.add_edge('a', 'c', weight=1)\n"
        "g.add_edge('b', 'c', weight=2)\n"
        "g.add_edge('c', 'd', weight=3)\n\n"
        "fig, ax = plt.subplots(figsize=(5, 5))\n\n"
        "pos = graph_layout(g, layout='dot')\n\n"
        "params = {\n"
        "    'node_color': 'r',\n"
        "    'node_size': 350,\n"
        "    'node_shape': 's',\n"
        "    'alpha': 0.5,\n"
        "    'pos': pos,\n"
        "    'ax': ax\n"
        "}\n"
        "_ = nx.drawing.nx_pylab.draw_networkx_nodes(g, **params)\n\n"
        "params = {\n"
        "    'font_size': 15,\n"
        "    'font_color': 'k',\n"
        "    'font_family': 'monospace',\n"
        "    'pos': pos,\n"
        "    'ax': ax\n"
        "}\n"
        "_ = nx.drawing.nx_pylab.draw_networkx_labels(g, **params)\n\n"
        "params = {\n"
        "    'width': 1.5,\n"
        "    'alpha': 0.5,\n"
        "    'edge_color': 'b',\n"
        "    'arrowsize': 20,\n"
        "    'pos': pos,\n"
        "    'ax': ax\n"
        "}\n"
        "_ = nx.drawing.nx_pylab.draw_networkx_edges(g, **params)\n\n"
        "params = {\n"
        "    'edge_labels': {e: g.edges[e]['weight'] for e in g.edges()},\n"
        "    'font_family': 'monospace',\n"
        "    'pos': pos,\n"
        "    'ax': ax\n"
        "}\n"
        "_ = nx.drawing.nx_pylab.draw_networkx_edge_labels(g, **params)\n",
    )
    replace_cell_containing(
        "plot-graph.ipynb",
        "positions = [nx.nx_agraph.graphviz_layout(g, prog='dot'",
        "from itertools import cycle\n\n"
        "g = nx.DiGraph()\n\n"
        "g.add_edge('a', 'c')\n"
        "g.add_edge('b', 'c')\n"
        "g.add_edge('c', 'd')\n"
        "g.add_edge('d', 'e')\n\n"
        "add_edges(g, 'a', 5)\n"
        "add_edges(g, 'b', 5)\n"
        "add_edges(g, 'c', 5)\n"
        "add_edges(g, 'd', 10)\n\n"
        "layouts = ['circo', 'dot', 'fdp', 'neato', 'osage', 'patchwork', 'sfdp', 'twopi']\n"
        "positions = [graph_layout(g, layout=layout) for layout in layouts]\n"
        "node_shapes = cycle('so^v><dp')\n"
        "node_colors = cycle('bgrcmy')\n"
        "edge_colors = cycle('ymcrgb')\n"
        "font_colors = 'wkkkkkkk'\n\n"
        "fig, axes = plt.subplots(len(layouts), 1, figsize=(15, 50))\n"
        "axes = np.ravel(axes)\n\n"
        "for layout, pos, node_shape, node_color, edge_color, font_color, ax in zip(layouts, positions, node_shapes, node_colors, edge_colors, font_colors, axes):\n"
        "    params = {\n"
        "        'node_color': node_color,\n"
        "        'node_size': 450,\n"
        "        'node_shape': node_shape,\n"
        "        'alpha': 0.5,\n"
        "        'pos': pos,\n"
        "        'ax': ax\n"
        "    }\n"
        "    _ = nx.drawing.nx_pylab.draw_networkx_nodes(g, **params)\n\n"
        "    params = {\n"
        "        'font_size': 15,\n"
        "        'font_color': font_color,\n"
        "        'font_family': 'monospace',\n"
        "        'pos': pos,\n"
        "        'ax': ax\n"
        "    }\n"
        "    _ = nx.drawing.nx_pylab.draw_networkx_labels(g, **params)\n\n"
        "    params = {\n"
        "        'width': 1.5,\n"
        "        'alpha': 0.5,\n"
        "        'edge_color': edge_color,\n"
        "        'arrowsize': 20,\n"
        "        'pos': pos,\n"
        "        'ax': ax\n"
        "    }\n"
        "    _ = nx.drawing.nx_pylab.draw_networkx_edges(g, **params)\n"
        "    \n"
        "    _ = ax.set_title(f'layout={layout}, node_shape={node_shape}')\n"
        "    _ = ax.axes.get_xaxis().set_visible(False)\n"
        "    _ = ax.axes.get_yaxis().set_visible(False)\n",
    )


if __name__ == "__main__":
    main()
