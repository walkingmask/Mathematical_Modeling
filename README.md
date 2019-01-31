# Scripts for Final Report of Mathmatical Modeling
This repository contains the following items:

- Script to generate data and datasets (ttt.py)
- Script to calculate Bayesian from generated data and datasets, assumed posterior probability (apply_bayes.py)


# Usage
## Generate data and datasets
To generate data and datasets, run ttt.py.

```
python ttt.py
```

If you want to change number of leagus to generate data, please change the argument of make_data at line #151.

```python
make_data(100)
```

And, if you want to change FSTD of player, please change the argument of make_datasets at line #155. You can also control the number of datasets by passing a number as the second argument.

```python
# 0: COR, 1: SID, 2: CEN
make_datasets(2)  # FSTD: CEN, num_datasets: 10
make_datasets(0, 100)  # FSTD: COR, num_datasets: 100
```


## Calculate Bayes
Use apply_bayes.py as follow.

```
python apply_bayes.py
```

You will use data and datasets you created. Change the variables after line #28.

```
if __name__ == '__main__':
    data = [
        # [victory, draw, defeat]
        [0.59, 0.12, 0.27],  # COR
        [0.55, 0.12, 0.32],  # SID
        [0.66, 0.11, 0.21],  # CEN
    ]
    datasets = [
        [5, 1, 4],  # 1st
        [6, 2, 2],  # 2nd
        ...
        [9, 0, 1],
    ]
    p_fstd = [1/3, 1/3, 1/3]  # assumption

    main(datasets, p_fstd, data)
```
