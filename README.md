# OneChartLab Slides

**简体中文** | [English](README.en.md)

OneChartLab Slides 是一个用于制作 HTML 演示文稿的 Agent Skill。它内置两套共享 16 种版式与公共交互运行时的模板：默认的 **ZXcharT Briefing** 用于研究、策略、数据和决策汇报；可选的 **ZXcharT Showcase** 用于发布会、提案、演讲和故事化展示。

安装后，向 Agent 提供主题、材料、受众和制作要求，即可生成可在浏览器中播放并继续修改的演示文稿。未指定模板时默认使用 Briefing。

## 主要功能

- 根据文章、报告、数据或提纲规划演示结构
- 在生成前提供逐页大纲供用户确认
- 根据沟通任务选择 Briefing 或 Showcase，并自动匹配封面、目录、数据、对比、时间轴和观点等版式
- 生成包含样式与交互的独立 HTML 演示文稿
- 支持键盘、触控和页面按钮翻页
- 支持卡片聚焦、条形图动画和减少动态效果设置
- 检查文字溢出、页面可读性、来源链接和内容完整性
- 使用 CSS 变量统一管理颜色、字体和间距

## 安装 Skill

请安装完整的 `onechartlab-slides` 文件夹。模板、设计规范、版式说明和脚本都属于 Skill 的组成部分。

使用 ZIP 上传时，压缩包内应只有一个顶层文件夹：

```text
onechartlab-slides/
└── SKILL.md
```

### HanaAgent

让 HanaAgent 从 GitHub 安装，或在 Skill 安装界面选择仓库/ZIP：

```text
请安装这个 Skill：https://github.com/ZXcharT/onechartlab-slides
```

手动安装方法参见 [docs/platforms/hanaagent.md](docs/platforms/hanaagent.md)。

### Claude

1. 启用 **Code execution and file creation**；
2. 进入 **Customize → Skills**；
3. 选择 **Add/Create skill → Upload a skill**；
4. 上传内部顶层文件夹为 `onechartlab-slides/` 的 ZIP。

### OpenAI Codex

可以让 `$skill-installer` 从 GitHub 安装，也可以把完整文件夹放到：

```text
~/.agents/skills/onechartlab-slides/
```

项目专用安装位置：

```text
项目目录/.agents/skills/onechartlab-slides/
```

如果新安装的 Skill 没有出现，请重启 Codex。

## 快速开始

安装后，直接向 Agent 描述任务：

```text
请使用 OneChartLab Slides，把这份季度经营总结制作成 10 页中文演示文稿。
受众是公司管理层，重点展示核心指标、问题和下一步计划。
先给我逐页大纲，确认后再生成 HTML。
```

标准流程：

1. Agent 阅读材料并确认主题、受众、页数和输出位置；
2. Agent 生成逐页大纲并匹配版式；
3. 用户确认大纲；
4. Agent 确认模板（未指定时使用 Briefing），创建 HTML 文件并写入内容；
5. Agent 在浏览器中检查排版、翻页和交互；
6. Agent 根据反馈修改并返回文件位置。

默认成品位置：

```text
projects/项目名称/index.html
```

## 使用要求

- 需要能够读取和写入本地文件的 AI Agent
- 建议 Agent 具备浏览器预览能力
- 演示文稿使用当前版本的 Chrome、Edge、Firefox 或 Safari 播放
- 手动复制模板不需要 Python；运行任一可选命令行生成器时需要 Python 3

## 模板选择

- **ZXcharT Briefing（默认）**：研究报告、策略推演、数据分析、项目复盘和内部决策。视觉克制、层级平面、适合证据密集内容。
- **ZXcharT Showcase（可选）**：产品发布、商业提案、主题演讲和叙事展示。使用模块化卡片、舞台化构图和受控氛围动效。

两套模板不是新旧版本或质量等级；它们共享相同版式标识、键盘/触控导航、聚焦交互、无障碍和 reduced-motion 契约。

## 内置版式

- **开场与收尾**：`layout-cover`、`layout-outro`、`layout-closing`
- **目录与内容结构**：`layout-agenda`、`layout-split`、`layout-detail`、`layout-stack`
- **数据与比较**：`layout-metrics`、`layout-dashboard`、`layout-bars`、`layout-compare`
- **叙事与观点**：`layout-quote`、`layout-timeline`、`layout-timeline-3col`、`layout-hook`、`layout-statement`

详细说明参见 [docs/layouts.md](docs/layouts.md)。

## 关键文件

```text
.
├── SKILL.md                       Skill 入口与执行要求
├── AGENTS.md                      制作和检查流程
├── template.html                  默认 ZXcharT Briefing 模板
├── templates/showcase.html        可选 ZXcharT Showcase 模板
├── templates/briefing.manifest.json  Briefing 验收摘要锁
├── index.html                     两套模板与精选版式预览
├── themes/zxchart/design.md       Briefing 视觉规范
├── themes/showcase/design.md      Showcase 视觉规范
├── docs/                          布局、定制和平台说明
├── examples/agent-workflow/       通用 Agent 工作流示例
├── scripts/                       可选项目生成脚本和检查器
├── projects/                      默认成品目录
└── assets/                        图片等项目素材
```

## 可选：使用命令行创建项目

### macOS / Linux

```sh
sh scripts/new-project.sh "my-deck"                         # 默认 Briefing
sh scripts/new-project.sh --template briefing "my-briefing"
sh scripts/new-project.sh --template showcase "my-showcase"
```

### Windows

```powershell
py scripts/new-project.py "my-deck"                         # 默认 Briefing
py scripts/new-project.py --template briefing "my-briefing"
py scripts/new-project.py --template showcase "my-showcase"
```

Shell 是 Python 生成器的薄包装；两种入口共享相同参数、错误码和默认模板。所有命令都会创建：

```text
projects/my-deck/index.html
```

## 致谢

模板基础来自 Zara Zhang 的 [beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates)，采用 MIT 许可证。[frontend-slides](https://github.com/zarazhangrui/frontend-slides) 和 [html-presentation](https://github.com/juanjuanjie/html-presentation) 为工作流与演示方法提供了参考。详情参见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 和 [SOURCES.md](SOURCES.md)。

## 许可证与商标

代码、文档和通用示例采用 [MIT 许可证](LICENSE)。OneChartLab、OneChartLab Slides、ZXcharT 名称及其 Logo 的相关权利保留，详见 [TRADEMARKS.md](TRADEMARKS.md)。
