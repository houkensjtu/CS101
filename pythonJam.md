## 关于Python包管理的一锅浆糊 :sob:

伴随着机械学习和人工智能的火爆，Python语言也在近5年经历了井喷式的用户人口增长。更多的用户为Python带来了更多的开发活力，也在同时导致了Python
处在一个相对激烈的不断进化过程之中。在这些进化的进程中，个人最头晕的问题莫过于Python的package安装管理机制。从最早的easy_install到setuptools，
后又出现了类似于Linux包管理器的pip，在这之上又发展出了虚拟环境virtualenv和pipenv，更别说如果你安装了Anaconda发行版还有conda管理器。
所有这些东西相互功能有所重叠又有所不同，且同时存活于现在的大环境之中，着实让笔者的思维每每想到这里都犹如便秘一般，欲要一泻千里脱下裤子却发现
动力不足。这里准备收集并整理一些有关这个话题的重要信息，希望在不久的将来可以理清这些头绪，排出体内淤积的恶臭元素。。

### easy_install

### setuptools

### pip

### virtualenv

### pipenv
根据[PyPA组织的推荐](https://packaging.python.org/guides/tool-recommendations/)，pipenv是目前从事**Python应用开发时**推荐的环境工具。
当然这并不意味着在所有场合下你都要使用pipenv来安装包。一个典型的场景是你有时需要安装一些用Python编写的工具，比如[MyPy](https://github.com/python/mypy)
### Anaconda

### Misc考察

#### 1. 在Linux上用sudo安装Python的包有什么后果？
