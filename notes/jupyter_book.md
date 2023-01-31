# jupyter bookでできること


# MyST (or Markedly Structured Text)
[MyST Markdown overview](https://jupyterbook.org/en/stable/content/myst.html)


## Blockを記述する


### noteを記述する

記述方法
```{code-block}
    ```{note}
    noteを書く場合はこのように記述する
    ```
```

記述結果
```{note}
noteを書く場合はこのように記述する
```


- codeを記述する

記述方法

```{code-block} python
    ```{code-block} python
        import numpy as np
        print(np.arange(10))
    ```
```

記述結果
```{code-block} python
    import numpy as np
    print(np.arange(10))
```

```python


```
