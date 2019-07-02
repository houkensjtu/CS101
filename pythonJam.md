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
当然这并不意味着在所有场合下你都要使用pipenv来安装包。一个典型的场景是你有时需要安装一些用Python编写的系统工具，比如[MyPy](https://github.com/python/mypy)。此类估计会在系统上所有用户共同共享，且相对不受版本问题困扰的工具类python包，可以用pip来直接安装。以下是一些关于pipenv的问答。   
- **已经有了pip和virtualenv，为什么还需要pipenv?**   
pipenv根据其[原作者的描述](https://docs.pipenv.org/en/latest/)，是整合了pip和virtualenv，从而向用户提供了一个更加完备且具有自我一致性的工具界面（不再需要由用户分别操作pip和virtualenv）。其初衷是将业界目前领先的包管理机制（比如npm和yarn）引入到Python中来。
- **pipenv是用来安装管理包的，那pipenv自己要怎么安装?**  
pipenv推荐用户先安装pip，然后通过pip在用户目录下进行用户安装。这个命令会将pipenv安装到用户目录下的~/.local/bin/中。一般此目录不在系统的PATH搜索路径中，因此需要手动添加。pipenv网站推荐将添加语句加到~/.profile中。
```
$ pip install --user pipenv
```

- **pipenv相比virtualenv好在哪里?**  
virtualenv的一个显著缺点是，为了激活虚拟环境，需要找到相应的project目录下面的bin/activate来启动。时间久了以后，各种虚拟环境的文件在系统中就会散布开来且开发者迟早会忘记他们的位置。pipenv的启动是一个统一的命令$ pipenv shell，且所有的文件都会安装project名字分类自动安装到./local文件中。项目文件下不保存虚拟环境相关的文件，**只保留一个存档Pipfile**。这样，**你如果拷贝这个项目到新的机器上，需要安装虚拟环境和依赖的包时只需要**
```
pipenv install
pipenv shell
```
### Anaconda

### Misc考察

#### 1. 在Linux上用sudo安装Python的包有什么后果？
