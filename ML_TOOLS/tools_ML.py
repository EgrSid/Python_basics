import pandas as pd
import numpy as np
import scipy
import imblearn.under_sampling as unders
import imblearn.over_sampling as overs
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
from sklearn.linear_model import Lasso  # L1-регуляризатор
from matplotlib import pyplot as plt


def check_types(values: list, target_type: tuple | type) -> bool:
    """Checking the types of the input data"""
    return all(isinstance(value, target_type) for value in values)


def detect_outliers(df: pd.DataFrame, method: str = '3sigma', **kwargs) -> pd.DataFrame:
    """
        Finds the outliers in the df according to the method and returns them.

        Parameters:
        df (pd.DataFrame): The input data.
        method (str): The method to detect outliers. Defaults to '3sigma'. Valid methods: '3sigma', 'Tukey', 'Shovene', 'Grabbs'.
        **kwargs: Additional keyword arguments to customize the function.

        Returns:
        pd.DataFrame: A DataFrame containing the outliers.
    """

    valid_methods = ('3sigma', 'Tukey', 'Shovene', 'Grabbs')
    assert isinstance(df, pd.DataFrame), f'Incorrect dtype. df: {type(df)} instead of {pd.DataFrame}'
    assert method.capitalize() in valid_methods, f"This method doesn't support. Valid methods: {valid_methods}"

    if method == 'Grabbs':
        # this method only shows whether the outliers are in the feature
        threshold = kwargs['threshold'] if 'threshold' in kwargs.keys() else 0.05
        mean_val = df.mean()
        std_val = df.std()
        n = df.count()
        t_value = (n - 1) * (abs(df.max() - mean_val) / std_val)
        critical_value = scipy.stats.t.sf(1 - threshold / (2 * n), n - 2)
        return t_value > critical_value

    res_df = pd.DataFrame()
    for feature in df:
        if not isinstance(df[feature][0], (float, int)): continue
        match method:
            case '3sigma':
                mu, sigma = df[feature].mean(), df[feature].std()
                d = df[abs(df[feature]) > mu + 3 * sigma]
                res_df = pd.concat((res_df, d)).drop_duplicates(keep=False)
            case 'Tukey':
                q1 = df[feature].quantile(0.25)
                q3 = df[feature].quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - (1.5 * iqr)
                upper_bound = q3 + (1.5 * iqr)
                d = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]
                res_df = pd.concat((res_df, d)).drop_duplicates(keep=False)
            case 'Shovene':
                d = df[scipy.special.erfc(abs(df[feature] - df[feature].mean()) / df[feature].std()) < 1 / (
                        2 * len(df[feature]))]
                res_df = pd.concat((res_df, d)).drop_duplicates(keep=False)
    return res_df.sort_index()


def fillna(df: pd.DataFrame, method: str = 'mean') -> pd.DataFrame:
    """
        Filling Nan values in df according to the method.

        Parameters:
        df (pd.DataFrame): The input data.
        method (str): The method to fill Nan values. Defaults to 'mean'. Valid methods: 'mean', 'median', 'mode', 'hmean', 'indicator', 'prev_num', 'interpolation'.

        Returns:
        pd.DataFrame: A DataFrame with filled Nan values.
    """

    valid_methods = ('mean', 'median', 'mode', 'hmean', 'indicator', 'prev_num', 'interpolation')
    assert isinstance(df, pd.DataFrame), f'Incorrect dtype. df: {type(df)} instead of {pd.DataFrame}'
    assert method.lower() in valid_methods, f"This method doesn't support. Valid methods: {valid_methods}"

    match method:
        case 'mean':
            df = df.fillna(df.mean()).round(2)
        case 'median':
            df = df.fillna(df.median()).round(2)
        case 'mode':
            df = df.fillna(df.mode().mean()).round(2)
        case 'hmean':
            df = df.fillna(pd.Series([np.round(scipy.stats.hmean(col[~np.isnan(col)]), 2) for col in df.values.T],
                                     index=df.columns).round(2))
        case 'indicator':
            temple_df = pd.DataFrame(df.isna().astype(int).to_numpy(),
                                     columns=df.isna().columns + '_indicator')
            df = pd.concat((df, temple_df), axis=1)
            df = df.loc[:, (df != 0).any(axis=0)]
        case 'prev_num':
            df = df.fillna(df.ffill()).fillna(df.bfill()).round(2)
        case 'interpolation':
            df = df.interpolate(method='linear', limit_direction='forward')
            df = fillna(df)
    return df


def corr_features(df: pd.DataFrame, threshold: int | float = 0.85, **kwargs) -> dict:
    """
        Finds the correlated features more than the threshold and returns like dict.

        Parameters:
        df (pd.DataFrame): The input data.
        threshold (int | float): The correlation threshold. Defaults to 0.85.
        **kwargs: Additional keyword arguments to customize the function.

        Returns:
        dict: A dictionary containing the correlated features.
    """

    assert isinstance(df, pd.DataFrame), f'Incorrect dtype. df: {type(df)} instead of {pd.DataFrame}'
    assert isinstance(threshold,
                      (int, float)), f'Incorrect dtype. threshold: {type(threshold)} instead of any {(int, float)}'
    assert 0 < threshold <= 1, 'Incorrect threshold value. It must be (0, 1]'

    method = kwargs.get('method', 'pearson').lower()
    corr_matrix = df.corr(method=method).abs()
    upper_tri = np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    corr_features = corr_matrix.where(upper_tri).unstack()

    return corr_features[corr_features > threshold].to_dict()


def balance_df(df: pd.DataFrame, target: str | int | float, threshold: int | float) -> None:
    """
        Checks the balance of the attribute distribution for the target variable.

        Parameters:
        df (pd.DataFrame): The input data.
        target (str | int | float): The target variable.
        threshold (int | float): The balance threshold.

        Returns:
        None
    """

    assert isinstance(df, pd.DataFrame), f'Incorrect dtype. df: {type(df)} instead of {pd.DataFrame}'
    assert target in df.columns, f'target must be in columns of df: {list(df.columns)}'
    assert isinstance(threshold,
                      (int, float)), f'Incorrect dtype. threshold: {type(threshold)} instead of any {(int, float)}'
    assert threshold >= 0, 'Incorrect threshold value. It must be >= 0'

    _, count_unique = np.unique(df[target], return_counts=True)
    balance = max(count_unique) / min(count_unique)
    print(f'Disbalanced: {balance}') if balance > threshold else print(f'Balanced: {balance}')


def check_norm_distribution(df, target) -> dict:
    """
        Checks the normality of the attribute distribution for the target variable.

        Parameters:
        df (pd.DataFrame): The input data.
        target (str | int | float): The target variable.

        Returns:
        dict: A dictionary containing the normality metrics.
    """

    assert isinstance(df, pd.DataFrame), f'Incorrect dtype. df: {type(df)} instead of {pd.DataFrame}'
    assert target in df.columns, f'target must be in columns of df: {list(df.columns)}'

    asymmetry = pd.DataFrame(df[target].to_numpy()).skew()[0].round(3)
    kurt = pd.DataFrame(df[target].to_numpy()).kurtosis()[0].round(3)
    print(
        f'ass: {asymmetry}, kurt: {kurt} -> '
        f'Distribution is {"normal" if abs(asymmetry) <= 2 and abs(kurt) <= 7 else "not normal"}')
    return {'asymmetry': asymmetry, 'kurt': kurt, 'normal': abs(asymmetry) <= 2 and abs(kurt) <= 7}


def under_sampling(df: pd.DataFrame, target: str | int | float, method='RandomUnderSampler', **kwargs) -> pd.DataFrame:
    """Under sampling dataset according to method

    Supported methods:
    'RandomUnderSampler',
    'EEditedNearestNeighbours',
    'RepeatedEditedNearestNeighbours',
    'AllKNN'
    'CondensedNearestNeighbour',
    'OneSidedSelection',
    'NeighbourhoodCleaningRule',
    'ClusterCentroids',
    'TomekLinks',
    'NearMiss',
    'InstanceHardnessThreshold'

    Parameters:
    df (pd.DataFrame): Input dataset
    target (str | int | float): Name of the target column
    method (str): Under-sampling method (default='random')
    **kwargs: Additional parameters for the under-sampling method

    Returns:
    pd.DataFrame: Under-sampled dataset
    """
    # checking common input parameters
    valid_methods = ('RandomUnderSampler', 'EditedNearestNeighbours', 'RepeatedEditedNearestNeighbours', 'AllKNN',
                     'CondensedNearestNeighbour', 'OneSidedSelection', 'NeighbourhoodCleaningRule', 'ClusterCentroids',
                     'TomekLinks', 'NearMiss', 'InstanceHardnessThreshold')
    assert isinstance(df, pd.DataFrame), f'Incorrect dtype. df: {type(df)} instead of {pd.DataFrame}'
    assert method in valid_methods, f"This method doesn't support. Valid methods: {valid_methods}"
    assert target in df.columns, f'target must be in columns of df: {list(df.columns)}'

    # listing all possible parameters for sample processing
    random_state = kwargs.get('random_state', None)
    sampling_strategy = kwargs.get('sampling_strategy', 'auto')
    n_neighbors = kwargs.get('n_neighbors', 3)
    kind_sel = kwargs.get('kind_sel', 'all')
    n_jobs = kwargs.get('n_jobs', None)
    max_iter = kwargs.get('max_iter', 100)
    allow_minority = kwargs.get('allow_minority', False)
    n_seeds_S = kwargs.get('n_seeds_S', 1)
    edited_nearest_neighbours = kwargs.get('edited_nearest_neighbours', None)
    threshold_cleaning = kwargs.get('threshold_cleaning', 0.5)
    estimator = kwargs.get('estimator', None)
    voting = kwargs.get('voting', 'auto')
    version = kwargs.get('version', 1)
    n_neighbors_ver3 = kwargs.get('n_neighbors_ver3', 3)
    cv = kwargs.get('cv', 5)

    # main program
    match method:
        case 'RandomUnderSampler':
            sampler = unders.RandomUnderSampler(random_state=random_state,
                                                sampling_strategy=sampling_strategy)
        case 'EditedNearestNeighbours':
            sampler = unders.EditedNearestNeighbours(sampling_strategy=sampling_strategy,
                                                     n_neighbors=n_neighbors,
                                                     kind_sel=kind_sel,
                                                     n_jobs=n_jobs)
        case 'RepeatedEditedNearestNeighbours':
            sampler = unders.RepeatedEditedNearestNeighbours(sampling_strategy=sampling_strategy,
                                                             n_neighbors=n_neighbors,
                                                             max_iter=max_iter,
                                                             kind_sel=kind_sel,
                                                             n_jobs=n_jobs)
        case 'AllKNN':
            sampler = unders.AllKNN(sampling_strategy=sampling_strategy,
                                    n_neighbors=n_neighbors,
                                    allow_minority=allow_minority,
                                    kind_sel=kind_sel,
                                    n_jobs=n_jobs)
        case 'CondensedNearestNeighbour':
            sampler = unders.CondensedNearestNeighbour(sampling_strategy=sampling_strategy,
                                                       random_state=random_state,
                                                       n_neighbors=n_neighbors,
                                                       n_jobs=n_jobs,
                                                       n_seeds_S=n_seeds_S)
        case 'OneSidedSelection':
            sampler = unders.OneSidedSelection(sampling_strategy=sampling_strategy,
                                               random_state=random_state,
                                               n_neighbors=n_neighbors,
                                               n_jobs=n_jobs,
                                               n_seeds_S=n_seeds_S)
        case 'NeighbourhoodCleaningRule':
            sampler = unders.NeighbourhoodCleaningRule(sampling_strategy=sampling_strategy,
                                                       edited_nearest_neighbours=edited_nearest_neighbours,
                                                       n_neighbors=n_neighbors,
                                                       n_jobs=n_jobs,
                                                       kind_sel=kind_sel,
                                                       threshold_cleaning=threshold_cleaning)
        case 'ClusterCentroids':
            sampler = unders.ClusterCentroids(sampling_strategy=sampling_strategy,
                                              random_state=random_state,
                                              estimator=estimator,
                                              voting=voting)
        case 'TomekLinks':
            sampler = unders.TomekLinks(sampling_strategy=sampling_strategy,
                                        n_jobs=n_jobs)
        case 'NearMiss':
            sampler = unders.NearMiss(sampling_strategy=sampling_strategy,
                                      version=version,
                                      n_neighbors=n_neighbors,
                                      n_neighbors_ver3=n_neighbors_ver3,
                                      n_jobs=n_jobs)
        case 'InstanceHardnessThreshold':
            sampler = unders.InstanceHardnessThreshold(estimator=estimator,
                                                       sampling_strategy=sampling_strategy,
                                                       random_state=random_state,
                                                       cv=cv,
                                                       n_jobs=n_jobs)

    changed_data, changed_labels = sampler.fit_resample(df.to_numpy(), df[target].to_numpy())
    return pd.DataFrame(changed_data, changed_labels, columns=df.columns)


def over_sampling(df: pd.DataFrame, target: str | int | float, method='RandomOverSampler', **kwargs) -> pd.DataFrame:
    """
    Over sampling dataset according to method

    Supported methods:
    'RandomOverSampler',
    'SMOTE',
    'ADASYN',
    'BorderlineSMOTE',
    'SVMSMOTE',
    'KMeansSMOTE',
    'SMOTENC',
    'SMOTEN'

    Parameters:
    df (pd.DataFrame): Input dataset
    target (str | int | float): Name of the target column
    method (str): Over-sampling method (default='RandomOverSampler')
    **kwargs: Additional parameters for the over-sampling method

    Returns:
    pd.DataFrame: Over-sampled dataset
    """
    # checking common input parameters
    valid_methods = (
        'RandomOverSampler', 'SMOTE', 'ADASYN', 'BorderlineSMOTE', 'SVMSMOTE', 'KMeansSMOTE', 'SMOTENC', 'SMOTEN')
    assert isinstance(df, pd.DataFrame), f'Incorrect dtype. df: {type(df)} instead of {pd.DataFrame}'
    assert method in valid_methods, f"This method doesn't support. Valid methods: {valid_methods}"
    assert target in df.columns, f'target must be in columns of df: {list(df.columns)}'

    # listing all possible parameters for sample processing
    default_k_neighbors = 2 if method == 'KMeansSMOTE' else 5  # it's necessary because
    # there are several parameters with the same names and different default values (KMeansSMOTE=2, others=5)
    random_state = kwargs.get('random_state', None)
    sampling_strategy = kwargs.get('sampling_strategy', 'auto')
    density_exponent = kwargs.get('density_exponent', 'auto')
    cluster_balance_threshold = kwargs.get('cluster_balance_threshold', 'auto')
    shrinkage = kwargs.get('shrinkage', None)
    k_neighbors = kwargs.get('k_neighbors', default_k_neighbors)
    n_neighbors = kwargs.get('n_neighbors', 5)
    m_neighbors = kwargs.get('m_neighbors', 10)
    n_jobs = kwargs.get('n_jobs', None)
    kmeans_estimator = kwargs.get('kmeans_estimator', None)
    svm_estimator = kwargs.get('svm_estimator', None)
    out_step = kwargs.get('out_step', 0.5)
    kind = kwargs.get('kind', 'borderline-1')
    categorical_features = kwargs.get('categorical_features', None)
    categorical_encoder = kwargs.get('categorical_encoder', None)

    # main program
    match method:
        case 'RandomOverSampler':
            sampler = overs.RandomOverSampler(random_state=random_state,
                                              sampling_strategy=sampling_strategy,
                                              shrinkage=shrinkage)
        case 'SMOTE':
            sampler = overs.SMOTE(random_state=random_state,
                                  sampling_strategy=sampling_strategy,
                                  k_neighbors=k_neighbors,
                                  n_jobs=n_jobs)
        case 'ADASYN':
            sampler = overs.ADASYN(random_state=random_state,
                                   sampling_strategy=sampling_strategy,
                                   n_neighbors=n_neighbors,
                                   n_jobs=n_jobs)
        case 'BorderlineSMOTE':
            sampler = overs.BorderlineSMOTE(random_state=random_state,
                                            sampling_strategy=sampling_strategy,
                                            k_neighbors=k_neighbors,
                                            m_neighbors=m_neighbors,
                                            kind=kind,
                                            n_jobs=n_jobs)
        case 'SVMSMOTE':
            sampler = overs.SVMSMOTE(random_state=random_state,
                                     sampling_strategy=sampling_strategy,
                                     k_neighbors=k_neighbors,
                                     m_neighbors=m_neighbors,
                                     svm_estimator=svm_estimator,
                                     out_step=out_step,
                                     n_jobs=n_jobs)
        case 'KMeansSMOTE':
            sampler = overs.KMeansSMOTE(random_state=random_state,
                                        sampling_strategy=sampling_strategy,
                                        k_neighbors=k_neighbors,
                                        n_jobs=n_jobs,
                                        kmeans_estimator=kmeans_estimator,
                                        cluster_balance_threshold=cluster_balance_threshold,
                                        density_exponent=density_exponent)
        case 'SMOTENC':
            sampler = overs.SMOTENC(random_state=random_state,
                                    sampling_strategy=sampling_strategy,
                                    k_neighbors=k_neighbors,
                                    categorical_features=categorical_features,
                                    n_jobs=n_jobs,
                                    categorical_encoder=categorical_encoder)
            changed_data, changed_labels = sampler.fit_resample(df, df[target])
            return pd.DataFrame(changed_data, changed_labels, columns=df.columns)
        case 'SMOTEN':
            sampler = overs.SMOTEN(random_state=random_state,
                                   sampling_strategy=sampling_strategy,
                                   k_neighbors=k_neighbors,
                                   n_jobs=n_jobs,
                                   categorical_encoder=categorical_encoder)

    changed_data, changed_labels = sampler.fit_resample(df.to_numpy(), df[target].to_numpy())
    return pd.DataFrame(changed_data, changed_labels, columns=df.columns)


def l1_models(X, y, l1=tuple(2 ** np.linspace(-10, 10, 100)), scale=False, early_stopping=False, **kwargs):
    """
        Linear models with different L1-regularization parameters.

        Parameters:
        X (list, tuple, np.array, pd.DataFrame): The input data.
        y (list, tuple, np.array, pd.Series, pd.DataFrame): The target data.
        l1 (list, tuple, np.array): The L1 regularization strengths. Defaults to a tuple of 100 values ranging from 2^(-10) to 2^10.
        scale (bool): A flag to indicate whether to scale the data. Defaults to False.
        early_stopping (bool): A flag to indicate whether to use early stopping. Defaults to False.
        **kwargs: Additional keyword arguments to customize the function.

        Returns:
        list: A list of Lasso models, each fitted with a different L1 regularization strength.
    """

    assert isinstance(X, (list, tuple, type(np.array), pd.DataFrame)), \
        f'Incorrect dtype. X: {type(X)} instead of {(list, tuple, type(np.array), pd.DataFrame)}'
    assert isinstance(y, (list, tuple, type(np.array), pd.Series, pd.DataFrame)), \
        f'Incorrect dtype. y: {type(y)} instead of {(list, tuple, type(np.array), pd.Series, pd.DataFrame)}'
    assert isinstance(l1, (list, tuple, type(np.array)))
    assert isinstance(scale, bool), f'Incorrect dtype. scale: {type(scale)} instead of {bool}'
    assert isinstance(early_stopping,
                      bool), f'Incorrect dtype. early_stopping: {type(early_stopping)} instead of {bool}'

    X = StandardScaler().fit_transform(X) if scale else X

    result = list()
    for alpha in tqdm(l1, desc='Fitting L1-models'):
        model = Lasso(alpha=alpha).fit(X, y)  # L1-regularization
        result.append(model)
        if early_stopping and all(map(lambda c: c == 0, model.coef_)): break  # if all weights are zero, stop
    return result


def l1_importance(X, y, l1=tuple(2 ** np.linspace(-10, 10, 100)), scale=False, early_stopping=False, **kwargs):
    """
        Weights features with different L1-regularization parameters.

        Parameters:
        X (list, tuple, np.array, pd.DataFrame): The input data.
        y (list, tuple, np.array, pd.Series, pd.DataFrame): The target data.
        l1 (list, tuple, np.array): The L1 regularization strengths. Defaults to a tuple of 100 values ranging from 2^(-10) to 2^10.
        scale (bool): A flag to indicate whether to scale the data. Defaults to False.
        early_stopping (bool): A flag to indicate whether to use early stopping. Defaults to False.
        **kwargs: Additional keyword arguments to customize the function.

        Returns:
        pd.DataFrame: A DataFrame containing the feature weights for each L1 regularization strength.
    """

    assert isinstance(X, (list, tuple, type(np.array), pd.DataFrame)), \
        f'Incorrect dtype. X: {type(X)} instead of {(list, tuple, type(np.array), pd.DataFrame)}'
    assert isinstance(y, (list, tuple, type(np.array), pd.Series, pd.DataFrame)), \
        f'Incorrect dtype. y: {type(y)} instead of {(list, tuple, type(np.array), pd.Series, pd.DataFrame)}'
    assert isinstance(l1, (list, tuple, type(np.array)))
    assert isinstance(scale, bool), f'Incorrect dtype. scale: {type(scale)} instead of {bool}'
    assert isinstance(early_stopping,
                      bool), f'Incorrect dtype. early_stopping: {type(early_stopping)} instead of {bool}'

    l1_models_ = l1_models(X, y, l1=l1, scale=scale, early_stopping=early_stopping)

    df = pd.DataFrame([l1_model.coef_ for l1_model in l1_models_], columns=X.columns)
    return pd.concat([pd.DataFrame({'L1': l1}), df], axis=1)


def l1_importance_plot(x, y, l1=tuple(2 ** np.linspace(-10, 10, 100)), scale=False, early_stopping=False, **kwargs):
    """
        Plot weights features with different L1-regularization parameters.

        Parameters:
        x (list, tuple, np.array, pd.DataFrame): The input data.
        y (list, tuple, np.array, pd.Series, pd.DataFrame): The target data.
        l1 (list, tuple, np.array): The L1 regularization strengths. Defaults to a tuple of 100 values ranging from 2^(-10) to 2^10.
        scale (bool): A flag to indicate whether to scale the data. Defaults to False.
        early_stopping (bool): A flag to indicate whether to use early stopping. Defaults to False.
        **kwargs: Additional keyword arguments to customize the plot, such as figsize and grid.

        Returns:
        None
    """

    assert isinstance(x, (list, tuple, type(np.array), pd.DataFrame)), \
        f'Incorrect dtype. X: {type(x)} instead of {(list, tuple, type(np.array), pd.DataFrame)}'
    assert isinstance(y, (list, tuple, type(np.array), pd.Series, pd.DataFrame)), \
        f'Incorrect dtype. y: {type(y)} instead of {(list, tuple, type(np.array), pd.Series, pd.DataFrame)}'
    assert isinstance(l1, (list, tuple, type(np.array)))
    assert isinstance(scale, bool), f'Incorrect dtype. scale: {type(scale)} instead of {bool}'
    assert isinstance(early_stopping,
                      bool), f'Incorrect dtype. early_stopping: {type(early_stopping)} instead of {bool}'

    df = l1_importance(x, y, l1=l1, scale=scale, early_stopping=early_stopping)
    df.dropna(axis=0, inplace=True)
    x = df.pop('L1')

    plt.figure(figsize=kwargs.get('figsize', (12, 9)))
    plt.grid(kwargs.get('grid', True))
    for column in df.columns:
        plt.plot(x, df[column])
    plt.legend(df.columns, fontsize=12)
    plt.xlabel('L1', fontsize=14)
    plt.ylabel('coef', fontsize=14)
    plt.xlim([0, l1[x.shape[0]]])
    plt.show()


def l1_best_features(x, y, l1_threshold, min_coef, l1=tuple(2 ** np.linspace(-10, 10, 100)), scale=False,
                     early_stopping=False, **kwargs):
    """
        Finds the best features to train the model based on L1 opinion.

        Parameters:
        x (list, tuple, np.array, pd.DataFrame): The input data.
        y (list, tuple, np.array, pd.Series, pd.DataFrame): The target data.
        l1_threshold (float): The threshold value for L1 regularization.
        min_coef (float): The minimum coefficient value for feature selection.
        l1 (list, tuple, np.array): The L1 regularization strengths. Defaults to a tuple of 100 values ranging from 2^(-10) to 2^10.
        scale (bool): A flag to indicate whether to scale the data. Defaults to False.
        early_stopping (bool): A flag to indicate whether to use early stopping. Defaults to False.
        **kwargs: Additional keyword arguments to pass to the l1_importance function.

        Returns:
        pd.Series: A Series containing the selected features with coefficients greater than min_coef at the optimal L1 regularization strength.
    """
    assert isinstance(x, (list, tuple, type(np.array), pd.DataFrame)), \
        f'Incorrect dtype. X: {type(x)} instead of {(list, tuple, type(np.array), pd.DataFrame)}'
    assert isinstance(y, (list, tuple, type(np.array), pd.Series, pd.DataFrame)), \
        f'Incorrect dtype. y: {type(y)} instead of {(list, tuple, type(np.array), pd.Series, pd.DataFrame)}'
    assert isinstance(l1, (list, tuple, type(np.array)))
    assert isinstance(scale, bool), f'Incorrect dtype. scale: {type(scale)} instead of {bool}'
    assert isinstance(early_stopping,
                      bool), f'Incorrect dtype. early_stopping: {type(early_stopping)} instead of {bool}'

    df = l1_importance(x, y, l1=l1, scale=scale, early_stopping=early_stopping)
    l1_place = df['L1'].to_list().index(
        df['L1'][min(range(len(df['L1'])), key=lambda i: abs(df['L1'][i] - l1_threshold))])
    res = df.iloc[l1_place, 1:]
    res = res[abs(res) > min_coef]
    return res
