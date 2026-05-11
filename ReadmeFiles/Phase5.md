# Unsupervised Learning in Scikit-learn (Core Concepts)

Unsupervised learning is a type of machine learning where the model learns patterns from unlabeled data. In sklearn, it is mainly used for clustering, dimensionality reduction, anomaly detection, and density estimation.

---

# 1. Clustering

Clustering groups similar data points together without predefined labels.

## K-Means Clustering

Objective:
min sum of squared distances to cluster centroids

Concept:
- Divides data into K clusters
- Assigns each point to nearest centroid

```python
from sklearn.cluster import KMeans

model = KMeans(n_clusters=3)
model.fit(X)
labels = model.labels_
```

---

## DBSCAN

Concept:
- Density-based clustering
- Detects noise/outliers

```python
from sklearn.cluster import DBSCAN

model = DBSCAN(eps=0.5, min_samples=5)
labels = model.fit_predict(X)
```

---

## Hierarchical Clustering

Concept:
- Builds tree of clusters
- Agglomerative approach most common

```python
from sklearn.cluster import AgglomerativeClustering

model = AgglomerativeClustering(n_clusters=3)
labels = model.fit_predict(X)
```

---

# 2. Dimensionality Reduction

## PCA

Concept:
- Reduces features while keeping variance

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
```

---

## t-SNE

Concept:
- Visualization of high-dimensional data

```python
from sklearn.manifold import TSNE

tsne = TSNE(n_components=2)
X_embedded = tsne.fit_transform(X)
```

---

# 3. Anomaly Detection

## Isolation Forest

Concept:
- Detects anomalies by isolation

```python
from sklearn.ensemble import IsolationForest

model = IsolationForest(contamination=0.1)
model.fit(X)
pred = model.predict(X)
```

---

## One-Class SVM

```python
from sklearn.svm import OneClassSVM

model = OneClassSVM(kernel='rbf')
model.fit(X)
```

---

# 4. Density Estimation

## Gaussian Mixture Model

```python
from sklearn.mixture import GaussianMixture

model = GaussianMixture(n_components=3)
model.fit(X)
labels = model.predict(X)
```

---

# 5. Key Ideas

- No labels required
- Finds hidden structure
- Used for clustering, reduction, anomaly detection

---

# 6. Summary

- KMeans → clustering
- DBSCAN → density clustering
- PCA → dimensionality reduction
- t-SNE → visualization
- Isolation Forest → anomaly detection
- GMM → probabilistic clustering
