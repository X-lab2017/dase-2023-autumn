## 细则
- 组队规则：1 个人/组

- 作业内容：**完成一个完整的数据作品**

   - 涉及完整的数据科学过程
   - 真实数据、有趣的问题
   - 一个数据作品报告（包括源代码、实验报告）
   - 讲解与演示（每人 10 分钟以内的视频）

- 时间节点：
   - 第 15 周：开始选题
   - 第 16 ~ 18 周：完成项目作品
   - 最终截止时间：**2024 年 1 月 15 日**

- 参考资料：
   - [OpenSODA 大赛](https://github.com/ECNU/OpenSODA)
   - [华东师范大学全民数字素养与人工智能创新应用大赛](https://dl4all.ecnu.edu.cn/6e/ee/c41924a552686/page.htm)

## 任务流程（参考）

### 1. 选题

- 选择一个你真正感兴趣的主题，确保你选择的主题有足够的可获得数据。
- 选择一个**有实际应用意义**的主题，这样你的项目不仅仅是一个练习，而且有可能对现实问题提供解决方案。
- 说明该项目任务的内容和需要达成的目的。
- 说明选题的研究意义与重要性。

#### 例子

1. 针对亚马逊消费者数据的研究

随着互联网的普及和电子商务的迅速发展，消费者在线购物已经成为现代社会中不可或缺的一部分。亚马逊作为全球最大的电商平台之一，吸引了数以亿计的用户，其海量数据蕴含了丰富的信息，深入挖掘这些信息对于理解消费者行为、改进用户体验以及提升商业竞争力具有重要的意义。

![image](https://github.com/X-lab2017/dase-2023-autumn/assets/50283262/478c26db-2ae2-4735-a824-3bf8d57fd964)

2.  2022-2023赛季NBA球员薪水及状态的数据分析与可视化

NBA，作为当今最热门的篮球联赛，随着其快速发展，nba球员的薪资也水涨船高。我们不由得思考，在当今联盟的比赛节奏中，球员的哪些数据更能决定其薪资水平，联盟球员的薪资分布情况。并进一步根据当前赛季的工资帽占比推测出球员的薪资水平。

3. 2023年度B站每周必看数据及热点分析

毫无疑问，B站是中国年轻人使用的最多的视频类网站（软件）。根据bilibili 2023年Q1财报显示，B站日均活跃用户已达9,370万，用户日均使用时长达到96分钟。超过150万UP主（即上传视频者的代称）在B站获得收入，月均投稿量超2,200万。因此，分析B站的每周必看板块的数据以及热点，具有较高的价值。

![image](https://github.com/X-lab2017/dase-2023-autumn/assets/50283262/94a04250-015f-4c83-b3c0-5d88e11c148f)

### 2. 数据获取

#### 网络爬虫

方法参考实验手册

#### API请求

方法参考实验手册

#### 数据集网站下载

1. **UCI Machine Learning Repository**: 提供了大量机器学习领域的数据集，包括分类、回归、聚类等。
2. **Kaggle Datasets**: Kaggle 是一个以数据科学竞赛为主的平台，它也提供了一个数据集平台，包含了来自各个领域的数据。
3. **Google Dataset Search**: Google 提供的一个数据集搜索引擎，可以通过关键词搜索找到各种数据集。
4. **AWS Open Data Registry**: 亚马逊 AWS 提供的开放数据集合集，覆盖了多个领域，可以免费访问。
5. **Data.gov**: 美国政府提供的开放数据平台，包含了来自各个政府机构的数据。
6. **Microsoft Research Open Data**: 微软研究提供的一些开放数据集，涵盖了计算机科学、社会科学等领域。
7. **IMDb Datasets**: IMDb 提供的数据接口，包含了电影、电视剧等娱乐行业的数据。

### 3. 数据预处理

- 删除重复数据
- 缺失值处理
- 数据类型变换

具体内容可以参考实验手册

### 4. 数据探索

- 基本数据统计信息
- 数据可视化展示

具体内容可以参考实验手册

### 5. 特征工程

- 相关性分析

<img width="900" alt="image" src="https://github.com/X-lab2017/dase-2023-autumn/assets/50283262/dcc57013-125c-4dc2-b12b-09b605b999e6">

- 主成分分析

### 6. 数据建模

- 机器学习方法
- 深度学习方法

### 7. 结论

##  部分作品展示

### 完整数据科学流程

1. [LOL游戏前十分钟的对局数据分析，预测该局游戏的最终胜方](https://github.com/Bret-t/ds-2023/blob/main/final_assignment/%E5%A4%A7%E4%BD%9C%E4%B8%9A%E8%AE%B2%E8%A7%A3.md)
2. [基于LSTM模型的城市用电量预测](https://github.com/ERQIs/data_science_homework/tree/master/final_project)
3. [PokeMon（Gen1 - Gen7）数据分析](https://github.com/DarkWesley/DataScience_Homework/tree/master/FinalProject)
   
### 可视化展示

1. [开源社区对比研究](https://github.com/X-lab2017/open-digger/blob/master/cooperations/paddle_hackathon_3rd/89_%E6%BA%90%E5%85%89%E9%97%AA%E7%83%81.ipynb)
2. [2023年度B站每周必看数据及热点分析](https://github.com/limbo-t/Assignments_for_DS2023/tree/main/final)
3. [2018-2023五年间玩家群体中gpu型号的调查](https://github.com/Gav1n-is-here/ds-2023-autumn/tree/main/PyCode/ds2023-week09)

### 论文复现

1. [基于Hidden Markov map matching的GPS路径匹配与可视化，以及基于深度生成模型的行程时间分布学习](https://github.com/ArcueidType/DataScience/tree/main/DeepGTT)
2. [基于深度学习的多模态图像识别与描述生成](https://github.com/immorrrtal/DataScience2023/tree/master/L09)

## 温馨提示

1. 将仓库内的文件整理好，注意文件命名以及commit message的**规范**。
2. 最终实验报告用PDF、MD或者ipynb的格式呈现。
3. **讲解视频**可以放在仓库里或者上传到在线网站(附上链接)。
4. 完成项目期间遇到的问题，可以记录在实验报告中，**什么问题、为何出现、如何解决**。
