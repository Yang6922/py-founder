# 项目环境与工具配置

## 环境
- **Python**: 使用 Anaconda 管理 Python 环境

## 工具
- **PyCharm**: 用于开发与调试
- **Jupyter Notebook**: 用于数据分析与实验

---

# 技术要点

## 基础知识
1. **Python 基础**:
   - 数据类型与结构
   - 流程控制
   - 函数与模块
   - 异常处理

2. **HTTP 基础**:
   - 请求与响应
   - HTTP 方法（GET、POST 等）
   - 状态码及其含义
   - Headers 和 Cookies

---

## 爬取与解析
1. **Requests 库**:
   - 发起 HTTP 请求
   - 处理响应数据
   - 模拟 Headers、Cookies 等

2. **BeautifulSoup 解析 HTML**:
   - DOM 树的导航与操作
   - 查找节点：`find()` 和 `find_all()`
   - 使用 CSS 选择器解析页面内容

---

## 数据存储
1. **存储为 CSV 文件**:
   - 使用 `csv` 模块或 Pandas 写入
2. **存储为 Excel 文件**:
   - 使用 Pandas 的 `to_excel` 方法

---

## 数据处理与分析
1. **Pandas**:
   - 数据读取与清洗
   - 数据选择、过滤与分组
   - 数据的聚合与变换

2. **NumPy**:
   - 数值计算与数组操作
   - 矩阵运算与线性代数

---

## 数据可视化
1. **Matplotlib**:
   - 基础绘图（折线图、柱状图、散点图等）
   - 图像自定义（标题、坐标轴、颜色等）

2. **Seaborn**:
   - 高级统计图表（箱型图、热力图等）
   - 与 Pandas 的 DataFrame 集成

---

## 并发性能优化
1. **Asyncio 和 Aiohttp**:
   - 使用异步编程提升爬取效率
   - 协程的基本概念与使用
   - 管理任务队列并发请求
