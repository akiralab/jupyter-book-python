# markdownをカスタマイズする


# jupytextを使ってjupyter lab上でプレビュー表示できるようにする


[jupytext](https://jupytext.readthedocs.io/en/latest/)にjupytextを有効にするための方法が記載されている.
jupytextを有効にすると、以下のようにmarkdown編集結果がliveで確認できる.

```{image} ../src/jupytext-preview.gif
:alt: fishy
:class: bg-primary
:width: 500px
:align: center
```

## jupytext設定方法

1. jupytextをpip installする

```{code-block} bash
# bash
pip install jupytext
```

2. jupyterlabのsetting -> DocumentManagerのjsonに以下を追加する

```{code-block} json
{
  "defaultViewers": {
    "markdown": "Jupytext Notebook",
    "myst": "Jupytext Notebook",
    "r-markdown": "Jupytext Notebook",
    "quarto": "Jupytext Notebook",
    "julia": "Jupytext Notebook",
    "python": "Jupytext Notebook",
    "r": "Jupytext Notebook"
  }
}
```

3. jupyter labを再起動する

4. mdファイルをを「Jupytext Notebookで開く」を選択する

```{image} ../src/jupytext-notebook-select.png
:alt: 
:class: bg-primary
:width: 500px
:align: center
```

### 参考
- [MyST Markdown overview](https://jupyterbook.org/en/stable/content/myst.html)
- [jupytext](https://jupytext.readthedocs.io/en/latest/)




## Blockを記述する
### admonition (意：勧告)を記述する

記述方法
````
```{admonition} admonitionのタイトル
admonitionを書く場合はこのように記述する
```
````

記述結果

```{admonition} admonitionのタイトル
admonitionを書く場合はこのように記述する
```


### noteを記述する

記述方法
````
```{note}noteを書く場合はこのように記述する
```
````

記述結果
```{note}noteを書く場合はこのように記述する
```


### warningを記述する

記述方法
````
```{warning}warningを書く場合はこのように記述する
```
````

記述結果
```{warning}warningを書く場合はこのように記述する
```



### codeを記述する

記述方法

````
```{code-block} python
    import numpy as np
    print(np.arange(10))
```
````

記述結果
```{code-block} python
    import numpy as np
    print(np.arange(10))
```

<!-- #region -->
> {sub-ref}`today` | {sub-ref}`wordcount-words` words | {sub-ref}`wordcount-minutes` min read


```{image} ../src/jupytext-preview.gif
:alt: fishy
:class: bg-primary
:width: 500px
:align: center
```

<!-- #endregion -->








