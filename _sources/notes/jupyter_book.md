---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


# MySTを用いてmarkdownを記述する方法


## 事前準備：jupytextを使ってjupyter lab上でプレビュー表示できるようにする


[jupytext](https://jupytext.readthedocs.io/en/latest/)にjupytextを有効にするための方法が記載されている.
jupytextを有効にすると、以下のようにmarkdown編集結果がliveで確認できる.

```{image} ../src/jupytext-preview.gif
:alt: fishy
:class: bg-primary
:width: 500px
:align: center
```

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

**参考**
- [MyST Markdown overview](https://jupyterbook.org/en/stable/content/myst.html)
- [jupytext](https://jupytext.readthedocs.io/en/latest/)
- <https://jupyterbook.org/en/stable/reference/cheatsheet.html>



## 基本文法


### Headerを指定する

このように記述すると、Headerを記述できる
```
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6
```



### 引用分を記述する 

記述方法
```
> 引用文
```

実行結果

> 引用文


### 分離線を記述する

記述方法
```
---
```

実行結果

---


### コメントを記述する 

記述方法
```
この行に記載された文章はpreviewでは表示される
% この行に記載された文章はpreviewでは表示されない
```

実行結果

この行に記載された文章はpreviewでは表示される
% この行に記載された文章はpreviewでは表示されない

<!-- #region -->
### HTML要素を記述する
```
<p>これはHTMLですが、markdownのpreview時には適切にrenderされます</p>
```


<p>これはHTMLですが、markdownのpreview時には適切にrenderされます</p>

<!-- #endregion -->

<!-- #region -->
### Tableを記述する

markdownにおいて一般的に表はこのように記述することが多い

記述方法
```
| a    | b    |
| :--- | ---: |
| c    | d    |
```

記述結果

| a    | b    |
| :--- | ---: |
| c    | d    |


このように1行で表の内容を記述することもできる
````
```{list-table}
:header-rows: 1

* - カラム名1
  - カラム名2
  - カラム名3
* - 1行目のカラム名1の要素
  - 1行目のカラム名2の要素
  - 1行目のカラム名3の要素
* - 2行目のカラム名1の要素
  - 2行目のカラム名2の要素
  - 2行目のカラム名3の要素
* - 3行目のカラム名1の要素
  - 3行目のカラム名2の要素
  - 3行目のカラム名3の要素
* - 4行目のカラム名1の要素
  - 4行目のカラム名2の要素
  - 4行目のカラム名3の要素
```
````

実行結果
```{list-table}
:header-rows: 1

* - カラム名1
  - カラム名2
  - カラム名3
* - 1行目のカラム名1の要素
  - 1行目のカラム名2の要素
  - 1行目のカラム名3の要素
* - 2行目のカラム名1の要素
  - 2行目のカラム名2の要素
  - 2行目のカラム名3の要素
* - 3行目のカラム名1の要素
  - 3行目のカラム名2の要素
  - 3行目のカラム名3の要素
* - 4行目のカラム名1の要素
  - 4行目のカラム名2の要素
  - 4行目のカラム名3の要素
```
<!-- #endregion -->







## Blockを記述する
### admonition (意：勧告)を記述する

記述方法
````
```{admonition} admonition(タイトルは自由に決められる)
admonitionを書く場合はこのように記述する
```
````

記述結果

```{admonition} admonition(タイトルは自由に決められる)
admonitionを書く場合はこのように記述する


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



### Cautionを記述する

記述方法
````
```{caution}
cautionを書く場合はこのように記述する
```
````

記述結果
```{caution}
cautionを書く場合はこのように記述する
```


### Attentionを記述する

記述方法
````
```{attention}
attentionを書く場合はこのように記述する
```
````

記述結果
```{attention}
attentionを書く場合はこのように記述する
```


### Tipを記述する

記述方法
````
```{tip}tipを書く場合はこのように記述する
```
````

記述結果
```{tip}tipを書く場合はこのように記述する
```



### Dangerを記述する

記述方法
````
```{danger}dangerを書く場合はこのように記述する
```
````

記述結果
```{danger}dangerを書く場合はこのように記述する
```



### Errorを記述する

記述方法
````
```{error}errorを書く場合はこのように記述する
```
````

記述結果
```{error}errorを書く場合はこのように記述する
```



### Hintを記述する

記述方法
````
```{hint}hintを書く場合はこのように記述する
```
````

記述結果
```{hint}hintを書く場合はこのように記述する
```



### Importantを記述する

記述方法
````
```{important}importantを書く場合はこのように記述する
```
````

記述結果
```{important}importantを書く場合はこのように記述する
```



## Codeを記述する

<!-- #region -->
### ブロックとしてCodeを記述する

記述方法

````
```{code-block} python
    import numpy as np
    print(np.arange(10))
```

- {code-block}を省略することもできる
```python
    import numpy as np
    print(np.arange(10))
```
````

記述結果
```{code-block} python
    import numpy as np
    print(np.arange(10))
```

```python
    import numpy as np
    print(np.arange(10))
```

<!-- #endregion -->

### インラインとしてCodeを記述する

記述方法
```
文章の途中でこのように`learning_rate = 0.0025`のようにcodeを記述することができる.
```

記述結果
文章の途中でこのように`learning_rate = 0.0025`のようにcodeを記述することができる.






## 画像を記述する


### Localに保存されている画像を記述する

記述方法
````
```{figure} ../src/r2d2.png
:height: 150px
:name: figure-example

R2D2はこのような外見のロボットです
```
````

記述結果
```{figure} ../src/r2d2.png
:height: 150px
:name: figure-example

R2D2はこのような外見のロボットです
```

<!-- #region -->
### Linkが分かっている画像を記述する


記述方法
```
![bb8](https://static.wikia.nocookie.net/starwars/images/6/68/BB8-Fathead.png)
```

記述結果
![bb8](https://static.wikia.nocookie.net/starwars/images/6/68/BB8-Fathead.png)
<!-- #endregion -->

## 数式を記述する


### インラインで記述する

記述方法
```
インラインで数式を定義する場合、$で数式を囲む
あるzは$z=\sqrt{x^2+y^2}$のように定義される
```

記述結果
インラインで数式を定義する場合、ドルマークで数式を囲むのみ。
あるzは$z=\sqrt{x^2+y^2}$のように定義される





### ブロックとして数式を記述する

記述方法

````
$$
z=\sqrt{x^3+y^3}
$$
````

記述結果

$$
z=\sqrt{x^3+y^3}
$$



[数式の記述方法についてさらに知りたい人向け](https://jupyterbook.org/en/stable/content/math.html)
