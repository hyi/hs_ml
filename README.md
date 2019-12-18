# HydroShare Resource Topic Analysis and Mapping

[Reference](https://monkeylearn.com/topic-analysis/)

## Usage

### Pull HydroShare data for topic analysis and mapping

- pull only published data

  Example:

```
  python3 pull_data.py published
```

```
  Dumped all published resources to data/hs_data_published.csv. The number of dumped resources:  303
```

```
  python3 pull_data.py public
```

```
  Dumped all non-published public resources to data/hs_data_public.csv. The number of dumped resources: 4196
```

```
  python3 pull_data.py
```

```
  Dumped all public resources to data/hs_data_public.csv. The number of dumped resources: 4206
```